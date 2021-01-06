from setuptools import setup


setup(
    name='socialpy',
    description='Use social networks like a hacke',
    url='https://github.com/axju/socialpy',
    author='axju',
    author_email='moin@axju.de',
    license='MIT',
    long_description='...',
    long_description_content_type='text/markdown',

    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    include_package_data=True,
    zip_Storage=False,

    packages=['socialpy'],
    install_requires=[
    ],
    entry_points={
        'socialpy.commands': [
            'api=socialpy.commands:ApiCommand',
            'post=socialpy.commands:PostCommand',
        ],
        'socialpy.configs': [
            'dummy=socialpy.apis.dummy:dummy_values',
        ],
        'socialpy.apis': [
            'dummy=socialpy.apis.dummy:DummyApi',
        ],
        'console_scripts': [
            'socialpy=socialpy.__main__:main',
        ],
    },

)
