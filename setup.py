from setuptools import setup, find_packages

setup(
    name='weather386',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy==1.24.2',
        'openmeteo_requests==1.1.0',
        'openmeteo_sdk==1.7.0',
        'pandas==1.5.3',
        'requests==2.28.2',
        'matplotlib==3.7.1',
        'seaborn==0.13.0',
        'python-dateutil==2.8.2',
        'requests_cache==1.1.1',
        'retry_requests==2.0.0'
    ],
    author='Cameron Slaugh, Taylor Davis',
    author_email='cmslaugh@student.byu.edu, tpd25@student.byu.edu',
    description='''A package made in conjunction to our data science
    class at BYU that provides an easy way to access and visualize
    weather forecast and history data with a few easy to use functions.''',
    url='https://lightningcookies.github.io/weather386/',
)