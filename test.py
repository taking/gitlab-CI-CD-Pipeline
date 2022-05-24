#!/usr/bin/python
import sys
import json
import unittest
import app as myapi


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = myapi.app.test_client()

    def test_sample_index(self):
        print("index('/') API CALL TEST")
        response = self.app.get('/')
        self.assertEqual(
            json.loads(response.get_data().decode(sys.getdefaultencoding())),
            {"message": "ok"}
        )

    def test_sample_test(self):
        print("test('/test') API CALL TEST")
        response = self.app.get('/test')
        self.assertEqual(
            json.loads(response.get_data().decode(sys.getdefaultencoding())),
            {"message": "test"}
        )


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
