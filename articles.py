from dataclasses import dataclass
from typing import Text

import os
import markdown_util
import html_util


@dataclass
class Article:
  name: str
  title: str
  content: str


_ARTICLES_DIR_PATH = 'content/articles'

_EXTENSIONS = frozenset(['.md', '.html'])


def _ParseTitle(html_content: Text) -> Text:
  for tag in ['title', 'h1']:
    title = html_util.ParseTag(html_content, tag)
    if title:
      return title

  raise AssertionError('Could not find title')


def LoadArticles():
  for filename in os.listdir(_ARTICLES_DIR_PATH):
    full_path = os.path.join(_ARTICLES_DIR_PATH, filename)
    with open(full_path, 'rt') as f:
      content = f.read()
      name, ext = os.path.splitext(filename)

      # ignore emacs temp files etc
      if ext not in _EXTENSIONS:
        continue

      if ext == '.md':
        content = markdown_util.to_html(content)

      yield Article(name, _ParseTitle(content), content)
