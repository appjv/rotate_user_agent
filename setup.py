# Setup template originally taken from learnpythonthehardway.org/book/ex46.html

def main():
    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup

    config = {
        'description': 'A Scrapy middleware to rotate user agents',
        'author': 'Joseph App',
        'download_url': 'not online',
        'author_email': 'appjoseph09@gmail.com',
        'version': '0.1.0',
        'install_requires': ['scrapy>=2.0.0'],
        # 'packages': [],
        # 'scripts': [],
        'name': 'rotate_user_agent'
    }

    setup(**config)


if __name__ == '__main__':
    main()
