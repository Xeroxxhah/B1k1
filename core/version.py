
import requests
import json

class Version():

    def __init__(self):

        self.currentVersion = 'v0.2.1'
        try:
            self.updatedVersion = str(requests.get('https://api.github.com/repos/Xeroxxhah/B1k1/releases/latest').json().get('body'))
        except:
            self.updatedVersion = None
            print('An Error Ocurred: Could not check latest version.')
    

    def IsUpdated(self):
        if self.currentVersion == self.updatedVersion:
            return True
        return False
