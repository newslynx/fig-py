from setuptools import setup, find_packages
import os 
from pip.req import parse_requirements

# hack for working with pandocs
import codecs 
try: 
  codecs.lookup('mbcs') 
except LookupError: 
  utf8 = codecs.lookup('utf-8') 
  func = lambda name, enc=utf8: {True: enc}.get(name=='mbcs') 
  codecs.register(func) 

# install readme
readme = os.path.join(os.path.dirname(__file__), 'README.md')

try:
  import pypandoc
  long_description = pypandoc.convert(readme, 'rst')
except (IOError, ImportError):
  long_description = ""

# parse requirements file
required = [str(ir.req) for ir in parse_requirements("requirements.txt")]

# setup
setup(
  name='{{ project_name }}',
  version='0.0.1',
  description='{{ description }}',
  long_description = long_description,
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    ],
  keywords='',
  author='{{ author }}',
  author_email='{{ email }}',
  url='http://github.com/{{ github_user }}/{{ project_name }}',
  license='MIT',
  packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
  namespace_packages=[],
  include_package_data=False,
  zip_safe=False,
  install_requires=[
  ],
  tests_require=[]
)
