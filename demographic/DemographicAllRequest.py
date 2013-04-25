import rest
import rest.RestRequest as RestRequest


class DemographicAllRequest(RestRequest):
    resource_url="https://gds.eligibleapi.com/v1/demographic/all.json"

    def submit(self):	
        responce_obj=self.get_responce(DemographicAllRequest.resource_url,self.make_argument())
        return responce_obj

