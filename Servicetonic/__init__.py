import requests
import json
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

    def new_client(self):
        url = "http://enecworldiberica.myservicetonic.com/ServiceTonic/strest/v1/services/"+self.credentials['proyecto']+"/cis"
        datos = {
            "fieldList":[
                {
                "fieldName":"TITLE",
                "textValue":"Martin_Sanchez"
                },
                {
                "fieldName":"STATUS",
                "textValue":"active"
                },
                {
                "fieldName":"SERIAL_NUMBER",
                "textValue":"78261438M"
                },
                {
                "fieldName":"CI_TYPE",
                "textValue":"Empresa"
                }
            ]
            
            }

        print(json.dumps(datos))

        params = {'rsConfigurationItem': json.dumps(datos)}

        print(params)
        req = requests.post(url, data = params, headers = {"Authorization":self.token, "Content-Type":"multipart/form-data"} )

        print(req.text)