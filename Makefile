help:
	@echo "    dev"
	@echo "        Initialise virtualenv and dev requirements"
	@echo "    init"
	@echo "        Install requirements"
	@echo "    test"
	@echo "        Run tests"

dev:
	sudo apt-get install python3-venv
	python3 -m venv venv
	printf '#!/bin/bash\nvenv/bin/pip3 "$$@"' > pip3
	chmod +x pip3
	printf '#!/bin/bash\nvenv/bin/python3 "$$@"' > python3
	chmod +x python3
	./pip3 install --upgrade pip
	./pip3 install -r requirements-dev.txt
	./pip3 install -r requirements.txt

install:
	pip3 install -r requirements.txt

test:
	nosetests tests