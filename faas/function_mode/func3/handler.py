import requests
import torch
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    header={"X-Callback-Url":req}
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/async-function/fun1',data="test_post",headers=header)
    print()
    return req+str(x.status_code)+" "+str(x.reason)+" "+str(x.apparent_encoding)
