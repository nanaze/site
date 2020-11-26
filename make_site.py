#!/usr/bin/env python3

from typing import Iterator, Text, Tuple

import os.path
import os
import shutil
import string
import sys

import articles
import index_page
import page_template


def _YieldFiles() -> Iterator[Tuple[Text, Text]]:
  """Iterates files. Pairs of path and contents."""

  yield 'index.html', page_template.FillPage(
      title=None, content=index_page.MakeIndexPageContent())


def _CopyFiles(dest_dir: Text):
  """Copy static files to their destinations."""
  dest_path = os.path.join(dest_dir, 'styles')
  shutil.copytree('styles', dest_path)


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
