import unittest
import server.s3 as storage
import requests

class TestS3IO(unittest.TestCase):
    def test_upload(self):
        object_name = "test.txt"
        post = storage.generate_presigned_post(object_name)

        files = {"file": "test_content"}
        response = requests.post(post["url"], data=post["fields"], files=files)
        # assert response code is 204
        self.assertEqual(response.status_code, 204)

    def test_download(self):
        object_name = "test.txt"
        download_url = storage.generate_presigned_url(object_name)
        
        response = requests.get(download_url)
        # assert response code is 200
        self.assertEqual(response.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()