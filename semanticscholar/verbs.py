import requests


API_BASE = 'http://api.semanticscholar.org/v1'


class BaseVerb:

    def endpoint(self):
        raise NotImplementedError


class Gettable(BaseVerb):

    def can_get(self):
        return False

    def get(self):
        if self.can_get():
            endpoint = API_BASE + self.endpoint()
            res = requests.get(endpoint).json()
            self.populate(**res)
