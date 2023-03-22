# Asynchronous Function With OpenFaas - Ruan Bekker's Blog

[https://blog.ruanbekker.com/blog/2020/02/17/python-asynchronous-function-with-openfaas/](https://blog.ruanbekker.com/blog/2020/02/17/python-asynchronous-function-with-openfaas/)

In this post we will explore how to use asynchronous functions in OpenFaas.

## What are we doing

A synchronous request blocks the client until operation completes, where a asynchronous request doesn’t block the client, which is nice to use for long-running tasks or function invocations to run in the background through the use of NATS Streaming.

We will be building a Python Flask API Server which will act as our webhook service. When we invoke our function by making a http request, we also include a callback url as a header which will be the address where the queue worker will post it’s results.

Then we will make a http request to the synchronous function where we will get the response from the function and a http request to the asynchronous function, where we will get the response from the webhook service’s logs

## Deploy OpenFaas

Deploy OpenFaas on a k3d Kubernetes Cluster if you want to follow along on your laptop. You can follow this post to deploy a kubernetes cluster and deploying openfaas:

- [https://blog.ruanbekker.com/blog/2020/02/17/traefik-ingress-for-openfaas-on-kubernetes-k3d/](https://blog.ruanbekker.com/blog/2020/02/17/traefik-ingress-for-openfaas-on-kubernetes-k3d/)

## Webhook Service

Lets build the Python Flask Webhook Service, our application code:

Our `Dockerfile`:

Building and Pushing to Docker Hub (or you can use my docker image):

Create the deployment manifest `webhook.yml` for our webhook service:

Now deploy to kubernetes:

After a minute or so, verify that you get a response when making a http request:

## Deploy the OpenFaas Function

We will deploy a dockerfile type function which will return the data that we feed it:

List the functions:

Describe the function:

## Testing

Test synchronous function:

Test asynchronous function, remember, here we need to provide the callback url which the queue worker will inform, which will be our webhook service:

Check the logs of the webhook pod:

Check the logs of the queue worker:

Make 1000 Requests:

View the log file that we wrote before we started and finished our requests:

The last request was actioned at:

## Thank You

This was a basic example to demonstrate async functions using OpenFaas

## OpenFaas Documentation:

- [https://docs.openfaas.com](https://docs.openfaas.com/)
- [https://docs.openfaas.com/reference/async/](https://docs.openfaas.com/reference/async/)
