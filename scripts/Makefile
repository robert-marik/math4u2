# Makefile pro generování a nasazení webu Math4U2

# Cílové adresáře
SITE_DIR=_site
WWW_DIR=/var/www/html/math4u2

# Výchozí cíl
all: html

# Kompilace HTML
html:
	@echo "🚀 Spouštím generování HTML..."
	python3 compile.py
	@echo "✅ Hotovo: HTML vygenerováno do $(SITE_DIR)/"

# Kopírování na server
www: html
	@echo "🚀 Nasazuji web do $(WWW_DIR)..."
	cp -r $(SITE_DIR)/* $(WWW_DIR)/
	@echo "✅ Nasazení dokončeno."

# Úklid
clean:
	@echo "🚀 Mažu adresář $(SITE_DIR)..."
	rm -rf $(SITE_DIR)
	@echo "✅ Hotovo."

.PHONY: all html www clean