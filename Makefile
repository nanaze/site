OUTPUT_DIR = out

site : clean mypy
	# make output directory
	mkdir $(OUTPUT_DIR)

	# run generation script
	./make_site.py $(OUTPUT_DIR)

clean :
	rm -rf $(OUTPUT_DIR)

mypy:
	# Checking Python types with mypy
	find . -type f -name "*.py" | xargs mypy

push_site : site
	# Push to github
	cd out
	git init
	git add .
	git commit -m 'set content'
	git remote add origin git@github.com:nanaze/nanaze.github.io.git
	git push --set-upstream origin master --force
	popd
