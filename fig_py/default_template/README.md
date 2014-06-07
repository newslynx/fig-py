![travis-img](https://travis-ci.org/{{ github_user }}/{{ project_name }}.svg)
{{ project_name }}
======
_{{ description }}_

## Install
```
mkvirtualenv {{ project_name }}
git clone https://github.com/{{ github_user }}/{{ project_name }}.git
cd {{ project_name }}
pip install -r requirements.txt
pip install .
```

## Test
Requires `nose`
```
nosetests
```
