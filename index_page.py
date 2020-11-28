import articles
import markdown
import io

from typing import Text

def _ReadMarkdownContent() -> Text:
  with open('content/index.md', 'rt') as f:
    return markdown.MarkdownToHtml(f.read())

def MakeIndexPageContent() -> Text:
  buf = io.StringIO()
  buf.write(_ReadMarkdownContent())
  buf.write('<ul>\n')
  for article in articles.LoadArticles():
    buf.write('<li>%s</li>' % article.name)
  buf.write('</ul>\n')
  return buf.getvalue()
