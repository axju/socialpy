import os
from setuptools import setup, find_packages

base_dir = os.path.dirname(__file__)

def readme():
    with open('README.md') as f:
        return f.read()

about = {}
with open(os.path.join(base_dir, 'socialpy', '__about__.py')) as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__summary__'],
    url=about['__url__'],
    author=about['__author__'],
    author_email=about['__email__'],
    license=about['__license__'],
    long_description=readme(),
    long_description_content_type='text/markdown',

    packages=find_packages(),
    install_requires=[
        'tweepy', #'InstagramAPI', 'facepy',
        'django', 'djangorestframework', 'coreapi', 'Pillow',
        'tabulate',
    ],
    entry_points = {
        'console_scripts': [
            'socialpy=socialpy.__main__:main',
            'socialpy-client=socialpy.client.__main__:main',
            'socialpy-server=socialpy.server.__main__:main',
            'socialpy-data=socialpy.data.__main__:main',

            'socialpy-twitter-setup=socialpy.scripts.twitter:setup',
        ],
    },
    include_package_data=True,
    zip_safe=False
)
