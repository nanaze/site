from typing import Text

import subprocess

def MarkdownToHtml(markdown_str: Text) -> Text:
  proc = subprocess.run(['markdown'], capture_output=True, input=markdown_str, text=True, )
  proc.check_returncode()
  return proc.stdout
