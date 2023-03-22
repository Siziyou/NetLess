# faasflow/faas-flow-example: Example flows cooked with faas-flow

[https://github.com/faasflow/faas-flow-example](https://github.com/faasflow/faas-flow-example)

# faas-flow examples

Super simple examples of faas-flow

## Dags

> 
> 
> 
> Sync Chain
> 
> ![faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/sync-chain-dag.png](faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/sync-chain-dag.png)
> 
> ![faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/async-chain-dag.png](faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/async-chain-dag.png)
> 
> ![faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/parallel-branch-dag.png](faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/parallel-branch-dag.png)
> 
> ![faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/dynamic-branch-dag.png](faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/dynamic-branch-dag.png)
> 
> ![faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/conditional-branch-dag.png](faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/conditional-branch-dag.png)
> 

## Getting Started

1. Deploy Openfaas
2. Deploy Faasflow Infra ([https://github.com/faasflow/faas-flow-infra#deploy-in-kubernetes](https://github.com/faasflow/faas-flow-infra#deploy-in-kubernetes))
3. Review your configuration at `flow.yml`

```
environment:
 gateway: "gateway.openfaas:8080"
 enable_tracing: true
 trace_server: "jaeger-agent.faasflow:5775"
 enable_hmac: false
 consul_url: "consul.faasflow:8500"
 consul_dc: "dc1"
 s3_url: "minio.faasflow:9000"
 s3_tls: false
```

1. Deploy the flow-functions

```
faas deploy
```

1. Request the flows

```
curl -v http://127.0.0.1:8080/function/sync-chain
curl -v http://127.0.0.1:8080/function/async-chain
curl -v http://127.0.0.1:8080/function/parallel-branching
curl -v http://127.0.0.1:8080/function/dynamic-branching
curl -v http://127.0.0.1:8080/function/conditional-branching
```

1. Check the logs of storage function

## Tracing Information in faas-flow-tower

> 
> 
> 
> Sync Chain
> 
> ![faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/sync-chain-tracing.png](faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/sync-chain-tracing.png)
> 
> ![faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/async-chain-tracing.png](faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/async-chain-tracing.png)
> 
> ![faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/parallel-branch-tracing.png](faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/parallel-branch-tracing.png)
> 
> ![faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/dynamic-branch-tracing.png](faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/dynamic-branch-tracing.png)
> 
> ![faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/conditional-branch-tracing.png](faasflow%20faas-flow-example%20Example%20flows%20cooked%20wi%209378b027d9e14c68bff457f580bed08b/conditional-branch-tracing.png)
>