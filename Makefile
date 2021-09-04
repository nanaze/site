OUTPUT_DIR = out

site : clean mypy
	# make output directory
	mkdir $(OUTPUT_DIR)
	.venv/bin/python3 make_site.py $(OUTPUT_DIR)

clean :
	rm -rf $(OUTPUT_DIR)
	rm -rf .venv

mypy: venv
	# Checking Python types with mypy
	find . -type f -name "*.py" | grep \.venv -v | xargs .venv/bin/python3 -m mypy

venv:
	python3 -m venv .venv
	.venv/bin/python3 -m pip install -r requirements.txt

push_site : site
	# Push to github
	bash push_site.sh
