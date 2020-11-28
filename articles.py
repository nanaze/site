from dataclasses import dataclass
from typing import Text

import os
import markdown


@dataclass
class Article:
  name: str
  content: str


_ARTICLES_DIR_PATH = 'content/articles'


def LoadArticles():
  for filename in os.listdir(_ARTICLES_DIR_PATH):
    full_path = os.path.join(_ARTICLES_DIR_PATH, filename)
    with open(full_path, 'rt') as f:
      content = f.read()
      name, ext = os.path.splitext(filename)
      if ext == '.md':
        content = markdown.MarkdownToHtml(content)

      yield Article(name, content)
