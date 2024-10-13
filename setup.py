from setuptools import setup, find_packages
#from src.importlistparser import __version__


setup(
    name='SimplHDL-gowin',
    description='Gowin synthesis flow for SimplHDL projects.',
    version=0.1,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    entry_points={
        'simplhdl.plugins': [
            'flow=gowin'],
    },
    install_requires=[
        'SimplHDL',
    ],
)
