import requests
import json

def search_by_id():
    response=request.get("https://api.sampleapis.com/coffee/hot")
    prinyt(json.dumps(responce.json(),indent=4))