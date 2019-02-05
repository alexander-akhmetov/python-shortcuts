generate-docs:
	python docs.py docs/actions.md


tests:
	tox


release-pypi:
	test -n "$(VERSION)"
	@echo "\033[92mVERSION=$(VERSION)\033[0m"
	@echo "\033[92mStarting tests\033[0m"
	tox

	@echo "\033[92mReleasing python-shortcuts with VERSION=$(VERSION)\033[0m"

	@echo "\033[92mBuilding python-shortcuts\033[0m"
	sed -i '' "s/name='shortcuts'/name='python-shortcuts'/" setup.py
	python setup.py sdist

	@echo "\033[92mBuilding shortcuts\033[0m"
	sed -i '' "s/name='python-shortcuts'/name='shortcuts'/" setup.py
	python setup.py sdist

	@echo "\033[92mUploading...\033[0m"
	twine upload dist/python-shortcuts-$(VERSION).tar.gz
	twine upload dist/shortcuts-$(VERSION).tar.gz
	@echo "\033[92mDone\033[0m"


isort-fix:
	isort -rc shortcuts


docker-build-cli:
	test -n "$(TAG)"
	docker build -t akhmetov/shortcuts-cli:$(TAG) .
