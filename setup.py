from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='socialpy',
      version='0.0.1',
      description='A gateway to all common uses social networks',
      long_description=readme(),
      keywords='social network',
      url='https://github.com/axju/socialpy',
      author='Axel Juraske',
      author_email='axel.juraske@short-report.de',
      license='MIT',
      packages=['socialpy'],
      install_requires=[
          'tweepy', 'InstagramAPI'
      ],
      zip_safe=False)
