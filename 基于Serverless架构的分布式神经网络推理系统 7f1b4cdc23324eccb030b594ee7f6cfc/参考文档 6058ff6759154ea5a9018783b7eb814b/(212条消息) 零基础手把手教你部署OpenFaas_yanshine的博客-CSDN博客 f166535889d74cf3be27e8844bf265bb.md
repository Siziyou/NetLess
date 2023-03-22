# (212条消息) 零基础手把手教你部署OpenFaas_yanshine的博客-CSDN博客

[https://blog.csdn.net/yanshine/article/details/102958263](https://blog.csdn.net/yanshine/article/details/102958263)

**引言**

- 本文的特点一：本文是零基础教程，本文包括Kubernetes安装过程，如果对Kubernetes非常清楚可以跳过安装过程。
- 本文的特点二：不用翻墙过程(科学上网)，不用翻墙，不用翻墙。重要的事情说三遍。虽然不是所有的源都是国内镜像比如dockerhub，但都不用翻墙。
- 本文的特点三：安装Kubernetes和OpenFaas都是点到为止，一堆插件都不装，几乎是能用起来的最简模式，就是用于零基础的。
- 本文的特点四：简明扼要废话少，格式清晰
- 读本文也要注意：资源都是现下载的，不是绿色的。您安装时版本可能不一致。

**我的环境还是要说一下，您的环境不同没有关系**

- Centos 7.6
- Docker 19.03.4
- Kubernetes 1.16.2
- 同时注意：你要有个dockerhub的仓库

话不多说，开整

### 目录

- [安装Docker和kubeadm（整个这部分master和各node都需要安装）](https://blog.csdn.net/yanshine/article/details/102958263#Dockerkubeadmmasternode_15)
- [系统环境配置](https://blog.csdn.net/yanshine/article/details/102958263#_19)[安装kube-proxy会用到的ipvs](https://blog.csdn.net/yanshine/article/details/102958263#kubeproxyipvs_49)[安装Docker](https://blog.csdn.net/yanshine/article/details/102958263#Docker_80)[安装kubeadm和kubelet](https://blog.csdn.net/yanshine/article/details/102958263#kubeadmkubelet_122)
- [安装Kubernetes（使用kubeadm）](https://blog.csdn.net/yanshine/article/details/102958263#Kuberneteskubeadm_179)
- [拉取kubernetes所需镜像](https://blog.csdn.net/yanshine/article/details/102958263#kubernetes_180)[创建一个安装配置文件](https://blog.csdn.net/yanshine/article/details/102958263#_203)[安装部署kubernetes](https://blog.csdn.net/yanshine/article/details/102958263#kubernetes_225)[安装flannel插件（必须安装否则启动不正常）](https://blog.csdn.net/yanshine/article/details/102958263#flannel_298)[确认运行正常（nodes是Ready，pod都是Running状态）](https://blog.csdn.net/yanshine/article/details/102958263#nodesReadypodRunning_306)
- [安装OpenFaas](https://blog.csdn.net/yanshine/article/details/102958263#OpenFaas_337)
- [安装faas-netes(这是OpenFaas的核心组件)](https://blog.csdn.net/yanshine/article/details/102958263#faasnetesOpenFaas_338)[给openfaas创建密码（必须要做否则必入坑）](https://blog.csdn.net/yanshine/article/details/102958263#openfaas_355)[安装openfaas的所有组件](https://blog.csdn.net/yanshine/article/details/102958263#openfaas_362)[下载faas-cli工具（就一个可执行文件，官方被墙直接下吧）](https://blog.csdn.net/yanshine/article/details/102958263#faascli_383)[写个小例子](https://blog.csdn.net/yanshine/article/details/102958263#_394)[常用命令整理](https://blog.csdn.net/yanshine/article/details/102958263#_453)
- [不要忘记别人的功劳](https://blog.csdn.net/yanshine/article/details/102958263#_469)

# 安装Docker和kubeadm（整个这部分master和各node都需要安装）

1. 用kubeadm的安装方式简单，所以采用这种方式。
2. Kubernetes只装了个master，单我会指明哪些是master和其他node都要用到的命令。

## 系统环境配置

添加主机名

```
cat /etc/hosts
#添加内容
192.168.10.100 master
123
```

关闭防火墙

```
systemctl stop firewalld
systemctl disable firewalld
12
```

禁用SELINUX：

```
setenforce 0
vi /etc/selinux/config
SELINUX=disabled
123
```

创建/etc/sysctl.d/k8s.conf文件，添加如下内容：

```
vi /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
1234
```

使其生效

```
modprobe br_netfilter
sysctl -p /etc/sysctl.d/k8s.conf
12
```

## 安装kube-proxy会用到的ipvs

```
vi /etc/sysconfig/modules/ipvs.modules
#!/bin/bash
modprobe -- ip_vs
modprobe -- ip_vs_rr
modprobe -- ip_vs_wrr
modprobe -- ip_vs_sh
modprobe -- nf_conntrack_ipv4
1234567
```

使其生效

```
chmod 755 /etc/sysconfig/modules/ipvs.modules
bash /etc/sysconfig/modules/ipvs.modules
lsmod | grep -e ip_vs -e nf_conntrack_ipv4
配置成功将看到：
[root@node1 ~]# lsmod | grep -e ip_vs -e nf_conntrack_ipv4
nf_conntrack_ipv4      15053  10
nf_defrag_ipv4         12729  1 nf_conntrack_ipv4
ip_vs_sh               12688  0
ip_vs_wrr              12697  0
ip_vs_rr               12600  0
ip_vs                 145497  6 ip_vs_rr,ip_vs_sh,ip_vs_wrr
nf_conntrack          133095  9 ip_vs,nf_nat,nf_nat_ipv4,nf_nat_ipv6,xt_conntrack,nf_nat_masquerade_ipv4,nf_conntrack_netlink,nf_conntrack_ipv4,nf_conntrack_ipv6
libcrc32c              12644  4 xfs,ip_vs,nf_nat,nf_conntrack
12345678910111213
```

安装ipvs用到的软件包和管理工具

```
yum install ipset
yum install ipvsadm
12
```

## 安装Docker

```
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
123
```

查看最新的Docker版本

```
yum list docker-ce.x86_64  --showduplicates |sort -r
docker-ce.x86_64            3:18.09.7-3.el7                     docker-ce-stable
docker-ce.x86_64            3:18.09.6-3.el7                     docker-ce-stable
docker-ce.x86_64            3:18.09.5-3.el7                     docker-ce-stable
docker-ce.x86_64            3:18.09.4-3.el7                     docker-ce-stable
docker-ce.x86_64            3:18.09.3-3.el7                     docker-ce-stable
docker-ce.x86_64            3:18.09.2-3.el7                     docker-ce-stable
1234567
```

安装新的Docker并启动

```
yum makecache fast

yum install -y --setopt=obsoletes=0 docker-ce-18.09.7-3.el7

systemctl start docker
systemctl enable docker
123456
```

修改docker cgroup driver为systemd

```
vi /etc/docker/daemon.json

{
  "exec-opts": ["native.cgroupdriver=systemd"]
}
12345
```

重启docker

```
systemctl restart docker
1
```

查看一下是否修改成功

```
docker info | grep Cgroup
Cgroup Driver: systemd
12
```

## 安装kubeadm和kubelet

添加yum源，国内源

```
vi /etc/yum.repos.d/kubernetes.repo
添加如下内容
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
123456789
```

安装

```
yum makecache fast
yum install -y kubelet kubeadm kubectl
12
```

关闭swap分区

```
swapoff -a
1
```

```
vi /etc/fstab

注释掉swap的那一行

# Created by anaconda on Tue Jun 11 22:47:09 2019
#
# Accessible filesystems, by reference, are maintained under '/dev/disk'
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
#
/dev/mapper/centos-root /                       xfs     defaults        0 0
UUID=564e4172-ea50-4676-8e80-3f94a97c9b62 /boot                   xfs     defaults        0 0
/dev/mapper/centos-home /home                   xfs     defaults        0 0
#/dev/mapper/centos-swap swap                    swap    defaults        0 0

1234567891011121314
```

```
vi /etc/sysctl.d/k8s.conf
添加一行
vm.swappiness=0
123
```

```
sysctl -p /etc/sysctl.d/k8s.conf
1
```

再配置kubelet的配置去掉这个限制

```
vi /etc/sysconfig/kubelet
KUBELET_EXTRA_ARGS=--fail-swap-on=false
12
```

启动kubeadm的服务kubelet.service

```
systemctl enable kubelet.service
1
```

# 安装Kubernetes（使用kubeadm）

## 拉取kubernetes所需镜像

```
vi /home/docker_pull_kube.sh
写入如下内容：用kubeadm config images list 先确认可用版本
#! /bin/bash
images=(
    kube-apiserver:v1.16.2
    kube-controller-manager:v1.16.2
    kube-scheduler:v1.16.2
    kube-proxy:v1.16.2
    pause:3.1
    etcd:3.3.15-0
    coredns:1.6.2
)
for imageName in ${images[@]} ; do
    docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/$imageName
    docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/$imageName k8s.gcr.io/$imageName
done
12345678910111213141516
```

```
bash /home/docker_pull_kube.sh
1
```

## 创建一个安装配置文件

```
vi /home/kubeadm.yaml

写入如下内容：

apiVersion: kubeadm.k8s.io/v1beta2
kind: InitConfiguration
localAPIEndpoint:
  advertiseAddress: 192.168.10.100
  bindPort: 6443
nodeRegistration:
  taints:
  - effect: PreferNoSchedule
    key: node-role.kubernetes.io/master
---
apiVersion: kubeadm.k8s.io/v1beta2
kind: ClusterConfiguration
kubernetesVersion: v1.16.2
networking:
  podSubnet: 10.244.0.0/16
12345678910111213141516171819
```

## 安装部署kubernetes

```
kubeadm init --config kubeadm.yaml --ignore-preflight-errors=Swap

运行结果如下：
[init] Using Kubernetes version: v1.15.0
[preflight] Running pre-flight checks
    [WARNING Swap]: running with swap on is not supported. Please disable swap
[preflight] Pulling images required for setting up a Kubernetes cluster
[preflight] This might take a minute or two, depending on the speed of your internet connection
[preflight] You can also perform this action in beforehand using 'kubeadm config images pull'
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Activating the kubelet service
[certs] Using certificateDir folder "/etc/kubernetes/pki"
[certs] Generating "etcd/ca" certificate and key
[certs] Generating "apiserver-etcd-client" certificate and key
[certs] Generating "etcd/server" certificate and key
[certs] etcd/server serving cert is signed for DNS names [node1 localhost] and IPs [192.168.99.11 127.0.0.1 ::1]
[certs] Generating "etcd/peer" certificate and key
[certs] etcd/peer serving cert is signed for DNS names [node1 localhost] and IPs [192.168.99.11 127.0.0.1 ::1]
[certs] Generating "etcd/healthcheck-client" certificate and key
[certs] Generating "ca" certificate and key
[certs] Generating "apiserver" certificate and key
[certs] apiserver serving cert is signed for DNS names [node1 kubernetes kubernetes.default kubernetes.default.svc kubernetes.default.svc.cluster.local] and IPs [10.96.0.1 192.168.99.11]
[certs] Generating "apiserver-kubelet-client" certificate and key
[certs] Generating "front-proxy-ca" certificate and key
[certs] Generating "front-proxy-client" certificate and key
[certs] Generating "sa" key and public key
[kubeconfig] Using kubeconfig folder "/etc/kubernetes"
[kubeconfig] Writing "admin.conf" kubeconfig file
[kubeconfig] Writing "kubelet.conf" kubeconfig file
[kubeconfig] Writing "controller-manager.conf" kubeconfig file
[kubeconfig] Writing "scheduler.conf" kubeconfig file
[control-plane] Using manifest folder "/etc/kubernetes/manifests"
[control-plane] Creating static Pod manifest for "kube-apiserver"
[control-plane] Creating static Pod manifest for "kube-controller-manager"
[control-plane] Creating static Pod manifest for "kube-scheduler"
[etcd] Creating static Pod manifest for local etcd in "/etc/kubernetes/manifests"
[wait-control-plane] Waiting for the kubelet to boot up the control plane as static Pods from directory "/etc/kubernetes/manifests". This can take up to 4m0s
[apiclient] All control plane components are healthy after 26.004907 seconds
[upload-config] Storing the configuration used in ConfigMap "kubeadm-config" in the "kube-system" Namespace
[kubelet] Creating a ConfigMap "kubelet-config-1.15" in namespace kube-system with the configuration for the kubelets in the cluster
[upload-certs] Skipping phase. Please see --upload-certs
[mark-control-plane] Marking the node node1 as control-plane by adding the label "node-role.kubernetes.io/master=''"
[mark-control-plane] Marking the node node1 as control-plane by adding the taints [node-role.kubernetes.io/master:PreferquNoSchedule]
[bootstrap-token] Using token: 4qcl2f.gtl3h8e5kjltuo0r
[bootstrap-token] Configuring bootstrap tokens, cluster-info ConfigMap, RBAC Roles
[bootstrap-token] configured RBAC rules to allow Node Bootstrap tokens to post CSRs in order for nodes to get long term certificate credentials
[bootstrap-token] configured RBAC rules to allow the csrapprover controller automatically approve CSRs from a Node Bootstrap Token
[bootstrap-token] configured RBAC rules to allow certificate rotation for all node client certificates in the cluster
[bootstrap-token] Creating the "cluster-info" ConfigMap in the "kube-public" namespace
[addons] Applied essential addon: CoreDNS
[addons] Applied essential addon: kube-proxy

Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 192.168.10.100:6443 --token 4qcl2f.gtl3h8e5kjltuo0r \
    --discovery-token-ca-cert-hash sha256:7ed5404175cc0bf18dbfe53f19d4a35b1e3d40c19b10924275868ebf2a3bbe6e
123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869
```

## 安装flannel插件（必须安装否则启动不正常）

```
curl -O https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
sed -i 's/quay.io\/coreos/registry.cn-beijing.aliyuncs.com\/imcto/g' kube-flannel.yml
# 安装flannel
kubectl apply -f kube-flannel.yml
1234
```

## 确认运行正常（nodes是Ready，pod都是Running状态）

```
[root@node1 home]$ kubectl get cs
NAME                 AGE
controller-manager   <unknown>
scheduler            <unknown>
etcd-0               <unknown>

[root@node1 home]$ kubectl get nodes
NAME    STATUS   ROLES    AGE   VERSION
node1   Ready    master   26h   v1.16.2

[root@node1 home]$ kubectl get pod -n kube-system
NAME                            READY   STATUS    RESTARTS   AGE
coredns-5644d7b6d9-9qln2        1/1     Running   0          26h
coredns-5644d7b6d9-nqlg2        1/1     Running   0          26h
etcd-node1                      1/1     Running   0          26h
kube-apiserver-node1            1/1     Running   0          26h
kube-controller-manager-node1   1/1     Running   0          26h
kube-flannel-ds-amd64-bpwlj     1/1     Running   0          26h
kube-proxy-lwnxj                1/1     Running   0          26h
kube-scheduler-node1            1/1     Running   0          26h
1234567891011121314151617181920
```

Kubernetes安装完成
 其实helm和dashboard等都不用安装。都是一些易用工具，如果有需要这都是Kubernetes的内容。对OpenFaas的首次部署意义不大。

**如果想搭建Kubernetes集群，只需要在node中安装好该安装的kubeadm和docker(前文提到了)，然后运行:**

> 
> 
> 
> kubeadm join 192.168.10.100:6443 --token 4qcl2f.gtl3h8e5kjltuo0r  –discovery-token-ca-cert-hash sha256:7ed5404175cc0bf18dbfe53f19d4a35b1e3d40c19b10924275868ebf2a3bbe6e
> 

# 安装OpenFaas

## 安装faas-netes(这是OpenFaas的核心组件)

```
git clone https://github.com/openfaas/faas-netes
cd faas-netes
kubectl apply -f ./namespaces.yml
123
```

验证是否成功创建openfaas，openfaas-fn两个namespaces

```
[root@node1 home] kubectl get namespaces
NAME              STATUS   AGE
default           Active   26h
kube-node-lease   Active   26h
kube-public       Active   26h
kube-system       Active   26h
openfaas          Active   26h
openfaas-fn       Active   26h
12345678
```

## 给openfaas创建密码（必须要做否则必入坑）

```
kubectl -n openfaas create secret generic basic-auth \
--from-literal=basic-auth-user=admin \
--from-literal=basic-auth-password=admin
123
```

## 安装openfaas的所有组件

```
git clone https://github.com/openfaas/faas-netes
cd faas-netes
kubectl apply -f ./yaml/
123
```

验证是否安装成功

```
[root@node1 home]$ kubectl get pod -n openfaas
NAME                                READY   STATUS    RESTARTS   AGE
alertmanager-667c74c9c9-zsx66       1/1     Running   0          27h
basic-auth-plugin-76899dc95-78qjc   1/1     Running   0          27h
faas-idler-86b55ffcbf-k4xkd         1/1     Running   0          27h
gateway-8549c458c9-h6l6z            2/2     Running   1          27h
nats-6b6d549b56-rvgv4               1/1     Running   0          27h
prometheus-b4cbb9bdc-2q8dg          1/1     Running   0          27h
queue-worker-554946dc65-gsvcp       1/1     Running   0          27h
123456789
```

如果出现ImagePullBackOff，ErrImagePull，可能是网络问题，可以先等等。

## 下载faas-cli工具（就一个可执行文件，官方被墙直接下吧）

```
https://github.com/openfaas/faas-cli/releases

去下载吧，windows和linux的都有
123
```

放入bin中

```
cp faas-cli /usr/local/bin
1
```

## 写个小例子

登录docker hub (必须要登录成功否则无法继续)

```
docker login -u 你的用户名 -p 你的密码
1
```

准备一个函数，python的

```
mkdir -p /home/functions
cd /home/functions
faas-cli new --lang python hello-python
123
```

这会生成hello-python.yml，hello-python文件夹

修改下hello-python/handler.py文件

```
vi hello-python/handler.py

def handle(req):
    print("Hello! You said: " + req)
1234
```

修改下hello-python.yml文件

```
vi hello-python.yml:

provider:
  name: faas
  gateway: http://192.168.10.100:31112

functions:
  hello-python:
    lang: python
    handler: ./hello-python
    image: yourName/hello-python（yourName这个地址是dockerhub地址）
1234567891011
```

```
faas-cli build -f ./hello-python.yml
1
```

下面是上传，部署，和运行，这个步骤还是很耗时的。（其实主要是网络速度，如果docker仓库在本地就没问题了）

```
faas-cli push -f ./hello-python.yml
1
```

这样你的node节点，就可以有地方下载了，当然如果你有私有镜像仓库，就传到私有镜像仓库。我这里使用的是docker.hub。接下来部署

```
faas-cli deploy -f ./hello-python.yml
1
```

运行

```
[root@node1 home]$ curl 127.0.0.1:31112/function/hello-python -d "123456"
hello:123456
123456
123
```

至此OpenFaas全部安装结束

### 常用命令整理

```
kubectl get pod -n kube-system
kubectl get cs
kubectl get nodes
kubectl get namespaces
1234
```

彻底卸载kube

```
kubeadm reset
ifconfig cni0 down
ip link delete cni0
ifconfig flannel.1 down
ip link delete flannel.1
rm -rf /var/lib/cni/
123456
```

# 不要忘记别人的功劳

1. https://www.kubernetes.org.cn/5551.html
2. https://www.2cto.com/net/201804/734810.html