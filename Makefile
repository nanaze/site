OUTPUT_DIR = out

site : clean
	# make output directory
	mkdir $(OUTPUT_DIR)

	# run generation script
	./make_site.py $(OUTPUT_DIR)

clean :
	rm -rf $(OUTPUT_DIR)

mypy:
	find . -type f -name "*.py" | xargs mypy
