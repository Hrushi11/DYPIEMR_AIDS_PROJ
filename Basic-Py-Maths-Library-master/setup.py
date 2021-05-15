from setuptools import _install_setup_requires, setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
  name='MathsBasicsFunctions',
  version='0.0.1',
  description='A basic maths functions',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',
  author='unnumsykar',
  author_email='1709krsunny@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='BasicMaths',
  packages=find_packages(),
  install_requires=['']

)