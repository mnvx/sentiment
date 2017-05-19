help:
	@echo "    dev"
	@echo "        Initialise virtualenv and dev requirements"
	@echo "    init"
	@echo "        Install requirements"
	@echo "    test"
	@echo "        Run tests"

dev:
	sudo apt-get install python3-virtualenv
	mkdir -p venv
	echo "Virtualenv directory" > venv/README
	virtualenv -p python3.6 --no-site-packages --prompt="(sentiment)" venv/sentiment
	./activate
	pip install -r requirements-dev.txt

init:
	pip install -r requirements.txt

test:
	nosetests tests