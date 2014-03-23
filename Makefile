clean:
	rm -f *.egg-info
	rm -rf dist build

publish:
	python setup.py sdist bdist_wheel upload

.PHONY: clean publish
