from setuptools import setup
from os import path
from nougat import __version__

here = path.abspath(path.dirname(__file__))

setup(
    name='nougat',
    version=__version__,
    description='Async API framework with human friendly params definition and automatic document',
    url='https://github.com/Kilerd/nougat',

    author='Kilerd Chan',
    author_mail='blove694@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='web framework async',

    packages=['nougat'],

    install_requires=[
        'curio>=0.8',
        'h11>=0.7.0',
        'yarl>=0.13.0',
        'click>=6.7.0'
    ],
    python_requires='>=3.6',
    entry_points='''
        [console_scripts]
        nougat=nougat.script:cli
    '''

)

