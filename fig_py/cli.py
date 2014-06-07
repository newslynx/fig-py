# -*- coding: utf-8 -*-

"""
fig -p fig -g newslynx \
-a 'Brian Abelson' -e 'brianabelson@gmail.com' \
-d 'A python package for initializing python packages'
"""
import subprocess 
import os
import argparse

from util import *
from create_template import create_template

def parse_args():
  parser = argparse.ArgumentParser(
    description='Initialize a python repository from a directory of jinja templates.')

  parser.add_argument(
    '-p', '--project-name', 
    dest='project_name',
    help='The name of your project.')

  parser.add_argument(
    '-g', '--github-user', 
    dest='github_user',
    help='Your github user name.')

  parser.add_argument(
    '-a', '--author', 
    dest='author',
    help="Your name.",
    default="")

  parser.add_argument(
    '-e', '--email', 
    dest='email',
    help="Your email.",
    default="")

  parser.add_argument(
    '-d', '--description', 
    dest='description',
    help="The projects' description.",
    default="")

  parser.add_argument(
    '-t', '--template', 
    dest='tmpl_path',
    help="A directory of custom templates",
    default=None)

  parser.add_argument(
    '-k', '--kwargs', 
    dest='kwargs',
    help="A json string or a .json / .yml filepath of custom kwargs",
    default="{}")

  return parser.parse_args()

def main():
  # parse args
  opts = parse_args()
  
  # get current absolute path
  wd = make_abs_path(opts.project_name)

  # insert template
  create_template(opts)

  # chnage directory
  os.chdir(wd)

  # # make virtual environment
  # mkvirtualenv(opts.project_name)

  # initialize git repository
  git_init()
  #workon(opts.project_name)
  print "DONE: Your new python project and git repo have been created in '%s/'" % opts.project_name

if __name__ == '__main__':
  main()
  

