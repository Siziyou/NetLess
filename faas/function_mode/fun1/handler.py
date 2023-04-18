import numpy
import json
def handle(req):
    data=json.loads(req)["data"]
    data=numpy.array(data)
    return json.dumps({"s":1,"d":data.tolist()})
