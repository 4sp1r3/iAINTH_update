import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "13"
              }
            },
            {
              "wildcard": {
                "registry_key_path.keyword": "*\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Debug*"
              }
            }
          ]
        }
      }
    }
  }
}



res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Defense Evasion"
technique = "Obfuscated Files or Information"
procedure = "Execute base64-encoded PowerShell from Windows Registry"
tech_code = "T1027"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 76)

json_str = json.dumps(doc)
with open("dst_procedures/Execute base64-encoded PowerShell from Windows Registry.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Defense Evasion"\n')
	f.write('technique = "Obfuscated Files or Information"\n')
	f.write('procedure = "Execute base64-encoded PowerShell from Windows Registry"\n')
	f.write('tech_code = "T1027"\n')
