from invoke import run as _run, task
from functools import partial
import re

# Always echo out the commands
run = partial(_run, echo=True, pty=True)


@task
def lint(verbose=False):
    "Run flake8 linter"
    run('flake8 sudo {0}'.format('-v' if verbose else ''))


@task('lint')
def test(verbose=False):
    "Run tests using py.test"
    run('py.test --cov sudo --cov-report term-missing {0}'.format('-v' if verbose else ''))


@task
def clean():
    "Clean working directory"
    run('rm -rf *.egg-info *.egg')
    run('rm -rf dist build')


@task
def release():
    "Cut a new release"
    with open('setup.py') as f:
        setup = f.read()

    version = run('python setup.py --version').stdout.strip()
    assert version, 'No version found in setup.py?'

    print('### Releasing new version: {0}'.format(version))
    run('git tag {0}'.format(version))
    run('git push --tags')

    run('python setup.py sdist bdist_wheel')
    run('twine upload dist/*')
