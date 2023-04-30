import requests
import onnxruntime
import json
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    header={"X-Callback-Url":req}
    
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/async-function/fun1',data={"data":"test_post","callback":req},headers=header)
    x = requests.post('http://gateway.openfaas.svc.cluster.local:8080/async-function/fun1',data=json.dumps({"data":"test_post_json","callback":req}),headers=header)
    return {"req":req,"x.status_code":x.status_code,"x.reason":x.reason,"x.apparent_encoding":x.apparent_encoding}
