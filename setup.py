from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='socialpy',
      version='0.0.1',
      description='Use social networks like a hacker',
      long_description=readme(),
      keywords='social network',
      url='https://github.com/axju/socialpy',
      author='Axel Juraske',
      author_email='axel.juraske@short-report.de',
      license='MIT',
      packages=['socialpy'],
      install_requires=[
          'tweepy', 'InstagramAPI', 'facepy', 'django', 'tabulate',
      ],
      entry_points = {
        'console_scripts': [
            'socialpy-client=socialpy.client.__main__:main',
            'socialpy-server=socialpy.server.__main__:main',
            'socialpy-data=socialpy.data.__main__:main',
        ],
      },
      zip_safe=False)
