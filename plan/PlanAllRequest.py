import rest
import rest.RestRequest as RestRequest


class PlanAllRequest(RestRequest):
    resource_url="https://gds.eligibleapi.com/v1/plan/all.json"

    def submit(self):	
        responce_obj=self.get_responce(PlanAllRequest.resource_url,self.make_argument())
        return responce_obj

