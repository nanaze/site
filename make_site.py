#!/usr/bin/env python3

from typing import Text

import os.path
import os
import shutil
import string
import sys

import articles
import index_page


def _YieldFiles():
  template_str = _ReadTemplate('base.html')
  template = string.Template(template_str)
  content = template.substitute({'content': index_page.MakeIndexPageContent()})

  yield 'index.html', content


def _CopyFiles(dest_dir: Text):
  dest_path = os.path.join(dest_dir, 'styles')
  shutil.copytree('styles', dest_path)


def _ReadTemplate(filename):
  with open(os.path.join('templates', filename)) as f:
    return f.read()


def main():
  args = sys.argv[1:]

  assert len(args) == 1, 'Expected one argument, the destination directory'

  out_dir = args[0]

  for path, content in _YieldFiles():
    path = os.path.join(out_dir, path)
    with open(path, 'wt') as f:
      f.write(content)

  _CopyFiles(out_dir)


if __name__ == '__main__':
  main()
