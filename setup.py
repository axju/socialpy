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
        'cryptography',
        'selenium',
        'chromedriver_autoinstaller',
    ],
    entry_points={
        'socialpy.commands': [
            'api=socialpy.commands:ApiStorageCommand',
            'user=socialpy.commands:UserStorageCommand',
            'post=socialpy.commands:PostCommand',
            'chat=socialpy.commands:ChatCommand',
        ],
        'socialpy.configs': [
            'socialpy.dummy=socialpy.apis.dummy:dummy_values',
            'socialpy.whatsapp=socialpy.apis.whatsapp:WhatsAppConfig',
        ],
        'socialpy.apis': [
            'socialpy.dummy=socialpy.apis.dummy:DummyApi',
            'socialpy.whatsapp=socialpy.apis.whatsapp:WhatsAppApi',
        ],
        'console_scripts': [
            'socialpy=socialpy.__main__:main',
        ],
    },

)
