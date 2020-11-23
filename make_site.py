#!/usr/bin/env python3

import os
import string
import sys

def _ReadTemplate(filename):
  with open(os.path.join('templates', filename)) as f:
    return f.read()

  
def main():
  args = sys.argv[1:]

  assert len(args) == 1, 'Expected one argument, the destination directory'

  template_str = _ReadTemplate('base.html')
  template = string.Template(template_str)
  output = template.substitute({
    # TODO: actually write content
    'content' : 'content'
    })

  # TODO: write to output dir
  print (output)

  
if __name__ == '__main__':
  main()
