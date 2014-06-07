import os
import subprocess

# helpers for making a virtul environment
class VirtualEnvError(Exception):
  pass

class InitError(Exception):
  pass

def exec_quiet(args):
  # print args
  # subprocess.call(args, shell=True)
  os.system(" ".join(args))

def mkvirtualenv(project_name):
  """
  TODO: git this to work
  """
  if not os.getenv('WORKON_HOME'):
    raise VirtualEnvError(
      "It looks like you don't have virtualenvwrapper installed."
      )
  # mkvirtualenv
  exec_quiet(["source", "/usr/local/bin/virtualenvwrapper.sh"])
  exec_quiet(["mkvirtualenv", project_name])

def workon(project_name):
  # exec_quiet(["source", "/usr/local/bin/virtualenvwrapper.sh"])
  exec_quiet(["workon", project_name])

def git_init():
  exec_quiet(["git", "init"])
  exec_quiet(["git", "add", "."])
  exec_quiet(["git", "commit", "-m", "'initial commit'"])

def make_abs_path(fn):
  return os.path.abspath(os.path.join(os.getcwd(), fn))




