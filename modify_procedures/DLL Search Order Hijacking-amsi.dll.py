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
              "bool": {
                "must": [
                  {
                    "match_phrase": {
                      "event_id": "7"
                    }
                  },
                  {
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "process_path.keyword": "*\\\\svchost.exe"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "bool": {
                      "should": [
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\tsmsisrv.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\tsvipsrv.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\wlbsctrl.dll"
                          }
                        },
                        {
                          "wildcard": {
                            "module_loaded.keyword": "*\\\\amsi.dll"
                          }
                        }
                      ]
                    }
                  }
                ]
              }
            },
            {
              "bool": {
                "must_not": [
                  {
                    "bool": {
                      "must": [
                        {
                          "match_phrase": {
                            "event_id": "7"
                          }
                        },
                        {
                          "bool": {
                            "should": [
                              {
                                "wildcard": {
                                  "process_path.keyword": "*\\\\svchost.exe"
                                }
                              }
                            ]
                          }
                        },
                        {
                          "bool": {
                            "should": [
                              {
                                "match_phrase": {
                                  "module_loaded": "C:\\Windows\\WinSxS\\*"
                                }
                              }
                            ]
                          }
                        }
                      ]
                    }
                  }
                ]
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
tactic = "Persistence"
technique = "DLL Search Order Hijacking"
procedure = "DLL Search Order Hijacking-amsi.dll"
tech_code = "T1038"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 69)

json_str = json.dumps(doc)
with open("dst_procedures/DLL Search Order Hijacking-amsi.dll.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Persistence"\n')
	f.write('technique = "DLL Search Order Hijacking"\n')
	f.write('procedure = "DLL Search Order Hijacking-amsi.dll"\n')
	f.write('tech_code = "T1038"\n')
