import articles
import markdown
import io

from typing import Iterable, Text


def _ReadMarkdownContent() -> Text:
  with open('content/index.md', 'rt') as f:
    return markdown.markdown(f.read())


def MakeIndexPageContent(article_list: Iterable[articles.Article]) -> Text:
  buf = io.StringIO()
  buf.write(_ReadMarkdownContent())
  buf.write('<ul>\n')
  for article in article_list:
    path = '%s.html' % article.name
    buf.write('<li><a href="%s">%s</a></li>' % (path, article.title))
  buf.write('</ul>\n')
  return buf.getvalue()
