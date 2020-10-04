from distutils.core import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
  name = 'albion_data',         # How you named your package folder (MyLib)
  packages = ['albion_data'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A python wrapper for Albion data Project',   # Give a short description about your library
  long_description=long_description,
  author = 'dravog7',                   # Type in your name
  author_email = 'dravog78@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/dravog7/Albion-data-python',   # Provide either the link to your github or to your website
  keywords = ['Albion', 'api'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
        'requests',
    ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Games/Entertainment',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which python versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)