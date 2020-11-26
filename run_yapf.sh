#!/bin/bash
#
# Run YAPF on Python sources 

set -ex

cd "$(dirname "$0")"

find . -type f -name "*.py" | xargs yapf -i --style style.yapf 
