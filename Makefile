dev:
	pip install -e .
	pip install "file://`pwd`#egg=django_sudo[tests]"

test: lint
	py.test -x

lint:
	flake8 django_sudo || exit 1

clean:
	rm -rf *.egg-info
	rm -rf *.egg
	rm -rf dist build

publish:
	python setup.py sdist bdist_wheel upload

.PHONY: test lint dev clean publish
