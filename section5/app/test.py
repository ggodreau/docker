import unittest
import app

class TestDockerapp(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
    
    # calls the '/' url with a key value pair and sets the submit value to save
    # and verifies that the return response is 200 with 2 and two in response
    def test_save_value(self):
        response = self.app.post('/', data=dict(submit='save', key='2', cache_value='two'))
        assert response.status_code == 200
        assert b'2' in response.data
        assert b'two' in response.data

    # loads in the values that we just set from the previous test case
    def test_load_value(self):
        self.app.post('/', data=dict(submit='save', key='2', cache_value='two'))
        response = self.app.post('/', data=dict(submit='load', key='2'))
        assert response.status_code == 200
        assert b'2' in response.data
        assert b'two' in response.data

if __name__=='__main__':
    unittest.main()
