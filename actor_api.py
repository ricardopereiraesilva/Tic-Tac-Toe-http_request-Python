import boardImage
import json
import requests

class ActorAPI:
    def __init__(self):
        self.state = boardImage.BoardImage()

    def getState(self):
        return self.state

    def click(self, a_line, a_column):
        #    https://docs.python-requests.org/en/latest/user/quickstart/
        resp = requests.post('https://api-jv.herokuapp.com/12345/', data={'line': a_line, 'column': a_column})
        resp_json = resp.text
        resp_dict = json.loads(resp_json)    #    https://www.w3schools.com/python/python_json.asp
        message = resp_dict['0'][0]
        map = resp_dict['1'][0]
        self.state.setMessage(message)
        self.state.setMap(map)
