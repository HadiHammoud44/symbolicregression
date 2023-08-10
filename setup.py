from setuptools import setup, find_packages
import pathlib


dir = pathlib.Path(__file__).resolve().parent
with open(dir / 'README.md', 'r') as f:
    readme = f.read()

setup(
    name='symbolicregression',
    version='1.0',       
    license='Apache License 2.0',      
    description='Symbolic Regression based on LLMs',
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Pierre-Alexandre Kamienny, Stéphane d'Ascoli, Guillaume Lample, François Charton",
    url='https://github.com/facebookresearch/symbolicregression',  
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    python_requires=">=3.7",
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
)
