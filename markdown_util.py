import markdown

def to_html(content : str) -> str:
  return markdown.markdown(content, extensions=['footnotes'])