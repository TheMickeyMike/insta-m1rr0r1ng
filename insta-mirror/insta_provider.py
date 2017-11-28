from instagram_private_api import Client as AuthedWebApiClient
from instagram_web_api import Client as WebApiClient


def create_insta_provider(username, password):
    return InstaProvider(
        WebApiClient(auto_patch=True, drop_incompat_keys=False),
        AuthedWebApiClient(username, password)
    )


class InstaProvider:
    def __init__(self, web_api_client, authed_web_api_client=None):
        self.web_api_client = web_api_client
        self.authed_web_api_client = authed_web_api_client

    def get_user_feed(self, user_id):
        return self.web_api_client.user_feed(user_id)

    def get_user_id(self, username):
        query_results = self.authed_web_api_client.search_users(username)
        if query_results['status'] != 'ok':
            raise Exception('dsadsda')
        if query_results['num_results'] >= 1:
            return query_results['users'][0][
                'pk']  # , query_results['users']['username'], query_results['users']['full_name']


