from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='mpl_finance',
      version='0.10.1',
      author='MPL Developers',
      author_email='matplotlib-users@python.org',
      py_modules=['mpl_finance'],
      description='Finance plots using matplotlib',
      long_description=long_description,
      long_description_content_type='text/markdown; charset=UTF-8',
      url='http://github.com/matplotlib/mpl-finance',
      platforms='Cross platform (Linux, Mac OSX, Windows)',
      install_requires=['matplotlib'],
      license="BSD-style",
      classifiers=['Development Status :: 7 - Inactive',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   ],
      keywords='finance',
      )
