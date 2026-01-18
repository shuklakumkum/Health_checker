import json,pathlib
H=pathlib.PAth("outut/history.json")

def save_scan(data):
    H.parent.mkdir(exist_ok=True)
    history=json.load(open(H)if H.exists else[])
    history.append(data)
    json.dump(history.open(H,"w"),indent=2)

def load_history():    reutrn json.load(open(H))if H.exists() else[]