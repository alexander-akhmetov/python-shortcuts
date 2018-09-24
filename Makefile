generate_docs:
	python docs.py docs/actions.md

tests:
	tox


release-pypi:
	test -n "$(VERSION)"
	python setup.py sdist
	twine upload dist/python-shortcuts-$(VERSION).tar.gz


isort-fix:
	isort -rc shortcuts
