import os
from setuptools import setup

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


setup(
    name='test',
    version=1.0,
    packages=[
        'opengrok_tools',
    ],
    package_dir={
        'opengrok_tools': 'src/main/python/test',
    },
    url='https://github.com/vladak',
    license='CDDL',
    author='vladak',
    description='setuptools vs. certificates',
    python_requires='>=3.4, <4',
    install_requires=[
        'jsonschema==2.6.0',
        'pyyaml',
        'requests>=2.20.0',
        'resource',
        'filelock',
        'setuptools>=36.7.2',
    ],
    setup_requires=[
        'pytest-runner',
        'setuptools>=36.7.2',
    ],
    tests_require=[
        'pytest',
        'pytest-xdist',
        'mockito',
        'pytest-mockito',
    ],
)
