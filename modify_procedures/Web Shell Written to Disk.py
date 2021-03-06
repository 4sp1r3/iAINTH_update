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
                "event_id": "11"
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "bool": {
                      "must": [
                        {
                          "wildcard": {
                            "file_name.keyword": "*\\\\inetpub\\\\wwwroot\\\\*"
                          }
                        },
                        {
                          "bool": {
                            "should": [
                              {
                                "wildcard": {
                                  "file_name.keyword": "*.asp*"
                                }
                              },
                              {
                                "wildcard": {
                                  "file_name.keyword": "*.ashx*"
                                }
                              },
                              {
                                "wildcard": {
                                  "file_name.keyword": "*.ph*"
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
                      "must": [
                        {
                          "bool": {
                            "should": [
                              {
                                "wildcard": {
                                  "file_name.keyword": "*\\\\www\\\\*"
                                }
                              },
                              {
                                "wildcard": {
                                  "file_name.keyword": "*\\\\htdocs\\\\*"
                                }
                              },
                              {
                                "wildcard": {
                                  "file_name.keyword": "*\\\\html\\\\*"
                                }
                              }
                            ]
                          }
                        },
                        {
                          "wildcard": {
                            "file_name.keyword": "*.ph*"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "bool": {
                      "must": [
                        {
                          "wildcard": {
                            "file_name.keyword": "*\\\\*"
                          }
                        },
                        {
                          "wildcard": {
                            "file_name.keyword": "*.jsp*"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "bool": {
                      "must": [
                        {
                          "wildcard": {
                            "file_name.keyword": "*\\\\cgi-bin\\\\*"
                          }
                        },
                        {
                          "wildcard": {
                            "file_name.keyword": "*.pl*"
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
technique = "Web Shell"
procedure = "Web Shell Written to Disk"
tech_code = "T1100"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 113)

json_str = json.dumps(doc)
with open("dst_procedures/Web Shell Written to Disk.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Persistence"\n')
	f.write('technique = "Web Shell"\n')
	f.write('procedure = "Web Shell Written to Disk"\n')
	f.write('tech_code = "T1100"\n')
