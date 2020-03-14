from lex import *
from utils import *
from node import *

def get_tree(data):
	lex.input(data)
	tree = Node('tree',parent=None,value='Tree')
	currnode = tree
	for tok in iter(lex.token, None):
		if(tok.type=='FILLER' or tok.value.strip()==""):
			continue
		if(tok.type=='STARTTAG'):
			text = tok.value
			tag,attr,values = node_from_tag(text)
			if(tag=="BR" or tag=="IMG"):
				tok.type='EMPTYTAG'
		if(tok.type=='STARTTAG'):
			text = tok.value
			tag,attr,values = node_from_tag(text)
			tempNode = Node('starttag',value=tag, parent=currnode, attr=attr, values = values)
			currnode.children.append(tempNode)
			currnode = tempNode
		if(tok.type=='ENDTAG'):
			text = tok.value
			tag,attr,values = node_from_tag(text)
			if(currnode.value!=tag):
				print("Invalid document Structure")
				exit()
			else:
				currnode = currnode.parent
		if(tok.type=='EMPTYTAG'):
			text = tok.value
			tag,attr,values = node_from_tag(text)
			tempNode = Node('emptytag',value=tag, parent=currnode, attr=attr, values=values)
			currnode.children.append(tempNode)
		if(tok.type=='TEXT'):
			text_value = tok.value
			tempNode = Node('text',value=text_value,parent=currnode)
			currnode.children.append(tempNode)
	return tree