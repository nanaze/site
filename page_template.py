import os
import string

from typing import Optional, Text

_SITE_NAME = 'nanaze.github.io'


def _ReadTemplate(filename: Text) -> Text:
  with open(os.path.join('templates', filename), 'rt') as f:
    return f.read()


def FillPage(title: Optional[Text] = None, content: Optional[Text] = None) -> Text:
  template_str = _ReadTemplate('base.html')
  template = string.Template(template_str)

  if title:
    title = '%s | %s' % (_SITE_NAME, title)
  else:
    title = _SITE_NAME

  # TODO: add title to template
  return template.substitute({'content': content})
