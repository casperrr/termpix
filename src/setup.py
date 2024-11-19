# import glob
from setuptools import setup, find_packages

with open("../README.md", "r") as f:
    long_description = f.read()

# tpix_files = glob.glob('tpix/*')

setup(
    name='termpix',
    version='0.1',
    description='Convert and display images as text in your terminal',
    long_description=long_description,
    author='casperrr',
    author_email='casper.sebastien@gmail.com',
    url='http://github.com/casperrr/termpix',
    packages=find_packages(),
    install_requires=[
        'pillow',
        'validators',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'termpix = termpix.__main__:main',
        ],
    }
)