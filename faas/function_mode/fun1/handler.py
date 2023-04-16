import json
def handle(req):
    data={"1":1,"req":json.loads(req)["data"]}
    return json.dumps(data)
