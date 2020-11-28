from dataclasses import dataclass
from typing import Text

import os
import markdown


@dataclass
class Article:
  name: str
  content: str


def LoadArticles():
  for filename in os.listdir('articles'):
    full_path = os.path.join('articles', filename)
    with open(full_path, 'rt') as f:
      content = f.read()
      name, ext = os.path.splitext(filename)
      if ext == '.md':
        content = markdown.MarkdownToHtml(content)

      yield Article(name, content)
