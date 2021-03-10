import requests
import business.common as common

def create_topic(topicdata):

# topic_data = {
#     "accesstoken": 'e983ec8e-fc0b-4be2-845c-508452c4ad9a',
#     "title": "Happy Python life",
#     "tab": "ask",
#     "content":"I am using Python to do api testing!"
# }

    url = 'http://49.233.108.117:3000/api/v1/topics'

    r = requests.post(url=url, json=topicdata)
    return r
