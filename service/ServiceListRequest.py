import rest
import rest.RestRequest as RestRequest


class ServiceListRequest(RestRequest):
    resource_url="https://gds.eligibleapi.com/v1/service/list.json"

    def submit(self):	
        responce_obj=self.get_responce(ServiceListRequest.resource_url,self.make_argument())
        return responce_obj

