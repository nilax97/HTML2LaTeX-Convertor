from anytree import Node, RenderTree

class Node:
	def __init__(self,type=None,parent=None,children=None,value=None,attr=[],values=[]):
		self.type = type
		if children:
			self.children = children
		else:
			self.children = []
		if parent:
			self.parent = parent
		else:
			self.parent = None
		self.attr = attr
		self.values = values
		self.value = value


def write_tree(root,file):
	for pre, fill, node in RenderTree(root):
		print(pre,node.value,end="",file=file)
		if(len(node.attr)>0):
		 	print(" --> ",end="",file=file)
		 	for x,y in zip(node.attr,node.values):
		 		print("("+x+","+y+")",end="",file=file)
		print("",file=file)