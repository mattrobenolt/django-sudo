clean:
	rm -f *.egg-info
	rm -rf dist

publish:
	python setup.py sdist bdist_wheel upload

.PHONY: clean publish
