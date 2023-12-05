import unittest
from importlib import resources
from rotate_user_agent.middleware import RotateUserAgentMiddleware
from scrapy.http import Request
from scrapy.spiders import Spider
from scrapy.utils.test import get_crawler


class TestRotateUserAgentMiddleware(unittest.TestCase):
    def setUp(self):
        # Access the user_agents.txt file from the package
        with resources.path('rotate_user_agent', 'user_agents.txt') as user_agents_file:
            # Setting up a crawler with the user agent list from the package
            self.crawler = get_crawler(settings_dict={'USER_AGENT_FILE': str(user_agents_file)})
            self.middleware = RotateUserAgentMiddleware.from_crawler(self.crawler)

    def test_user_agent_rotation(self):
        spider = Spider('dummy')
        last_user_agent = None

        for _ in range(10):  # Test with 10 requests
            request = Request('https://httpbin.org/')
            self.middleware.process_request(request, spider)
            user_agent = request.headers.get('User-Agent', b'').decode('utf-8')
            print(f"++ User Agent: {user_agent} \n")

            if last_user_agent:
                self.assertNotEqual(user_agent, last_user_agent,
                                    "Two consecutive requests used the same user agent, indicating lack of rotation.")

            last_user_agent = user_agent

    def test_unique_user_agent_each_request(self):
        spider = Spider('dummy')
        seen_user_agents = set()
        allowed_repetitions = 2  # Allow a user agent to be repeated twice

        for _ in range(10):  # Test with 10 requests
            request = Request('https://httpbin.org/')
            self.middleware.process_request(request, spider)
            user_agent = request.headers.get('User-Agent', b'').decode('utf-8')

            # Count the repetitions of the user agent
            seen_user_agents.add(user_agent)
            if list(seen_user_agents).count(user_agent) > allowed_repetitions:
                self.fail(f"User agent '{user_agent}' repeated more than {allowed_repetitions} times")


if __name__ == '__main__':
    unittest.main()
