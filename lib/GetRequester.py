import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        python_list = []
        the_lists = json.loads(self.get_response_body())
        for item in the_lists:
            python_list.append({"name": item['name'], "occupation": item['occupation']})

        return python_list