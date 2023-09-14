# Makefile for UwUifier

INSTALL_DIR = ~/.local/bin
CONFIG_DIR = ~/.config/uwuifier
SCRIPT_NAME = uwuifier.py
CONFIG_FILE = default_config.json

install:
	@echo "Installing UwUifier..."
	@mkdir -p $(INSTALL_DIR)
	@mkdir -p $(CONFIG_DIR)
	@python3 -m pip install -r requirements.txt
	@ln -s $(CURDIR)/$(SCRIPT_NAME) $(INSTALL_DIR)/uwuifier
	@cp $(CONFIG_FILE) $(CONFIG_DIR)/config.json
	@echo "UwUifier is now installed in $(INSTALL_DIR)"
