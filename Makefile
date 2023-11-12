build:
	python -m build

install: build
	pip install dist/*.tar.gz

develop:
	pip install -e .

uninstall:
	pip uninstall Bin

clean:
	rm -rv dist/ src/*.egg-info
