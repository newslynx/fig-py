import os
import sys
import pkg_resources
import json
import yaml
from jinja2 import Template

from util import *

default_tmpl_path = os.path.dirname(
  pkg_resources.resource_filename('fig_py', 'default_template/README.md')
 )
# default_tmpl_path = 'default_template' # for dev purposes

class KwargsLoadError(Exception):
  pass

def load_kwargs(kwargs):

  if kwargs.endswith('.json'):
    try:
      with open(make_abs_path(kwargs), 'rb') as f:
        kwarg_opts = json.load(f)
    except ValueError:
      raise KwargsLoadError(
        'Error loading json file.'
        )

  elif kwargs.endswith('.yml'):
    try:
      with open(make_abs_path(kwargs), 'rb') as f:
        kwarg_opts = json.load(f)

    except ValueError:
      raise KwargsLoadError(
        'Error loading yml file.'
        )
  else:
    try:
      kwarg_opts = json.loads(kwargs)

    except ValueError:
      raise KwargsLoadError(
        'Error parsing json kwargs.'
        )

  return kwarg_opts


def get_readme_tmpl(tmpl_path):
  fp = [
    os.path.join(tmpl_path, fp)
      for fp in os.listdir(tmpl_path) 
        if 'readme.md' in fp.lower()
    ]
  with open(fp[0], 'rb') as f:
    return f.read()


def render_tmpl(tmpl, tmpl_context):
  tmpl = Template(tmpl)
  rendered = tmpl.render(**tmpl_context)
  return rendered

def get_readme_rst(tmpl_path, tmpl_context):

  # get readme and render
  readme_tmpl = get_readme_tmpl(tmpl_path)
  readme = render_tmpl(readme_tmpl, tmpl_context)

  # convert to rst if pandoc is installed.
  try:
    import pypandoc
    readme_rst = pypandoc.convert(readme, 'rst', format='md')

  except (IOError, ImportError):
    readme_rst = """
    {project_name}
    =================
    {description}
    """.format(**tmpl_context)

  return readme_rst

def create_template(opts):

  # get base path
  base_path = make_abs_path(opts.project_name)

  # set template path
  tmpl_path = opts.tmpl_path
  if tmpl_path is None:
    tmpl_path = default_tmpl_path

  # default context
  tmpl_context = {
    "project_name": opts.project_name,
    "github_user": opts.github_user,
    "author": opts.author,
    "email": opts.email,
    "description": opts.description
  }

  # optional context
  kwarg_opts = load_kwargs(opts.kwargs)
  tmpl_context = dict(tmpl_context.items() + kwarg_opts.items())

  # add readme_rst to tmpl_context
  tmpl_context['readme_rst'] = get_readme_rst(tmpl_path, tmpl_context)

  for dir_name, dir_list, file_list in os.walk(tmpl_path.encode('utf-8')):

    # set the path for the destination folder
    dest = dir_name.replace(tmpl_path, base_path)

    # if the source directory doesn't exist in the destination folder,
    # create it
    if not os.path.isdir(dest):
      os.makedirs(dest)

    # copy over files, optionally applying templating
    for filename in file_list:
      # if somehow a DS_Store or pyc gets in here during dev, skip it
      if 'DS_Store' in filename or '.pyc' in filename:
        continue

      old_path = os.path.join(dir_name, filename)
      new_path = os.path.join(dest, filename)
      
      # read in the template file
      tmpl_fh = open(old_path, 'r')
      tmpl = tmpl_fh.read()

      # dont apply templates to flask doc templates, 
      # these will be built later on with sphinx.
      if not old_path.endswith('.html'):

        tmpl = Template(tmpl)
        tmpl = tmpl.render(**tmpl_context)

      tmpl_fh.close()

      # write the file
      with open(new_path, 'w') as fh:
        fh.write(tmpl)
