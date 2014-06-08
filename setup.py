from setuptools import setup, find_packages
from pip.req import parse_requirements
import os 

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

# include template
data_files = []
eager_files = []

# Figure out the necessary stuff for the template
rel_path = 'fig_py/default_template'

for dir_name, dir_list, filename_list in os.walk(rel_path):
    file_list = filter(lambda f: not f.endswith('.pyc'), filename_list)
    file_list = [os.path.join(dir_name, filename) for filename in file_list]
    data_files.append((dir_name, file_list))
    eager_files.extend(file_list)

# setup
setup(
  name='fig-py',
  version='0.0.4',
  description='An utility for configuring python projects from jinja templates.',
  long_description = long_description,
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    ],
  keywords='',
  author='Brian Abelson',
  author_email='brian@newslynx.org',
  url='http://github.com/newslynx/fig-py',
  license='MIT',
  packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
  namespace_packages=[],
  include_package_data=False,
  zip_safe=False,
  install_requires=[
    "Jinja2==2.7.2",
    "MarkupSafe==0.23",
    "PyYAML==3.11",
    "Pygments==1.6",
    "Sphinx==1.2.2",
    "docutils==0.11",
    "nose==1.3.3",
    "pypandoc==0.8.2",
    "wsgiref==0.1.2"
  ],
  tests_require=[],
  data_files = data_files,
  eager_resources = eager_files,
  entry_points = {
    'console_scripts': [
      'fig = fig_py:main', 
    ]
    }
)
