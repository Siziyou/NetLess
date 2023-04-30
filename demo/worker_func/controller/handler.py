import controller
def handle(req):
    new_instance=controller()
    return new_instance.predict(req)

