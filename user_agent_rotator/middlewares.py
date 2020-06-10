import random
from itertools import cycle

from scrapy import signals
from scrapy.exceptions import NotConfigured

class RotateUserAgentMiddleware(object):
    def __init__(self, user_agents: list, min_usage: int, max_usage: int):
        '''Creates a new instance of RotateUserAgentMiddleware 
        
        Keyword arguments:
            user_agents -- List of user-agents
            min_usage -- Minimum user-agent usage
            max_usage -- Maximum user-agent usage
        '''

        self.items_scraped = 0

        self.min_usage = min_usage
        self.max_usage = max_usage

        self.limit_usage = random.randint(self.min_usage, self.max_usage)

        self.user_agents = cycle(user_agents)
        self.user_agent = next(self.user_agents)

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('ROTATE_USER_AGENT_ENABLED', False):
            raise NotConfigured()

        user_agents = crawler.settings.get('USER_AGENTS', None)

        min_usage = crawler.settings.getint('MIN_USER_AGENT_USAGE', 1)
        max_usage = crawler.settings.getint('MAX_USER_AGENT_USAGE', 100)

        if user_agents is None or min_usage < 0 or max_usage < 0:
            raise NotConfigured()

        return cls(user_agents, min_usage, max_usage)

    def process_request(self, request, spider):
        if self.items_scraped >= self.limit_usage:
            self.items_scraped = 0
            self.limit_usage = random.randint(self.min_usage, self.max_usage)

            self.user_agent = next(self.user_agents)

        request.headers['user-agent'] = self.user_agent
        self.items_scraped += 1
