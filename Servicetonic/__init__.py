import requests
import json
class api:
    credentials = ""
    token = "" 
    def __init__ (self):
        self.credentials = self.read_credentials()
        self.token = self.login()
        print(self.token.text)



    def read_credentials(self):
        with open('./Servicetonic/credentials.json') as f:
            credentials = json.load(f)
        
        return credentials

    def login(self):
        url =  "https://enecworldiberica.myservicetonic.com/ServiceTonic/strest/v1/auth"
        auth = {
            "idProject" : self.credentials['proyecto'], 
            "username" : self.credentials['username'], 
            "password" : self.credentials['password']
        }
        
        req = requests.post(url, data=json.dumps(auth), headers = {'Content-Type': 'application/json'})

        return req