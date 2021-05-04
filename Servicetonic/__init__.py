import requests
from requests_toolbelt import MultipartEncoder
import json
import pprint
class api:
    credentials = ""
    token = "" 
    def __init__ (self):
        self.credentials = self.read_credentials()
        self.token = self.login()
        print(self.token)



    def read_credentials(self):
        with open('./Servicetonic/credentials.json') as f:
            credentials = json.load(f)

        print(credentials)
        return credentials

    def login(self):
        url =  "http://enecworldiberica.myservicetonic.com/ServiceTonic/strest/v1/auth"
        auth = {
            "idProject" : self.credentials['proyecto'], 
            "username" : self.credentials['username'], 
            "password" : self.credentials['password']
        }
        
        req = requests.post(url, data=json.dumps(auth), headers = {'Content-Type': 'application/json'})

        return req.text

    def new_client(self, client):

        f = open("./data/client.csv", "a")
        url = "http://enecworldiberica.myservicetonic.com/ServiceTonic/strest/v1/services/"+self.credentials['proyecto']+"/cis"    
        datos = {
            "fieldList":[
                {
                "fieldName":"TITLE",
                "textValue":client[1]
                },
                {
                "fieldName":"STATUS",
                "textValue":"active"
                },
                {
                "fieldName":"SERIAL_NUMBER",
                "textValue":client[2]
                },
                {
                "fieldName":"CI_TYPE",
                "textValue":"Empresa"
                }
            ]
            
            }
        params = {'rsConfigurationItem': json.dumps(datos)}
        #params = { 'rsConfigurationItem': 'hola' }
        print(params)
        m = MultipartEncoder(params)
        req = requests.post(url, data = m , headers = {"Authorization":self.token, "Content-Type":m.content_type} )
        f.write(client[2]+";"+req.text)
        print(req.text)