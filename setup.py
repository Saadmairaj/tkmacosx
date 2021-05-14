from tkmacosx import __version__, __author__
from setuptools import setup, find_packages


def get_long_description(path):
    """Opens and fetches text of long descrition file."""
    with open(path, 'r') as f:
        text = f.read()
    return text


attrs = dict(
    name='tkmacosx',
    version=__version__,
    packages=find_packages(exclude=('test',)),
    long_description=get_long_description('README.md'),
    description='Tkmacosx is a Python library extension to the Tkinter module that let you change background color of the button on macOS.',
    long_description_content_type='text/markdown',
    author=__author__,
    author_email='Saadmairaj@yahoo.in',
    url='https://github.com/Saadmairaj/tkmacosx',
    license='Apache',
    python_requires='>=3',
    install_requires=[
        'colour',
    ],
    keywords=[
        'tkinter',
        'macos',
        'variable',
        'widgets',
        'colorscale',
        'tk',
        'color',
        'button',
        'circlebutton',
        'marquee',
        'tkinter-widgets',
        'tkinter-scrollableframe',
        'scrollableframe',
    ],
    classifiers=[
        'Development Status :: 6 - Mature',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'License :: OSI Approved :: Apache Software License',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/Saadmairaj/tkmacosx/issues',
        'Source': 'https://github.com/Saadmairaj/tkmacosx',
        'Documentation': 'https://github.com/Saadmairaj/tkmacosx#documentation',
    },
    include_package_data=True,
)

setup(**attrs)
