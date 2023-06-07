# from setuptools import setup
from distutils.core import setup

setup(
    name='shubhank_utility',
    packages=['shubhank_utility'],
    version='0.0.1',
    license='MIT',
    description='A Python package for personal work',
    author='Shubhank Singhal',
    author_email='shubhank.singhal98@gmail.com',
    url='https://github.com/ShubhankSinghal/shubhank-utility',
    keywords=['SHUBHANK', 'SHUBHANK SINGHAL'],
    install_requires = [
        'pymongo',
        'requests',
        'tldextract',
        'fuzzywuzzy',
        "bs4",
        "beautifulsoup4",
        "html5lib",
        "lxml",
        "pymssql",
        "python-Levenshtein",
        "pandas",
        "numpy",
        "nltk"
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.*'
    ],
)