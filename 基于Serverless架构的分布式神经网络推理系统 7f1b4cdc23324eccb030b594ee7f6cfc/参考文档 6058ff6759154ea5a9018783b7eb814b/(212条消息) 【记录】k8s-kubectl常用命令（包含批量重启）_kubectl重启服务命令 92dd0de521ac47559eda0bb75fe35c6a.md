# (212条消息) 【记录】k8s-kubectl常用命令（包含批量重启）_kubectl重启服务命令_沐子·李的博客-CSDN博客

[https://blog.csdn.net/u010328311/article/details/122992654](https://blog.csdn.net/u010328311/article/details/122992654)

### 1：在[k8s](https://so.csdn.net/so/search?q=k8s&spm=1001.2101.3001.7020) master节点使用命令获取kuboard访问token

```
kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep kuboard-user | awk '{print $1}')
1
```

### 2：获取命名空间列表

```
kubectl get namespaces
1
```

### 3：在k8s master节点使用命令查看kuboard是否已在运行

```
kubectl get pods -n kube-system | grep kuboard
1
```

### 4：获取节点信息

```
kubectl get nodes
1
```

### 5：获取【kube-system命名空间】下的pod列表

```
# kubectl get pods -n <namespcae>

kubectl get pods -n kube-system
123
```

### 6：获取【kube-system命名空间】下某个节点信息

```
# kubectl describe pod -n <namespace>  <pod-name>

kubectl describe pod -n kube-system kuboard-6d9dc76cd7-r2r27
123
```

### 7：获取 Node的详细信息

```
kubectl describe nodes <node-name>
1
```

### 8：查看rc和sercice列表

```
 kubectl get rc,service
1
```

### 9：根据[yaml配置文件](https://so.csdn.net/so/search?q=yaml%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6&spm=1001.2101.3001.7020)一次创建service和rc

```
 kubectl create -f my-service.yaml -f my-rc.yaml
1
```

### 10：根据目录下所有.yaml、.yml、.json文件的定义进行创建操作

```
kubectl create -f <directory>
1
```

### 11：删除所有Pod

```
kubectl delete pods --all
1
```

### 12：执行Pod的date命令，默认使用Pod的第1个容器执行

```
 kubectl exec <pod-name> date
1
```

### 13：指定Pod中某个容器执行date命令

```
 kubectl exec <pod-name> -c <container-name> date
1
```

### 14：通过bash获得Pod中某个容器的TTY，相当于登陆容器

```
 kubectl exec -it <pod-name> -c <container-name> /bin/bash
1
```

### 15：查看容器输出到stdout的日志

```
 kubectl logs <pod-name>  -n <namespace-name>
1
```

### 16：跟踪查看容器的日志，相当于tail -f命令的结果

```
kubectl logs -f <pod-name> -n <namespace-name>
1
```

### `17：批量重启（批量删除容器）`

```
kubectl get pods -n <namespace> | awk '{print $1}' | xargs kubectl delete pod -n <namespace>
1
```

### 18：kubernetes获取join命令

```
kubeadm token create --print-join-command
1
```

### 19：卸载k8s

```
kubeadm reset -f
1
```

### 20：查看kubelet日志

```
journalctl -xef -u kubelet -n 20

```

**目录**

[一.kubectl 基本命令操作](https://blog.csdn.net/weixin_57837701/article/details/121101776#%E4%B8%80.kubectl%20%E5%9F%BA%E6%9C%AC%E5%91%BD%E4%BB%A4%E6%93%8D%E4%BD%9C)

[1.陈述式资源管理方法](https://blog.csdn.net/weixin_57837701/article/details/121101776#1.%E9%99%88%E8%BF%B0%E5%BC%8F%E8%B5%84%E6%BA%90%E7%AE%A1%E7%90%86%E6%96%B9%E6%B3%95)

[查看版本信息](https://blog.csdn.net/weixin_57837701/article/details/121101776#%E6%9F%A5%E7%9C%8B%E7%89%88%E6%9C%AC%E4%BF%A1%E6%81%AF)

[查看资源对象简写](https://blog.csdn.net/weixin_57837701/article/details/121101776#%E6%9F%A5%E7%9C%8B%E8%B5%84%E6%BA%90%E5%AF%B9%E8%B1%A1%E7%AE%80%E5%86%99)

[查看集群信息](https://blog.csdn.net/weixin_57837701/article/details/121101776#%E6%9F%A5%E7%9C%8B%E9%9B%86%E7%BE%A4%E4%BF%A1%E6%81%AF)

[配置kubectl自动补全](https://blog.csdn.net/weixin_57837701/article/details/121101776#%E9%85%8D%E7%BD%AEkubectl%E8%87%AA%E5%8A%A8%E8%A1%A5%E5%85%A8)

[node 节点查看日志](https://blog.csdn.net/weixin_57837701/article/details/121101776#node%20%E8%8A%82%E7%82%B9%E6%9F%A5%E7%9C%8B%E6%97%A5%E5%BF%97)

[2.基本信息查看](https://blog.csdn.net/weixin_57837701/article/details/121101776#2.%E5%9F%BA%E6%9C%AC%E4%BF%A1%E6%81%AF%E6%9F%A5%E7%9C%8B)

[查看master 节点状态](https://blog.csdn.net/weixin_57837701/article/details/121101776#%E6%9F%A5%E7%9C%8Bmaster%20%E8%8A%82%E7%82%B9%E7%8A%B6%E6%80%81)

[查看命令空间](https://blog.csdn.net/weixin_57837701/article/details/121101776#%E6%9F%A5%E7%9C%8B%E5%91%BD%E4%BB%A4%E7%A9%BA%E9%97%B4)

[查看default命名空间的所有资源](https://blog.csdn.net/weixin_57837701/article/details/121101776#%E6%9F%A5%E7%9C%8Bdefault%E5%91%BD%E5%90%8D%E7%A9%BA%E9%97%B4%E7%9A%84%E6%89%80%E6%9C%89%E8%B5%84%E6%BA%90)

[创建命名空间 (app)](https://blog.csdn.net/weixin_57837701/article/details/121101776#%E5%88%9B%E5%BB%BA%E5%91%BD%E5%90%8D%E7%A9%BA%E9%97%B4%20%28app%29)

[删除命名空间(app)](https://blog.csdn.net/weixin_57837701/article/details/121101776#%E5%88%A0%E9%99%A4%E5%91%BD%E5%90%8D%E7%A9%BA%E9%97%B4%28app%29)

[在命名空间创建副本控制器启动Pod](https://blog.csdn.net/weixin_57837701/article/details/121101776#%E5%9C%A8%E5%91%BD%E5%90%8D%E7%A9%BA%E9%97%B4%E5%88%9B%E5%BB%BA%E5%89%AF%E6%9C%AC%E6%8E%A7%E5%88%B6%E5%99%A8%E5%90%AF%E5%8A%A8Pod)

[查看命名空间kube-public中的pod信息](https://blog.csdn.net/weixin_57837701/article/details/121101776#%E6%9F%A5%E7%9C%8B%E5%91%BD%E5%90%8D%E7%A9%BA%E9%97%B4kube-public%E4%B8%AD%E7%9A%84pod%E4%BF%A1%E6%81%AF)

[kubectl exec](https://blog.csdn.net/weixin_57837701/article/details/121101776#kubectl%20exec)

[重启（删除）pod资源](https://blog.csdn.net/weixin_57837701/article/details/121101776#%E9%87%8D%E5%90%AF%EF%BC%88%E5%88%A0%E9%99%A4%EF%BC%89pod%E8%B5%84%E6%BA%90)

[扩容缩容](https://blog.csdn.net/weixin_57837701/article/details/121101776#%E6%89%A9%E5%AE%B9%E7%BC%A9%E5%AE%B9)

[删除副本控制器](https://blog.csdn.net/weixin_57837701/article/details/121101776#%E5%88%A0%E9%99%A4%E5%89%AF%E6%9C%AC%E6%8E%A7%E5%88%B6%E5%99%A8)

[二.项目的生命周期](https://blog.csdn.net/weixin_57837701/article/details/121101776#%E4%BA%8C.%E9%A1%B9%E7%9B%AE%E7%9A%84%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F)

[1.创建kubectl run命令](https://blog.csdn.net/weixin_57837701/article/details/121101776#1.%E5%88%9B%E5%BB%BAkubectl%20run%E5%91%BD%E4%BB%A4)

[2.发布kubectl expose命令](https://blog.csdn.net/weixin_57837701/article/details/121101776#2.%E5%8F%91%E5%B8%83kubectl%20expose%E5%91%BD%E4%BB%A4)

[3.更新kubectl set](https://blog.csdn.net/weixin_57837701/article/details/121101776#3.%E6%9B%B4%E6%96%B0kubectl%C2%A0set)

[4.回滚kubectl rollout](https://blog.csdn.net/weixin_57837701/article/details/121101776#4.%E5%9B%9E%E6%BB%9Akubectl%C2%A0rollout)

[5.删除kubectl delete](https://blog.csdn.net/weixin_57837701/article/details/121101776#5.%E5%88%A0%E9%99%A4kubectl%20delete)

[5.金丝雀发布(Canary Release)](https://blog.csdn.net/weixin_57837701/article/details/121101776#5.%E9%87%91%E4%B8%9D%E9%9B%80%E5%8F%91%E5%B8%83%28Canary%20Release%29)

[(1)更新deployment的版本，并配置暂停deployment](https://blog.csdn.net/weixin_57837701/article/details/121101776#%281%29%E6%9B%B4%E6%96%B0deployment%E7%9A%84%E7%89%88%E6%9C%AC%EF%BC%8C%E5%B9%B6%E9%85%8D%E7%BD%AE%E6%9A%82%E5%81%9Cdeployment)

[6.声明式管理方法](https://blog.csdn.net/weixin_57837701/article/details/121101776#6.%E5%A3%B0%E6%98%8E%E5%BC%8F%E7%AE%A1%E7%90%86%E6%96%B9%E6%B3%95)

[1.查看资源配置清单](https://blog.csdn.net/weixin_57837701/article/details/121101776#1.%E6%9F%A5%E7%9C%8B%E8%B5%84%E6%BA%90%E9%85%8D%E7%BD%AE%E6%B8%85%E5%8D%95)

[2.解释资源配置清单](https://blog.csdn.net/weixin_57837701/article/details/121101776#2.%E8%A7%A3%E9%87%8A%E8%B5%84%E6%BA%90%E9%85%8D%E7%BD%AE%E6%B8%85%E5%8D%95)

[3.修改资源配置清单并应用](https://blog.csdn.net/weixin_57837701/article/details/121101776#3.%E4%BF%AE%E6%94%B9%E8%B5%84%E6%BA%90%E9%85%8D%E7%BD%AE%E6%B8%85%E5%8D%95%E5%B9%B6%E5%BA%94%E7%94%A8)

**本次的命令操作基于：**[kubeadm安装的kubernetes](https://blog.csdn.net/weixin_57837701/article/details/121082039)

# 一.kubectl 基本命令操作

## 1.陈述式资源管理方法

> 
> 
> 
> kubernetes集群管理集群资源的唯一入口是通过相应的方法调用apiserver的接口
> 
> kubectl 是官方的CLI命令行工具，用于与apiserver 进行通信，将用户在命令行输入的命令，组织并转化为apiserver能识别的信息，进而实现管理k8s 各种资源的一种有效途径
> 
> kubectl 的命令大全 kubectl --help k8s中文文档: http://docs.kubernetes.org.cn/683.html
> 
> 对资源的增、删、查操作比较方便，但对改的操作就不容易了
> 

### 查看版本信息

```
kubectl version

```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/7ee2e8a3462d4b8ba37b639ffe024b3b.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/7ee2e8a3462d4b8ba37b639ffe024b3b.png)

### 查看资源对象简写

```
kubectl api-resources

```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/3c5679e904804f1c97c72e454440b6d5.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/3c5679e904804f1c97c72e454440b6d5.png)

### 查看集群信息

```
kubectl cluster-info

```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/8b51137466154bffaa286012d54b3e17.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/8b51137466154bffaa286012d54b3e17.png)

### 配置kubectl[自动补全](https://so.csdn.net/so/search?q=%E8%87%AA%E5%8A%A8%E8%A1%A5%E5%85%A8&spm=1001.2101.3001.7020)

```
source <(kubectl completion bash)

```

注意：此时命令补全功能切换环境后是不生效的，如果要使切换环境后也生效需要配置全局环境变量

```
vim /etc/bashrc.....source <(kubectl completion bash)         #在底部添加
```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/443f029a3dd3460dbf5aa0843bb1a039.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/443f029a3dd3460dbf5aa0843bb1a039.png)

### [node](https://so.csdn.net/so/search?q=node&spm=1001.2101.3001.7020) 节点查看日志

```
journalctl -u kubelet -f或者直接查看日志cat /var/log/messages
```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/05171274f8404056a3d9cb7c4b0df60b.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/05171274f8404056a3d9cb7c4b0df60b.png)

## 2.基本信息查看

```
kubectl get <resource> [-o wide | json | yaml] [-n namespace]

```

> 
> 
> 
> 获取资源的相关信息，-n指定命令空间，-o指定输出格式
> 
> resource可以是具体资源名称，如pod nginx -xxx;也可以是资源类型，如pod; 或者all (仅展示几种核心资源，并不完整)
> 
> - -all-namespaces 或-A :表示显示所有命令空间，
> - -show-labels :显示所有标签
> - l app:仅显示标签为app的资源
> - l app=nginx :仅显示包含app标签， 且值为nginx的资源

### 查看master 节点状态

```
kubectl get componentstatuseskubectl get cs
```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/ba3004494b7445578076c5e792cb1275.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/ba3004494b7445578076c5e792cb1275.png)

### 查看命令空间

> 
> 
> 
> 命令空间的作用:用于允许不同 命令空间的相同类型的资源重名
> 

```
kubectl get name spacekubectl get ns
```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/37cab888f8c548b29d743f40e05c847b.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/37cab888f8c548b29d743f40e05c847b.png)

### 查看default命名空间的所有资源

```
kubectl get all [-n default]

```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/73fe1d3a22cf49b6b857fd49fe65d034.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/73fe1d3a22cf49b6b857fd49fe65d034.png)

### 创建命名空间 (app)

```
kubectl create ns appkubectl get ns
```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/12c4215f45014270a7d0a79211918cfe.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/12c4215f45014270a7d0a79211918cfe.png)

### 删除命名空间(app)

```
kubectl delete namespace appkubectl get ns
```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/093ce1c4e55a4c68be43398c43723c70.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/093ce1c4e55a4c68be43398c43723c70.png)

### 在命名空间创建副本控制器启动Pod

例：在命名空间kube-public 创建副本控制器( deployment) 来启动Pod (nginx-w1)

```
kubectl create deployment nginx-wl --image=nginx -n kube-public

```

描述某个资源的详细信息

```
kubectl describe deployment nginx-cc -n kube-publickubectl describe pod nginx-cc-5d7d5c6b54 -n kube-public
```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/d4751affac2147c69bf0ad970811c322.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/d4751affac2147c69bf0ad970811c322.png)

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/e26677fa142048fa81795fe17e005c99.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/e26677fa142048fa81795fe17e005c99.png)

### 查看命名空间kube-public中的pod信息

```
kubectl get pods -n kube-public

```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/e1f287487552471ea99690d0ee75d15c.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/e1f287487552471ea99690d0ee75d15c.png)

### kubectl exec

kubectl exec可以跨主机登录容器，docker exec 只能在容器所在主机上登录

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/5fdce4b2e1c94a69955008dc88e4d494.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/5fdce4b2e1c94a69955008dc88e4d494.png)

### 重启（删除）pod资源

由于存在deployment/rc之类的副本控制器，删除pod也会重新拉起来

```
kubectl delete pod nginx-cc-5d7d5c6b54-ld8qt -n kube-public

```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/32c536675e464750b4dda9ef1396a205.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/32c536675e464750b4dda9ef1396a205.png)

若pod无法删除，总是处于terminate状态， 则要强行删除pod

```
kubectl delete pod <pod-name> -n <namespace> --force --grace-period=0#grace-period表示过渡存活期，默认30s，在删除pod之前允许POD慢慢终止其上的容器进程，从而优雅退出，0表示立即终止pod
```

### 扩容缩容

```
kubectl scale deployment nginx-cc --replicas=2 -n kube-public  #扩容kubectl scale deployment nginx-cc --replicas=1 -n kube-public  #缩容
```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/fb151ff36d5b4d13b814a1fb81e271c5.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/fb151ff36d5b4d13b814a1fb81e271c5.png)

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/08849c3702c146018b06df2469c8647d.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/08849c3702c146018b06df2469c8647d.png)

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/07542865ae724ee89f66e2a3ae17ad19.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/07542865ae724ee89f66e2a3ae17ad19.png)

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/09cc453b45254992bb6e4675a1a39749.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/09cc453b45254992bb6e4675a1a39749.png)

### 删除副本控制器

```
kubectl delete deployment nginx-cc -n kube-publickubectl delete deployment/nginx-cc -n kube-public
```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/812dd3e9cd37428f9de1f3e2cf6f60fd.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/812dd3e9cd37428f9de1f3e2cf6f60fd.png)

# 二.项目的生命周期

> 
> 
> 
> 创建–>发布–>更新–>回滚–>删除
> 

## 1.创建kubectl run命令

●创建并运行一个或多个容器镜像
 ●创建一个deployment或job来管理容器

```
kubectl run --help

```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/8d58ac6fe4a44c6e99fc9dab85a98e0a.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/8d58ac6fe4a44c6e99fc9dab85a98e0a.png)

启动nginx 实例，暴露容器端口80，设置副本数3

```
kubectl run nginx --image=nginx:1.14 --port=80 --replicas=3kubectl get podskubectl get all
```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/34e917b1252e43d6bb8313a694a7354a.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/34e917b1252e43d6bb8313a694a7354a.png)

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/99f75171cbb34745b15e7badc94f5b06.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/99f75171cbb34745b15e7badc94f5b06.png)

## 2.发布kubectl expose命令

将资源暴露为新的Service

```
kubectl expose --help

```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/2e86effa747947c3a8f771dbc8463259.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/2e86effa747947c3a8f771dbc8463259.png)

为deployment的nginx创建service， 并通过Service的80端口转发至容器的80端口上，Service的名称为nginx-service， 类型为NodePort

```
kubectl expose deployment nginx --port=80 --target-port=80 --name=nginx-service --type=NodePortKubernetes之所以需要Service， 一方面是因为Pod的IP 不是固定的(Pod可能会重建)，另一-方面则是因为- -组Pod实例之间总会有负载均衡的需求。Service通过label Selector实现的对一组的Pod的访问。对于容器应用而言，Kubernetes 提供了基于VIP (虚拟IP)的网桥的方式访问 Service， 再由Service 重定向到相应的Pod。service的类型:●ClusterIP:提供一个集群内部的虚拟IP以供Pod访问( service默认类型)●NodePort:在每个Node.上打开一个端口以供外部访问，Kubernetes将会在每个Node.上打开一个端口并且每个Node的端口都是一样的，通过NodeIp:NodePort的方式Kubernetes集群外部的程序可以访问Service。注:每个端口只能是一种服务，端口范围只能是30000-32767●LoadBalancer:通过外部的负载均衡器来访问，通常在云平台部署LoadBalancer还需要额外的费用。
```

查看pod网络状态详细信息和Service暴露的端口

```
kubectl get pods,svc -o wide

```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/bfc28c768e944bbfa1db8d493da6ee70.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/bfc28c768e944bbfa1db8d493da6ee70.png)

查看关联后端的节点

```
kubectl get endpoints

```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/eb7ecc097ea84191a5410769547c84b0.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/eb7ecc097ea84191a5410769547c84b0.png)

查看service 的描述信息

```
kubect1 describe svc nginx

```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/e8ae8e1d2bd74bc588c514b70722741b.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/e8ae8e1d2bd74bc588c514b70722741b.png)

在node01 节点上操作，查看负载均衡端口

```
yum install ipvsadm -y
```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/645e921eb06440cd988e6c138b6b425b.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/645e921eb06440cd988e6c138b6b425b.png)

```
curl 10.96.203.199curl 192.168.111.173:32238
```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/32ba90be7e554eb8a6417a4ebba598e4.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/32ba90be7e554eb8a6417a4ebba598e4.png)

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/9961bd0c3aec4ee595c4df6d350e4ba2.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/9961bd0c3aec4ee595c4df6d350e4ba2.png)

在master01操作 查看访问日志

```
kubectl logs nginx-65fc77987d-wh9fxkubectl logs nginx-65fc77987d-x7knxkubectl logs nginx-65fc77987d-zmgq2
```

## 3.更新kubectl set

更改现有应用资源一些信息

```
kubectl set --help

```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/7cc50eea227749e7a41e32f515b907c5.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/7cc50eea227749e7a41e32f515b907c5.png)

获取修改模板

```
kubectl set image --help

```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/02bbdaabe14b48e9b34d7c11fe291993.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/02bbdaabe14b48e9b34d7c11fe291993.png)

查看当前nginx 的版本号

```
curl -I http://192.168.111.171:32238curl -I http://192.168.111.173:32238
```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/ae69c2e02cff4bab8cf9b627bcabcdff.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/ae69c2e02cff4bab8cf9b627bcabcdff.png)

