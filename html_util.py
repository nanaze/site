import html.parser

from typing import Optional, Text


def ParseTag(content: Text, parsed_tag) -> Optional[Text]:

  contents = []

  class Parser(html.parser.HTMLParser):

    def handle_starttag(self, tag, attrs):
      self.current_tag = tag

    def handle_data(self, data):
      if self.current_tag == parsed_tag:
        contents.append(data)

  parser = Parser()
  parser.feed(content)

  if contents:
    return contents[0]
