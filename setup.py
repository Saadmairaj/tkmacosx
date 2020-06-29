from setuptools import setup


def long_description():
    with open('Information.md') as f:
        longdis = f.read()
    return longdis


setup(
    name="tkmacosx",
    version="0.1.4",
    description="Tkmacosx is a Python library extension to the Tkinter module for macOS.",
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
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.3",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
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
    keywords=['tkinter', 'macos', 'variable', 'widgets', 'colorscale', 'tk', 'color'],
    packages=["tkmacosx"],
    include_package_data=True,
    install_requires=['colour'],
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/Saadmairaj/tkmacosx/issues',
        'Source': 'https://github.com/Saadmairaj/tkmacosx',
        'Documentation': 'https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx#documentation-of-tkmacosx',
    },
)