将nginx 版本更新为1.15版本

```
kubectl set image deployment/nginx nginx=nginx:1.15

```

处于动态监听pod状态，由于使用的是滚动更新方式，所以会先生成--个新的pod，然后删除--个旧的pod，往后依次类推（动态更新的）

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/baf8050506ec4eee9095f223c7a17617.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/baf8050506ec4eee9095f223c7a17617.png)

再看更新好后的Pod的ip会改变

```
kubectl get pods -o wide

```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/92bc5d6f3b044253bfce2427cf62eb47.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/92bc5d6f3b044253bfce2427cf62eb47.png)

再看nginx 的版本号

```
curl -I http://192.168.111.173:32238curl -I http://192.168.111.175:32238
```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/4b4d9945ab7c40339346af488b6b4a78.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/4b4d9945ab7c40339346af488b6b4a78.png)

## 4.回滚kubectl rollout

对资源进行回滚管理

```
kubectl rollout --help

```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/52b0836203fa4aec9e24fc7d8026e072.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/52b0836203fa4aec9e24fc7d8026e072.png)

查看历史版本

```
kubectl rollout history deployment/nginx

```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/763df1b9879347eca654f64708ef4a79.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/763df1b9879347eca654f64708ef4a79.png)

执行回滚到上一个版本

