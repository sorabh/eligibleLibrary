import sys
sys.path.append('/home/sorabh/myProject/eligibleLibrary') ###  put path of library insted of /home/sorabh/myProject/eligibleLibrar/
import demographic
import demographic.DemographicAllRequest as DemographicAllRequest
import unittest

class TestDemographicAllRequest(unittest.TestCase):
    def setup(self):
        pass

    def test_responce_isdict(self):
        request= DemographicAllRequest("TEST","Group Health Demographic - CMR GROUP HEALTH PLAN (GHP)","184","Thomason","Mark","1928384219","W120923801","Austen","Jane","1955-12-14")
	responce=request.submit()
        self.assertTrue(type(responce)==dict)


    def test_responce_isempty(self):
        request= DemographicAllRequest("TEST","Group Health Demographic - CMR GROUP HEALTH PLAN (GHP)","184","Thomason","Mark","1928384219","W120923801","Austen","Jane","1955-12-14")
	responce=request.submit()
        self.assertTrue((responce)!="")
        	
 

if __name__ ==  "__main__":
    unittest.main()
