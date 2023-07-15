from django.test import TestCase, Client


# Create your tests here.
class TestHello(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_index_get(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello World")
    
    def test_index_post(self):
        data =  {"note": "Lorem Ipsum"}
        response = self.client.post("/", data=data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, data["note"])
        self.assertNotContains(response, "HAHAHHA!!!!")