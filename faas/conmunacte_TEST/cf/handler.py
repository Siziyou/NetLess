import numpy
import orjson
def handle(req):
    body=orjson.loads(req)
    numpy.array(body['d'])
    return orjson.dumps(body,option=orjson.OPT_SERIALIZE_NUMPY)
