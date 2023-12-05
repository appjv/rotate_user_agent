# Rotate User Agent Middleware for Scrapy

This package provides a Scrapy middleware for rotating user agents with each request, which can help in avoiding getting blocked by websites that limit scraping.

## Features
- Easy integration with Scrapy projects.
- Automatic rotation of user agents for each request.
- Customizable list of user agents.

## Installation

You can install the package directly from GitHub using pip:

```bash
pip install git+https://github.com/appjv/rotate_user_agent.git
```
## Usage

Specify the middleware in your Scrapy project's settings.py file as well as the location of your user_agent.txt file.

```python
DOWNLOADER_MIDDLEWARES = {
    # ... other middlewares ...
    'rotate_user_agent.RotateUserAgentMiddleware': 543,
}

USER_AGENT_FILE = 'path/to/your/user_agents.txt'  # Adjust the path as needed
```

