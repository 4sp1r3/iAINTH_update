{"query": {"constant_score": {"filter": {"bool": {"must": [{"bool": {"must": [{"match_phrase": {"event_id": "4624"}}, {"bool": {"should": [{"bool": {"must": [{"match_phrase": {"user_reporter_sid": "S-1-0-0"}}, {"match_phrase": {"logon_type": "3"}}, {"match_phrase": {"logon_process_name": "ntlmssp"}}, {"match_phrase": {"logon_key_length": "0"}}]}}, {"bool": {"must": [{"match_phrase": {"logon_type": "9"}}, {"match_phrase": {"logon_process_name": "seclogo"}}]}}]}}]}}, {"bool": {"must_not": [{"bool": {"must": [{"match_phrase": {"user_name": "ANONYMOUS LOGON"}}]}}]}}]}}}}}
tactic = "Lateral Movement"
technique = "Pass the Hash"
procedure = "Pass the Hash Activity 2"
tech_code = "T1175"
