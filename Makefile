PKG_NAME=pdir-athesto

build:
	python3 -m build

clean-build:
	rm -rf dist/

push-test:
	python3 -m twine upload --repository testpypi dist/*

push-main:
	python3 -m twine upload --repository pypi dist/*


install-test:
	pip install --no-build-isolation -i https://test.pypi.org/simple/ --upgrade -I $(PKG_NAME)
	pip3 list | grep $(PKG_NAME)

install-main:
	pip install --upgrade -I $(PKG_NAME)
