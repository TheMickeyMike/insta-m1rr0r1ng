import unittest
from unittest.mock import Mock

from insta_provider import InstaProvider


class TestInstaProvider(unittest.TestCase):
    def setUp(self):
        self.instagram_conductor = InstaProvider(
            web_api_client=Mock(), authed_web_api_client=Mock(search_users=Mock()))

        self.instagram_user_search_response = {
            'users': [
                {'pk': 12345, 'username': 'username', 'full_name': 'Elvis Musk'}
            ],
            "num_results": 1,
            "status": 'ok'
        }

    def test_should_resolve_instagram_username_to_user_id(self):
        self.instagram_conductor.authed_web_api_client.search_users.return_value = self.instagram_user_search_response
        result = self.instagram_conductor.get_user_id('username')
        self.instagram_conductor.authed_web_api_client.search_users.assert_called_once_with('username')
        self.assertEqual(result, 12345)

    def test_should_get_user_feed(self):
        self.instagram_conductor.web_api_client.user_feed.return_value = []
        results = self.instagram_conductor.get_user_feed(12345)
        self.instagram_conductor.web_api_client.user_feed.assert_called_once_with(12345)
        self.assertEqual(results, [])
