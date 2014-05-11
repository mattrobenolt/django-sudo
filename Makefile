dev:
	pip install -r dev-requirements.txt

test: lint
	py.test --cov sudo --cov-report term-missing

lint:
	flake8 sudo || exit 1

clean:
	rm -rf *.egg-info
	rm -rf *.egg
	rm -rf dist build

publish:
	python setup.py sdist bdist_wheel
	twine upload dist/*

.PHONY: test lint dev clean publish
