from setuptools import setup


def long_description():
    with open('Information.md') as f:
        longdis = f.read()
    return longdis


setup(
    name="tkmacosx",
    version="0.1.0",
    description="Tkmacosx is a Python library extension to the Tkinter module for macOS",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Saadmairaj/tkmacosx",
    author="Saad Mairaj",
    author_email="Saadmairaj@yahoo.in",
    license="Apache",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Build Tools",
        'Topic :: Software Development :: Widget Sets',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: MacOS X",

    ],
    keywords=['tkinter', 'macos', 'variable', 'widgets', 'colorscale', 'tk'],
    packages=["tkmacosx"],
    include_package_data=True,
    install_requires=['colour', 'pillow'],
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/Saadmairaj/tkmacosx',
        'Source': 'https://github.com/Saadmairaj/tkmacosx/issues',
    },
)
