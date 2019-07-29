from django.test import TestCase
from .models import SimpleModel
from django.http import HttpRequest
# Create your tests here.

class SimpleModelTestCase(TestCase):
    def test_homepage_testcode(self):
        response = self.client.get('/api/v1/')
        self.assertEquals(response.status_code, 200)
    def test_create_get_object(self):
        sobj = SimpleModel.objects.create(name='Software13432434',description='this is description for software13432434',
        driver='ORACLE',host='193.33.23.33',port=80,username='user3423424',password="pass2343434343")
        s_details: list = [sobj.name,sobj.driver,sobj.host,sobj.port]
        print(s_details)
        obj_id: str = str(sobj.id)
        response = self.client.get('/api/v1/'+ obj_id + '/')
        self.assertEquals(response.status_code,200)

    

