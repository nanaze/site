from dataclasses import dataclass
from typing import Text

import os
import subprocess


@dataclass
class Article:
  name: str
  content: str


def _MarkdownToHtml(markdown_str: Text) -> Text:
  proc = subprocess.run(['markdown'], input=markdown_str, text=True)
  proc.check_returncode()
  return proc.stdout


def LoadArticles():
  for filename in os.listdir('articles'):
    full_path = os.path.join('articles', filename)
    with open(full_path, 'rt') as f:
      content = f.read()
      name, ext = os.path.splitext(filename)
      if ext == '.md':
        content = _MarkdownToHtml(content)

      yield Article(name, content)
