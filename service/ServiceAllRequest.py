import rest
import rest.RestRequest as RestRequest


class ServiceAllRequest(RestRequest):
    resource_url="https://gds.eligibleapi.com/v1/service/all.json"
    def __init__(self,service_type_code, api_key, payer_name, payer_id,  service_provider_first_name, service_provider_last_name, service_provider_npi,  subscriber_id, subscriber_first_name,  subscriber_last_name, subscriber_dob):
        RestRequest.__init__(self, api_key, payer_name, payer_id,  service_provider_first_name, service_provider_last_name, service_provider_npi,  subscriber_id, subscriber_first_name,  subscriber_last_name, subscriber_dob)
        self.service_type_code=service_type_code

    def get_service_type_code(self):
        return self.service_type_code

    def set_service_type_code(self,service_type_code):
        self.service_type_code = service_type_code

    def make_argument(self):
        RestRequest.makeArgument(self)
        self.dic["service_type_code"]=self.service_type_code
        return self.dic

    def submit(self):	
        responce_obj=self.get_responce(ServiceAllRequest.resource_url,self.make_argument())
        return responce_obj

