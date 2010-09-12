import os
from setuptools import setup, find_packages

def read_file(filename):
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''

setup(
    name = "django-elrte",
    version = __import__('django-elrte').get_version().replace(' ', '-'),
    url = '',
    author = 'coordt',
    author_email = '',
    description = 'Django-elRTE is an easy way to use the elRTE rich text editor within Django without creating dependencies.',
    long_description = read_file('README.rst'),
    packages = find_packages(),
    include_package_data = True,
    install_requires=read_file('requirements.txt'),
    classifiers = [
    ],
)
