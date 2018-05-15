NAME    = $(shell cat bundle.json | sed -n 's/"name"//p' | tr -d '", :')
VERSION = $(shell cat bundle.json | sed -n 's/"version"//p' | tr -d '", :')

PROJECT = sanji-bundle-$(NAME)

DISTDIR = $(PROJECT)-$(VERSION)
ARCHIVE = $(CURDIR)/$(DISTDIR).tar.gz

SANJI_VER   ?= 1.0
INSTALL_DIR = $(DESTDIR)/usr/lib/sanji-$(SANJI_VER)/$(NAME)
STAGING_DIR = $(CURDIR)/staging
PROJECT_STAGING_DIR = $(STAGING_DIR)/$(DISTDIR)

TARGET_FILES = \
	bundle.json \
	data/{{cookiecutter.project_slug}}.json.factory \
	index.py \
	requirements.txt \
	{{cookiecutter.project_slug}}/__init__.py \
	{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}.py
DIST_FILES= \
	$(TARGET_FILES) \
	Makefile \
	README.md \
	tests/__init__.py \
	tests/requirements.txt \
	tests/test_index.py
INSTALL_FILES=$(addprefix $(INSTALL_DIR)/,$(TARGET_FILES))
STAGING_FILES=$(addprefix $(PROJECT_STAGING_DIR)/,$(DIST_FILES))

all:

clean:
	@rm -rf ./data/*.json
	@rm -rf ./data/*.json.backup
	@find ./ -name *.pyc | xargs rm -f
	@rm -rf $(DISTDIR)*.tar.gz $(STAGING_DIR)

distclean: clean

pylint:
	flake8 -v index.py ./{{cookiecutter.project_slug}}

test:
	nosetests --with-coverage --cover-package=index,{{cookiecutter.project_slug}} --cover-erase -v

dist: $(ARCHIVE)

$(ARCHIVE): distclean $(STAGING_FILES)
	@mkdir -p $(STAGING_DIR)
	cd $(STAGING_DIR) && \
		tar zcf $@ $(DISTDIR)

$(PROJECT_STAGING_DIR)/%: %
	@mkdir -p $(dir $@)
	@cp -a $< $@

install: $(INSTALL_FILES)

$(INSTALL_DIR)/%: %
	@mkdir -p $(dir $@)
	@cp -a $< $@

uninstall:
	-rm $(addprefix $(INSTALL_DIR)/,$(TARGET_FILES))

.PHONY: clean dist pylint test
