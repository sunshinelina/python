import json
import requests

json_str = '{"act":"v3/datasource/get","args":{"auth":"BwsI1eeC1s9nk1kwmJcrKkjNjt9RfwJBLKfSLYKMAHga7Hxrxt0WFau/28H4P4ZfXB+/5RaLbsrlslgwjVlPSOJqeynQoefE","corp_id":"5ba4c10400c0f229dec6f1d1","_id":"5bcd968100c0f232f04fcc4a"}}'
payload = json.loads(json_str)
r = requests.post("http://rebuild.dev.datahunter.cn/rpc", json=payload)
if r.status_code != 200:
    print("服务器异常")
else:
    try:
        result = r.json()
        code = result["code"]
        if code == 200:
            print(result["msg"])
    except:
        print("json decode fail.")