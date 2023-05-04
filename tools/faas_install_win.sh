#Download openfaas
git clone https://github.com/openfaas/faas-netes
cd faas-netes
#Please check kubectl is available
kubectl apply -f ./namespaces.yml
#Create auth
kubectl -n openfaas create secret generic basic-auth \
--from-literal=basic-auth-user=admin \
--from-literal=basic-auth-password=admin
#Install all components
kubectl apply -f ./yaml/
