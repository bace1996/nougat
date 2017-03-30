from setuptools import setup, find_packages
from os import path
from misuzu import __version__

here = path.abspath(path.dirname(__file__))


setup_kwargs = {
    'name': 'misuzu',
    'version': __version__,
    'description': 'Async API framework with human friendly params definition and automatic document',
    'url': 'https://github.com/Kilerd/misuzu',

    'author': 'Kilerd Chan',
    'author_email': 'blove694@gmail.com',

    'license': 'MIT',

    'classifiers': [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    'keywords': 'web framework async',

    'packages': ['misuzu'],
    'install_requires': ['uvloop'],
}
try:
    normal_requirements = [
        'httptools>=0.0.9',
        'uvloop>=0.5.3',
        'aiofiles>=0.3.0',
    ]
    setup_kwargs['install_requires'] = normal_requirements
    setup(**setup_kwargs)

except DistutilsPlatformError as exception:
    windows_requirements = [
        'httptools>=0.0.9',
    ]
    setup_kwargs['install_requires'] = windows_requirements
    setup(**setup_kwargs)