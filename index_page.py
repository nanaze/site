import articles
import io

from typing import Text


def MakeIndexPageContent() -> Text:
  buf = io.StringIO()
  buf.write('<ul>\n')
  for article in articles.LoadArticles():
    buf.write('<li>%s</li>' % article.name)
  buf.write('</ul>\n')
  return buf.getvalue()
