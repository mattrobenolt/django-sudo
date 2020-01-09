from invoke import run as _run, task
from functools import partial

# Always echo out the commands
run = partial(_run, echo=True, pty=True)


files = "sudo tests *.py"


@task
def lint(c, verbose=False):
    "Run flake8 linter"
    run("flake8 %s %s" % (files, "-v" if verbose else ""))
    run("black --check %s" % files)


@task
def format(c):
    "Run black"
    run("black %s" % files)


@task
def test(c, verbose=False):
    "Run tests using py.test"
    run("py.test --cov sudo --cov-report term-missing %s" % ("-v" if verbose else ""))


@task
def clean(c):
    "Clean working directory"
    run("rm -rf *.egg-info *.egg")
    run("rm -rf dist build")


@task(clean)
def release(c):
    "Cut a new release"
    version = run("python setup.py --version").stdout.strip()
    assert version, "No version found in setup.py?"

    print("### Releasing new version: %s" % version)
    run("git tag %s" % version)
    run("git push --tags")

    run("python setup.py sdist bdist_wheel")
    run("twine check dist/*")
    run("twine upload -s dist/*")
