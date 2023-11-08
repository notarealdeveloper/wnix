all:
	python -m build --sdist

install: all
	pip install dist/*.tar.gz

uninstall:
	pip uninstall wnix

clean:
	rm -rv dist/ src/*.egg-info
