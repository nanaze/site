# This script is meant to be invoked by Makefile

set -ex

cd out
git init
git add .
git commit -m 'set content'
git remote add origin git@github.com:nanaze/nanaze.github.io.git
git push --set-upstream origin main --force

