import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware


class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent_list):
        super().__init__()
        self.user_agent_list = user_agent_list

    @classmethod
    def from_crawler(cls, crawler):
        ua_file = crawler.settings.get('USER_AGENT_FILE', 'user_agents.txt')
        with open(ua_file, 'r') as file:
            user_agent_list = [line.strip() for line in file.readlines()]
        return cls(user_agent_list)

    def process_request(self, request, spider):
        user_agent = random.choice(self.user_agent_list)
        request.headers.setdefault('User-Agent', user_agent)
