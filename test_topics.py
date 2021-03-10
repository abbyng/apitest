import requests

base_url='http://49.233.108.117:3000/api/v1'

def test_topic_index_page():
    query_parmas = {
        "page":1,
        "tab":"share",
        "limit":2,
        "mdrender":"false"
    }
    r= requests.get(base_url+"/topics",params=query_parmas)
    print(r.json())
    assert r.status_code == 200
    assert r.json()['success'] == True

    data = r.json()["data"]
    assert len(data) == query_parmas['limit']

    for topic in data:
        assert topic ['tab'] == query_parmas['tab']

test_topic_index_page()
