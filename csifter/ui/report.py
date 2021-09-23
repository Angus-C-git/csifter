from rich.console import Console, RenderGroup
from rich.syntax import Syntax
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.markdown import Markdown

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
	""" render the potentially vulnerable code block """
	snippet = data[2] 
	title = data[0]['name']
	description = data[0]['description']
	block_type = data[0]['type']
	

	# change the panel outline for
	# warnings and detections
	block_border = 'yellow' if block_type == 'warning' else 'red1'

	code_snippet = Syntax(
						snippet, 
						SYNTAX, 
						theme=THEME, 
						line_numbers=True, 
						start_line=data[1]
					)

	description_txt = Markdown(
			f""" ## Explanation \n {description} """,
			inline_code_lexer=SYNTAX,
			inline_code_theme=THEME,
		)
	
	components = RenderGroup(
					code_snippet,
					description_txt
				)
	
	block = Panel(
			components,
			title=f'[b white]{title}',
			width=60,
			border_style=block_border
		)

	# render
	print('\n')
	print(block)



def render_report(blocks):
	""" 
	render the blocks that
	make up the audit report	
	"""
	for block in blocks:
	  render_block(
		(
		  block[0],		# signature 
		  block[1],     # line number
		  block[2],		# line
		)
	  )