```
kubectl rollout undo deployment/nginx

```

执行回滚到指定版本

```
kubectl rollout undo deployment/nginx --to-revision=2

```

检查回滚状态

```
kubectl rollout status deployment/nginx

```

## 5.删除kubectl delete

删除副本控制器

```
kubectl delete deployment/nginx

```

删除service

```
kubectl delete svc/nginx-servicekubectl get all
```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/f5ccf778f176486298c8b829e678be97.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/f5ccf778f176486298c8b829e678be97.png)

## 5.金丝雀发布(Canary Release)

Deployment控制器支持自定义控制更新过程中的滚动节奏，如“暂停(pause)”或“继续(resume)”更新操作。比如等待第一批新的Pod资源创

建完成后立即暂停更新过程，此时，仅存在一部分新版本的应用，主体部分还是旧的版本。然后，再筛选一小部分的用户请求路由到新版本的Pod应用，继续观察能否稳定地按期望的方式运行。确定没问题之后再继续完成余下的Pod资源滚动更新，否则立即回滚更新操作。这就是所谓的金丝雀发布。

### (1)更新deployment的版本，并配置暂停deployment

```
kubectl set image deployment/nginx nginx=nginx:1.14 && kubectl rollout pause deployment/nginx

```

(2)监控更新的过程，可以看到已经新增了一个资源，但是并未按照预期的状态去删除一个旧的资源， 就是因为使用了pause暂停命令

