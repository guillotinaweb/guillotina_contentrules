from setuptools import find_packages
from setuptools import setup


try:
    README = open('README.rst').read()
except IOError:
    README = None

setup(
    name='guillotina_contentrules',
    version="1.0.0",
    description='Provide dynamic actions based on content',
    long_description=README,
    install_requires=[
        'guillotina'
    ],
    author='Nathan Van Gheem',
    author_email='vangheem@gmail.com',
    url='',
    packages=find_packages(exclude=['demo']),
    include_package_data=True,
    tests_require=[
        'pytest',
    ],
    extras_require={
        'test': [
            'pytest'
        ]
    },
    classifiers=[],
    entry_points={
    }
)
