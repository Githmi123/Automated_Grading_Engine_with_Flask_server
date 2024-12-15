import unittest
from unittest.mock import patch
from server import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    # def test_members_route(self):
    #     response = self.app.get('/members')
    #     data = response.get_json()
    #     self.assertEqual(data['members'], ["Member1", "Member2", "Member3"])
    #     self.assertEqual(response.status_code, 200)

    # @patch('server.fetch_image_urls_from_s3')
    # def test_get_image_urls_route(self, mock_fetch_image_urls_from_s3):
    #     mock_fetch_image_urls_from_s3.return_value = ['url1', 'url2']
    #     response = self.app.get('/image_urls')
    #     data = response.get_json()
    #     self.assertEqual(data['image_urls'], ['url1', 'url2'])
    #     self.assertEqual(response.status_code, 200)

    @patch('server.download_images')
    @patch('server.download_markingscheme')
    @patch('server.grader.grade')
    @patch('server.delete_directory_contents')
    def test_grade_images_route(self, mock_download_images, mock_download_markingscheme, mock_grader_grade, mock_delete_directory_contents):
        data = {
            'answerScript': 'scheme_url',
            'studentAnswers': [{'studentId': '1', 'downloadUrl': 'url1'}, {'studentId': '2', 'downloadUrl': 'url2'}]
        }

        response = self.app.post('/grade', json=data)

        # Assert that download_images, download_markingscheme, and grader.grade were called with the correct arguments
        mock_download_images.assert_called_once_with(['url1', 'url2'], ['1', '2'], 'downloaded_images')
        mock_download_markingscheme.assert_called_once_with('scheme_url', 'downloaded_marking_scheme')
        mock_grader_grade.assert_called()
        mock_delete_directory_contents.assert_called_with('downloaded_images')
        mock_delete_directory_contents.assert_called_with('downloaded_marking_scheme')

        # Assert the response
        data = response.get_json()
        self.assertEqual(data['message'], "Grade received successfully")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

# import unittest
# from unittest.mock import patch
# from server import app

# class TestFlaskApp(unittest.TestCase):

#     def setUp(self):
#         app.testing = True
#         self.app = app.test_client()

#     def tearDown(self):
#         pass

#     def test_members_route(self):
#         response = self.app.get('/members')
#         data = response.get_json()
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('members', data)
#         self.assertListEqual(data['members'], ["Member1", "Member2", "Member3"])

#     # Add other test methods for your routes...

# if __name__ == '__main__':
#     unittest.main()
