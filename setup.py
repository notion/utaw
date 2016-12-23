"""Setup for utaw."""


# [ Imports ]
# [ -Python ]
from setuptools import setup, find_packages


# [ Main ]
setup(
    name='utaw',
    version='0.1.0',
    description='UTAW: UnitTest Assertion Wrapper.',
    url='https://github.com/notion/utaw',
    author='toejough',
    author_email='toejough@gmail.com',
    classifiers=[
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 3 - Alpha',

            # Indicate who your project is intended for
            'Intended Audience :: Developers',

            # Pick your license as you wish (should match "license" above)
            'License :: OSI Approved :: Apache Software License',

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
    ],
    keywords="test assert assertions",
    packages=find_packages(),
    install_requires=[],
    entry_points={}
)
