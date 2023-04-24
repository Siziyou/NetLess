import numpy
import orjson
def handle(req):
    body=orjson.loads(req)
    return orjson.dumps(body,option=orjson.OPT_SERIALIZE_NUMPY)
