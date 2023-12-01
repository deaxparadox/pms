from django.test import TestCase, LiveServerTestCase

from . import URL_api_v1

# {
#         "id": 1,
#         "heading": "October",
#         "start": null,
#         "end": null,
#         "created": "2023-10-07T14:49:27.015000Z",
#         "updated": "2023-10-07T14:49:27.015000Z",
#         "tasks": [
#             {
#                 "task": "c binary tree",
#                 "start": "2023-10-01",
#                 "end": "2023-10-31",
#                 "created": "2023-10-07T16:11:00.375000Z",
#                 "updated": "2023-10-07T16:36:42.827000Z"
#             }
#         ]
#     }


class HeadingsTestCase(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get(f"{URL_api_v1}")

    def test_headings_response_status_code(self):
        self.assertEqual(self.response.status_code, 200)


    def test_headings_response_structure(self):
        # print(type(self.response))
        self.assertEqual(type(self.response.json()), list)




        