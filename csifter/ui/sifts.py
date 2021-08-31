from rich.console import Console
from rich.syntax import Syntax
from rich import print
from rich.panel import Panel

'''
‣ Dipslays results from source analysis
‣ Renders potentially vulnerable code blocks
  as highlighted source code with line numbers
'''

# CONFIG
SYNTAX = 'C'
THEME = 'material' 
console = Console()



def render_block(data):
    block_table = None
    
    snippet = data[1].strip('\n')

    render_snippet = Syntax(snippet, "cpp", theme=THEME, line_numbers=True)
    block_panel = Panel(render_snippet, title=data[0])
    print(block_panel)



def render_blocks(blocks):

    for block in blocks:
      render_block(
        (
          block[0]['name'],
          block[1],           # line number
        )
      )

