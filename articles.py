from dataclasses import dataclass
import os


@dataclass
class Article:
  name: str
  content: str


def LoadArticles():
  for filename in os.listdir('articles'):
    full_path = os.path.join('articles', filename)
    with open(full_path, 'rt') as f:
      content = f.read()
      name, _ = os.path.splitext(filename)
      yield Article(name, f.read())
