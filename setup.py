from setuptools import setup, find_packages

setup(
    name="faker_animals",  # Your package name on PyPI
    version="1.0",               # Package version
    license='MIT',
    description="A provider for the python faker library to generate random animals data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Symeon Iordanidis",
    author_email="iordanidissimeon@gmail.com",
    url="https://github.com/symeoniordanidis/faker_animals",  # URL to your repo (optional)
    packages=find_packages(),
    install_requires=['faker'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
