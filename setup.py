from setuptools import setup, find_packages

setup(
    name='sample',
    version='0.0.1',
    description='Sample package',
    author='ibara1454',
    author_email='ibara1454@gmail.com',
    url='',
    license='',
    package_dir={'sample': 'src'},
    packages=['sample'],
    install_requires=[
        'mpi4py'
    ],
    dependency_links=[],
    test_suite='test'
)
