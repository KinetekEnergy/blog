# Configuration, override port with usage: make PORT=4200
PORT ?= 4100
REPO_NAME ?= studentCSA
LOG_FILE = /tmp/jekyll$(PORT).log

SHELL = /bin/bash -c
.SHELLFLAGS = -e # Exceptions will stop make, works on MacOS

# Phony Targets, makefile housekeeping for below definitions
.PHONY: default server issues convert clean stop

# List all .ipynb files in the _notebooks directory
NOTEBOOK_FILES := $(shell find _notebooks -name '*.ipynb')

# Specify the target directory for the converted Markdown files
DESTINATION_DIRECTORY = _posts
MARKDOWN_FILES := $(patsubst _notebooks/%.ipynb,$(DESTINATION_DIRECTORY)/%.md,$(NOTEBOOK_FILES))

# Call server, then verify and start logging
default: server
	@echo "Terminal logging starting, watching server..."

# Start the local web server
server: stop convert
	@echo "Starting server..."
	@@bundle exec jekyll s
	@@until [ -f $(LOG_FILE) ]; do sleep 1; done

# Convert .ipynb files to Markdown with front matter
convert:
	@python3 scripts/convert_notebooks.py
  
# Clean up project derived files, to avoid run issues stop is dependency
clean: stop
	@echo "Cleaning converted IPYNB files..."
	@find _posts -type f -name '*.md' -exec rm {} +
	@echo "Removing empty directories in _posts..."
	@while [ $$(find _posts -type d -empty | wc -l) -gt 0 ]; do \
		find _posts -type d -empty -exec rmdir {} +; \
	done
	@echo "Removing _site directory..."
	@rm -rf _site


# Stop the server and kill processes
stop:
	@echo "Stopping server..."
	@# kills process running on port $(PORT)
	@@lsof -ti :$(PORT) | xargs kill >/dev/null 2>&1 || true
