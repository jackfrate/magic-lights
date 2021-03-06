from src.magic_controller import LightLister
from flask import Flask, request
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)
lc = LightLister()


@app.route('/ip_list')
def ip_list():
    return json.dumps(lc.get_ip_list())


@app.route('/index_list')
def index_list():
    return json.dumps(lc.get_light_indicies())


@app.route('/light_status/<idx>')
def light_status(idx):
    return json.dumps(lc.get_light_status(int(idx)))


@app.route('/light_color', methods=['POST'])
def change_color():
    data = request.json
    index = data["index"]
    r = data["r"]
    g = data["g"]
    b = data["b"]
    lc.change_color(r, g, b, index)
    return json.dumps({"message": f'successfully changed light {index} color'})


@app.route('/light_bright', methods=['POST'])
def change_bright():
    data = request.json
    index = data['index']
    bright = data['bright']
    lc.change_brightness(bright, index)
    return json.dumps({"message": f'successfully changed light {index} brightness'})


@app.route('/light_refresh')
def refresh_lights():
    lc.refresh_list()
    return json.dumps({"message": "list refreshed"})
