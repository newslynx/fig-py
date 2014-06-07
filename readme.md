pyinit
======
`pyinit` is a command line tool for generating skeletons of python packages from a directory of `jinja` templates.

The interface is easy:

```
pyinit -p my-new-project -g my-github-user-name
```

This will initialize a highly-opinionated github repository, with your command line args inserted in relevant places throughout the following directory tree:

```
my-new-project
├── README.md
├── build_docs.sh
├── docs
│   ├── Makefile
│   ├── _static
│   │   └── logo.png
│   ├── _themes
│   │   ├── flask_theme_support.py
│   │   └── kr
│   │       ├── autotoc.html
│   │       ├── layout.html
│   │       ├── relations.html
│   │       ├── sidebarlogo.html
│   │       ├── static
│   │       │   └── flasky.css_t
│   │       └── theme.conf
│   ├── conf.py
│   ├── index.rst
│   └── install.rst
├── requirements.txt
├── setup.py
├── src
│   └── __init__.py
└── tests
    ├── README.md
    ├── __init__.py
    ├── fixtures
    │   └── README.md
    └── tests.py
```

This default template comes with `nose` for testing, `sphinx` for docs (with Kenneth Reitz's Template), 
`travis-ci` for continuous integration and `pandoc` for rendering your markdown README.md on py-pi.

You can build and serve the docs by running `build.sh`.

## Customizing

If you'd like, you can also create your own folder of `jinja` templates and pass it in as follows:
```
pyinit -p my-new-project -g my-github-user-name -t path/to/my-template/
```

You can also pass in a series of custom json key-value pairs if you want to add extra context:
```
pyinit -p my-new-project -g my-github-user-name -t my-template/ -k "{'key1':'value1', 'key2':'value2'}"
```

These values can be inserted anywhere in your custom templates using standard `jinja` syntax:
```
{{ key1 }}, {{ key2 }}
```

Heres the full cli specification:
```
usage: pyinit [-h] [-p PROJECT_NAME] [-g GITHUB_USER] [-a AUTHOR] [-e EMAIL]
              [-d DESCRIPTION] [-t TEMPLATE_PATH] [-k KWARGS]

Initialize a python repository.

optional arguments:
  -h, --help            show this help message and exit
  -p PROJECT_NAME, --project-name PROJECT_NAME
                        The name of your project.
  -g GITHUB_USER, --github-user GITHUB_USER
                        Your github user name.
  -a AUTHOR, --author AUTHOR
                        Your name.
  -e EMAIL, --email EMAIL
                        Your email.
  -d DESCRIPTION, --description DESCRIPTION
                        The projects' description.
  -t TEMPLATE_PATH, --template TEMPLATE_PATH
                        A directory of custom templates
  -k KWARGS, --kwargs KWARGS
                        A json string or a .json / .yml filepath of custom
                        kwargs
```

## Installation
```
pip install pyinit
```

TODO:
* Don't rely on `os.system()`
* create repository on `github`
* activate virtualenv
* link `README.md` -> index.rst for docs.
* webhooks for read the docs / s3 upload for data / binaries.



