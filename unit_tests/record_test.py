import unittest
import requests
import json



class RecordTest(unittest.TestCase):
    """Test case for the record's namespace"""


    def setUp(self):
        """Set up some configs before the test"
        """
        # SERVER
        self.host = "localhost"
        self.port = 3000
        # ROUTES
        self.multi_url  = "http://" + self.host + ":" + str(self.port) + "/api/records"
        self.single_url = "http://" + self.host + ":" + str(self.port) + "/api/record"



    def tearDown(self):
        """Called after each test
        """
        pass

    

    def test_getAll(self):
        """ Testing the route that returns all documents
        """
        res = requests.get(self.multi_url)
        res_json = res.json()

        # Testing body
        self.assertEqual(res.status_code, 200)                              # status_code
        self.assertEqual(res.headers['Content-Type'], 'application/json')   # content type is json
        # Testing content
        self.assertIsNotNone(res_json['message'])           # message content is not null
        self.assertIsNotNone(res_json['data'])              # data content is not null
        self.assertEqual(res_json['message'], 'success')    # success message
        self.assertIsInstance(res_json['data'], list)       # data content is a list


    def test_postOne(self):
        """ Testing the route that allows to post one document
        """
        with open('unit_tests/datasets/postOne_dummy.json', 'r') as f:
            data = json.load(f)
            res = requests.post(self.single_url, json=data)
            res_json = res.json()

            # Testing body
            self.assertEqual(res.status_code, 201)                              # status_code
            self.assertEqual(res.headers['Content-Type'], 'application/json')   # content type is json
            # Testing content
            self.assertIsNotNone(res_json['message'])                       # message content is not null
            self.assertIsNotNone(res_json['data'])                          # data content is not null
            self.assertIsNotNone(res_json['data']['inserted_id'])           # inserted_id content not null
            self.assertEqual(res_json['message'], 'success')                # success message
            self.assertIsInstance(res_json['data'], dict)                   # data content is a dict
            self.assertIsInstance(res_json['data']['inserted_id'], str)     # inserted_id content type is a string


    def test_postMany(self):
        """ Testing the route that allows to post multiple documents
        """
        with open('unit_tests/datasets/postMany_dummy.json', 'r') as f:
            data = json.load(f)
            res = requests.post(self.multi_url, json=data)
            res_json = res.json()

            # Testing body
            self.assertEqual(res.status_code, 201)                              # status_code
            self.assertEqual(res.headers['Content-Type'], 'application/json')   # content type is json
            # Testing content
            self.assertIsNotNone(res_json['message'])                       # message content is not null
            self.assertIsNotNone(res_json['data'])                          # data content is not null
            self.assertIsNotNone(res_json['data']['inserted_ids'])          # inserted_ids content not null
            self.assertEqual(res_json['message'], 'success')                # success message
            self.assertIsInstance(res_json['data'], dict)                   # data content is a dict
            self.assertIsInstance(res_json['data']['inserted_ids'], list)   # inserted_ids content type is a list
            self.assertGreater(len(res_json['data']['inserted_ids']), 0)    # inserted_ids content not empty
            