from setuptools import setup
setup(
    name='mycli-cli',
    version='0.1.0',
    packages=['mycli'],
    entry_points={
        'console_scripts': [
            'mycli = mycli.__main__:main'
        ]
    })
