from setuptools import setup
import codecs
import os.path


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


def get_readme():
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, 'README.md'), mode='r') as file:
        readme = file.read()
    return readme


setup(
    name='py-doccle',
    version=get_version("doccle/__init__.py"),
    description='A Python package to get data from Doccle.',
    url='https://github.com/sgilissen/py-doccle',
    author='Steve Gilissen',
    license='GNU GPLv3',
    long_description=get_readme(),
    long_description_content_type='text/markdown',
    packages=['doccle'],
    install_requires=['requests'],

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
)
