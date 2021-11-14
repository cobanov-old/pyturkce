#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

test_requirements = []

setup(
    author="Mert Cobanov",
    author_email='mertcobanov@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python package for Turkish Language.",
    entry_points={
        'console_scripts': [
            'pyturkce=pyturkce.cli:main',
        ],
    },  
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='pyturkce',
    name='pyturkce',
    packages=find_packages(include=['pyturkce', 'pyturkce.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/cobanov/pyturkce',
    version='0.1.1',
    zip_safe=False,
)
