dev:
	pip install -e .
	pip install "file://`pwd`#egg=django_sudo[tests]"

clean:
	rm -f *.egg-info
	rm -rf dist build

publish:
	python setup.py sdist bdist_wheel upload

.PHONY: dev clean publish
