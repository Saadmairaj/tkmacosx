from setuptools import setup

def long_description():
    with open('Information.md') as f:
        longdis = f.read()
    return longdis

setup(
    name="tkmacosx",
    version="0.0.1",
    description="Tkmacosx is a Python library extension to Tkinter module for masOS",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Saadmairaj/tkmacosx",
    author="Saad Mairaj",
    author_email="Saadmairaj@yahoo.in",
    license="Apache",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: MacOS X"
    ],
    packages=["tkmacosx"],
    include_package_data=True,
    install_requires=['colour', 'pillow']
)