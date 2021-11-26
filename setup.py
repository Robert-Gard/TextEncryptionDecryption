from setuptools import setup
setup(
    name = 'TextEncyptionDecrytion',
    version = '0.1.0',
    packages = ['TextEncyptionDecrytion'],
    entry_points = {
        'console_scripts': [
            'TextEncyptionDecrytion = TextEncyptionDecrytion.__main__:main'
        ]
    })