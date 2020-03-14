from node import *
from lex import *
from utils import *
import ply.yacc as yacc

def p_document(p):
	'''document : 
				| FILLER document
				| COMMENT document
				| DOCTYPE document
				| start document
				| end document
				| empty document
				| text document
				| ENDFILE
				'''
	try:
		if(p[1].type == 'starttag'):
			p[1].children.append(p[2])
			p[0] = p[1]
		elif(p[1].type == 'endtag'):
			p[1].parent.children.append(p[2])
			p[0] = p[1].parent
		elif(p[1].type=='emptytag'):
			p[1].parent.children.append(p[2])
			p[0] = p[1].parent
		elif(p[1].type=='text'):
			p[2].parent.children.append(p[1])
			p[0] = p[2].parent
	except:
		try:
			p[0] = p[2]
		except:
			p[0] = Node('endtag')
def p_start(p):
	'''start : STARTTAG
			'''
	try:
		text = p[1]
		tag,attr,values = node_from_tag(text)
		p[0] = Node('starttag',value=tag, attr=attr, values=values)
	except:
		p[0] = Node('starttag',value=tag, attr=attr, values=values)
def p_end(p):
	'''end : ENDTAG
			'''
	try:
		text = p[1]
		tag,attr,values = node_from_tag(text)
		p[0] = Node('endtag',value = tag)
	except:
		p[0] = Node('endtag',value = tag)
def p_empty(p):
	'''empty : EMPTYTAG
			'''
	try:
		text = p[1]
		tag,attr,values = node_from_tag(text)
		p[0] = Node('emptytag',value=tag, attr=[(attr,values)])
	except:
		p[0] = Node('emptytag',value=tag, attr=[(attr,values)])
def p_text(p):
	'''text : TEXT
			'''
	try:
		p[0] = Node('text',value=p[1])
	except:
		p[0] = Node('text',value=p[1])

def p_error(p):
	print("Syntax error")

yacc.yacc(debug=0, write_tables=0)