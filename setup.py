from setuptools import setup
setup(
    name = 'TextEncyptionDecryption',
    version = '0.1.0',
    packages = ['TextEncyptionDecryption'],
    entry_points = {
        'console_scripts': [
            'TextEncyptionDecryption = TextEncyptionDecryption.__main__:main'
        ]
    })