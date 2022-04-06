import os
import io

from setuptools import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name='kociemba',
    version='1.2.1',
    description='Python/C implementation of Herbert Kociemba\'s 2x2 optimal solver',
    long_description=readme,
    long_description_content_type='text/markdown',
    keywords='kociemba 2x2 rubik cube solver',
    url='https://github.com/Safacan7/Rubiks2x2x2-OptimalSolver',
    author='safacan',
    author_email='kokcansafa7@gmail.com',
    license='GPLv2',
    packages=['kociemba_2x2'],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
    ),
    setup_requires=['pytest-runner', "cffi>=1.0.0"],
    tests_require=['pytest', ],
    zip_safe=False,
    install_requires=["cffi>=1.0.0", 'future'],
)