```
kubectl get pods -w

```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/8038271ba3a0438e8cf201df78626750.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/8038271ba3a0438e8cf201df78626750.png)

## 6.声明式管理方法

> 
> 
> 
> 1.适合于对资源的修改操作
> 
> 2.声明式资源管理方法依赖于资源配置清单文件对资源进行管理资源配置清单文件有两种格式: yaml (人性化，易读)，json (易于api接口解析)
> 
> 3.对资源的管理，是通过事先定义在统–资源配置清单内，再通过陈述式命令应用到k8s集群里
> 
> 4.语法格式: kubectl create/app1y/delete -f xxxx.yaml
> 

### 1.查看资源配置清单

```
kubectl get deployment nginx -o yaml

```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/2e1efe127d05414ea0f093d8d66c1749.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/2e1efe127d05414ea0f093d8d66c1749.png)

### 2.解释资源配置清单

```
kubectl explain deployment.metadatakubectl get service nginx -o yamlkubectl explain service.metadata
```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/2a7c40161fdc44ce8a52f518763a8ba7.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/2a7c40161fdc44ce8a52f518763a8ba7.png)

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/443de9a5c4f2496b87664eb0e0385000.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/443de9a5c4f2496b87664eb0e0385000.png)

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/27d5a8118a464051a3bc93e07bee052c.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/27d5a8118a464051a3bc93e07bee052c.png)

