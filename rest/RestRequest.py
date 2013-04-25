import urllib
import urllib2
import json
#from GetRequest import GetRequest


class RestRequest:
    def __init__(self, api_key, payer_name, payer_id,  service_provider_first_name, service_provider_last_name, service_provider_npi,  subscriber_id, subscriber_first_name,  subscriber_last_name, subscriber_dob):
        
        self.api_key = api_key
	self.payer_name = payer_name
	self.payer_id = payer_id
	self.service_provider_npi = service_provider_npi
	self.subscriber_id = subscriber_id
	self.subscriber_first_name = subscriber_first_name
	self.subscriber_last_name = subscriber_last_name
	self.subscriber_dob = subscriber_dob
	self.service_provider_first_name = service_provider_first_name
	self.service_provider_last_name = service_provider_last_name
    
    def get_api_key(self):
        return self.api_key
    
    def set_api_key(self,api_key):
        self.api_key = api_key
    
    def get_payer_name(self):
        return self.payer_name
    
    def set_payer_name(self, payer_name):
        self.payer_name = payer_name
   
    def get_payer_id(self):
        return self.payer_id
   
    def set_payer_id(self, payer_id):
        self.payer_id = payer_id
   
    def get_service_provider_first_name(self):
        return self.service_provider_first_name
   
    def set_service_provider_first_name(self,service_provider_first_name):
        self.service_provider_first_name = service_provider_first_name
   
    def get_service_provider_last_name(self):
        return self.service_provider_last_name
   
    def set_service_provider_last_name(self,service_provider_last_name):
        self.service_provider_last_name = service_provider_last_name
   
    def get_service_provider_npi(self):
        return self.service_provider_npi
   
    def set_service_provider_npi(self,service_provider_npi): 
        self.service_provider_npi = service_provider_npi
   
    def get_subscriber_id(self):
        return self.subscriber_id
   
    def set_subscriber_id(self,subscriber_id): 
        self.subscriber_id = subscriber_id
   
    def get_subscriber_first_name(self):
        return self.subscriber_first_name
   
    def set_subscriber_first_name(self,subscriber_first_name):
        self.subscriber_first_name = subscriber_first_name
   
    def get_subscriber_last_name(self):
        return self.subscriber_last_name
   
    def set_subscriber_last_name(self,subscriber_last_name):
        self.subscriber_last_name = subscriber_last_name
   
    def get_subscriber_dob(self): 
        return self.subscriber_dob
   
    def set_subscriber_dob(self,subscriber_dob): 
        self.subscriber_dob = subscriber_dob
    def make_argument(self):
        self.dic={"api_key":self.api_key,"payer_name":self.payer_name,"payer_id":self.payer_id,"service_provider_first_name":self.service_provider_first_name,"service_provider_last_name":self.service_provider_last_name,"service_provider_npi":self.service_provider_npi,"subscriber_id":self.subscriber_id,"subscriber_first_name":self.subscriber_first_name,"subscriber_last_name":self.subscriber_last_name,"subscriber_dob":self.subscriber_dob}
        return self.dic

    def get_responce(self,resourse,arguments):
        request_url=resourse + "?"+urllib.urlencode(arguments)
        responce_data=urllib2.urlopen(request_url).read()
        responce_data_json=json.loads(responce_data)
        return responce_data_json        
