import os
import io

from setuptools import setup

long_description = io.open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8').read()

setup(
    name='kociemba',
    version='1.2.1',
    description='Python/C implementation of Herbert Kociemba\'s 2x2 optimal solver',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='kociemba 2x2 rubik cube solver',
    url='https://github.com/Safacan7/Rubiks2x2x2-OptimalSolver',
    author='safacan',
    author_email='kokcansafa7@gmail.com',
    license='GPLv2',
    packages=['kociemba_2x2'],
    package_data={
        '': [
            'cprunetables/*',
            'kociemba/*.py'
            'pykociemba/*.py',
            'pykociemba/prunetables/*',
            'ckociemba/include/*.h',
            'ckociemba/*.c'],
    },
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
    ),
    entry_points = {
        'console_scripts': ['kociemba=kociemba.command_line:main'],
    },
    setup_requires=['pytest-runner', "cffi>=1.0.0"],
    tests_require=['pytest', ],
    zip_safe=False,
    cffi_modules=["kociemba/build_ckociemba.py:ffi"],
    install_requires=["cffi>=1.0.0", 'future'],
)