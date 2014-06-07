import os
import subprocess

# helpers for making a virtul environment
class VirtualEnvError(Exception):
  pass

class InitError(Exception):
  pass

def call(args, shell=False):
  subprocess.Popen(args, shell=shell)

def mkvirtualenv(project_name):
  """
  TODO: git this to work
  """
  if not os.getenv('WORKON_HOME'):
    raise VirtualEnvError(
      "It looks like you don't have virtualenvwrapper installed."
      )
  # mkvirtualenv
  call(["source", "/usr/local/bin/virtualenvwrapper.sh"])
  call(["mkvirtualenv", project_name], shell=True)

def workon(project_name):
  # exec_quiet(["source", "/usr/local/bin/virtualenvwrapper.sh"])
  call(["workon", project_name], shell=True)

def git_init():
  call(["git", "init"])
  call(["git", "add", "."])
  call(["git", "commit", "-m", "'initial commit'"])

def make_abs_path(fn):
  return os.path.abspath(os.path.join(os.getcwd(), fn))

