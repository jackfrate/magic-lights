from src.magic_controller import LightLister
from flask import Flask, request
import json

app = Flask(__name__)

lc = LightLister()
lc.refresh_list()


@app.route('/ip_list')
def ip_list():
    return json.dumps({
        "ipList": lc.get_ip_list()
    })

@app.route('/index_list')
def index_list():
    return json.dumps({
        "indexList": lc.get_light_indicies()
    })

@app.route('/light')
def change_color():
    data = request.json
    index = data["index"]
    r = data["r"]
    g = data["g"] 
    b = data["b"]
    lc.change_color(r, g, b, index)
    return json.dumps({
        "message": f'successfully changed light {index} color'
    })
