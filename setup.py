from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='steam-wrapper-api',
    version='0.1',
    license='MIT License',
    author='Gabriel Batistuta',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='batistutag190@gmail.com',
    keywords='steam, wrapper, api',
    description=u'unofficial steam API wrapper',
    packages=['steam_api'],
    install_requires=['requests'],)