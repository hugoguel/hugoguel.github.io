.PHONY: build

PYTHON ?= python
HOST    = 0.0.0.0
PORT    = 3000
BUILDIR = /var/www/html
BRAND   = hugoguel

install:
	cat requirements/*.txt > requirements.txt

	pip install -r requirements.txt

	bundler install

build:
	$(PYTHON) -B -m build

	bundle exec jekyll build

	# sudo cp -R _site/* $(BUILDIR)/$(BRAND)

serve:
	bundle exec jekyll serve --host=$(HOST) --port=$(PORT)

clean:
	find . | grep -E "__pycache__" | xargs rm -rf

	rm -rf _site .sass-cache _config.yml

	clear

all:
	make clean install build serve