### 3.修改资源配置清单并应用

离线修改:

> 
> 
> 
> 修改yaml文件，并用kubectl apply -f xxxx.yaml文件使之生效注意:当apply不生效时， 先使用delete清除资源，再apply创建资源
> 

```
kubectl get service nginx -o yaml > nginx-svc.yamlvim nginx-svc.yaml#修改port: 8080kubectl delete -f nginx-svc.yamlkubectl apply -f nginx-svc.yamlkubectl get svc
```

![(212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/6fc57abcf55c45049ab4aa7e44f5cf3b.png]((212%E6%9D%A1%E6%B6%88%E6%81%AF)%20%E3%80%90%E8%AE%B0%E5%BD%95%E3%80%91k8s-kubectl%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%88%E5%8C%85%E5%90%AB%E6%89%B9%E9%87%8F%E9%87%8D%E5%90%AF%EF%BC%89_kubectl%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1%E5%91%BD%E4%BB%A4%2092dd0de521ac47559eda0bb75fe35c6a/6fc57abcf55c45049ab4aa7e44f5cf3b.png)

在线修改:

> 
> 
> 
> 直接使用kubectl edit service nginx在线编辑资源配置清单并保存退出即时生效(如port:888)PS:此修改方式不会对yaml文件内容修改
> 

删除资源配置清单: