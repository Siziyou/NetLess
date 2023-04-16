curl -sLS https://get.arkade.dev | sudo sh
arkade get faas-cli
arkade install mongodb
arkade install openfaas
echo export MONGODB_ROOT_PASSWORD=$(kubectl get secret --namespace default mongodb -o jsonpath="{.data.mongodb-root-password}" | base64 --decode) >> ~/.bashrc
faas-cli secret create mongo-db-password --from-literal $MONGODB_ROOT_PASSWORD