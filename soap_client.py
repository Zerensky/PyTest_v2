# библиотека для работы с SOAP AP

import zeep

class SoapClient:
    def __init__(self, wsdl_url):
        self.client = zeep.Client(wsdl=wsdl_url)

    def check_text(self, text):
        response = self.client.service.checkText(text)
        return response
