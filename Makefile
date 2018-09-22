generate_docs:
	python src/docs.py docs/actions.md

tests:
	tox


release-pypi:
	test -n "$(VERSION)"
	python setup.py sdist
	twine upload dist/python-shortcuts-$(VERSION).tar.gz
