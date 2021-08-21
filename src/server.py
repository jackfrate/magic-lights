from src.magic_controller import LightLister
from flask import Flask
import json

app = Flask(__name__)

lc = LightLister()


@app.route('/ip_list')
def ip_list():
    return json.dumps({
        "ipList": lc.get_ip_list()
    })
