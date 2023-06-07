from setuptools import setup

setup(
    name='shubhank_utility',
    version='0.1.3',
    description='A Python package for personal work',
    # url='https://github.com/shuds13/pyexample',
    author='Shubhank Singhal',
    author_email='shubhank.singhal1@acuitykp.com',
    # license='BSD 2-clause',
    packages=['shubhank_utility'],
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
        # 'Development Status :: 1 - Planning',
        # 'Intended Audience :: Science/Research',
        # 'License :: OSI Approved :: BSD License',
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