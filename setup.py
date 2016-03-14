"""Setup for data-structures package."""

from setuptools import setup


setup(name='data-structures',
      description='Command line program to manage data-structures.',
      version=0.1,
      keywords=[],
      classifiers=[],
      author='Kevin Gifford',
      author_email='ksgifford@gmail.com',
      license='MIT',
      packages=[],  # all your python packages with an __init__ file
      py_modules=['linked_list',
                  'stack',
                  'dbl_linked_list',
                  'new_queue',
                  'new_deque'
                  ],  # your python modules to include
      package_dir={'': 'src'},
      install_requires=[],
      extras_require={'test': ['pytest', 'pytest-xdist', 'tox']}
      )
