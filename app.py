from flask import Flask
import json
from time import sleep
import threading
import requests

url = "testapp-service.argocdtest.svc.cluster.local:5000"


app = Flask(__name__)

@app.route('/testapp')
def test():
    x = threading.Thread(target=thread_function)
    x.start()
    response = requests.get(url)
    return response
    #x.join()
   # response = {"foo:bar", "hello:test"}
#    return """
#    {
#        'test':'foo',
#        'foo':'bar',
#        'name':'jenny'
#    }
#    """

def thread_function():
    sleep(10)
