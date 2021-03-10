import requests

base_url='http://49.233.108.117:3000/api/v1'

def test_topic_index_page():
    query_parmas = {
        "page":1,
        "tab":"ask",
        "limit":1,
        "mdrender":"false"
    }
    r= requests.get(base_url+"/topics",params=query_parmas)
    assert r.status_code == 200
    assert r.json()['success'] == True


test_topic_index_page()
