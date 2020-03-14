from dicts import *

def print_init(file):
	print("\\documentclass{article}", file=file)
	print("\\usepackage{graphicx}", file=file)
	print("\\usepackage[margin=0.75in]{geometry}", file=file)
	print("\\usepackage{hyperref}", file=file)
	print("\\usepackage[singlelinecheck=false]{caption}", file=file)
	print("\\setlength{\\parindent}{0pt}", file=file)
	print("\\setlength{\\parskip}{1em}", file=file)
	print("\\date{}", file = file)
	print("\\author{}", file = file)

def handle_font(Node, file):
	for x,y in zip(Node.attr,Node.values):
		if(x.upper()=="SIZE"):
			val = int(y)
			if(val>8):
				val = 8
			if(val<1):
				val = 1
			print("{\\" + font_size[val],file=file,end="")
			return "}"

def handle_anchor(Node,file):
	for x,y in zip(Node.attr,Node.values):
		if(x.upper()=="HREF"):
			link = y
			if(link[0]!='#'):
				print("\\href{"+link+"}{",file=file)
				return "}"
			else:
				link = link.replace('#',"")
				print("\\hyperref["+link+"]{",file=file,end="")
				return "}"
		if(x.upper()=="NAME"):
			link = y
			print("\\label{"+link,file=file,end="")
			return "}"

def handle_table(Node,file):
	for x,y in zip(Node.attr,Node.values):
		border = 0
		if(x.upper() == "BORDER"):
			border = int(y)
	rows = len(Node.children)
	cols = 0
	for x in Node.children:
		cols = max(cols,len(x.children))
	print("\\begin{table}[h!]", file=file)
	for x in Node.children:
		if(x.value!="TR"):
			check_node(x,file)
		else:
			for y in x.children:
				if(y.value!="TH" and y.value!="TD"):
					check_node(y,file)
	row_str = ['||']
	empty_list = []
	for x in range(cols):
		row_str.append('c||')
		empty_list.append(" ")
	row_str = "".join(row_str)
	if(border==0):
		row_str = row_str.replace("||"," ")
	print("\\begin{tabular}{"+row_str+"}",file=file)
	if(border==1):
		print("\\hline",file=file)
		print("\\hline",file=file)
	for x in Node.children:
		if(x.value=="TR"):
			for y in x.children:
				if(y.value=="TH" or y.value=="TD"):
					if(y.value=="TH"):
						print("\\textbf{",file=file, end="")
					for z in y.children:
						check_node(z,file)
					if(y.value=="TH"):
						print("}",file=file, end="")
					if(y!=x.children[-1]):
						print("&",file=file,end="")
				else:
					continue
			for i in range(len(x.children),cols):
				print("& ",file=file,end="")
		else:
			continue
		print("\\\\",file=file)
		if(border==1):
			print("\\hline",file=file)
			print("\\hline",file=file)
	print("\\end{tabular}",file=file)
	print("\\end{table}",file=file)
	return ""

def handle_img(Node,file):
	print("[",file=file, end="")
	added = 0
	for x,y in zip(Node.attr,Node.values):
		if(x.upper()=="WIDTH" or x.upper()=="HEIGHT"):
			if(added!=0):
				print(",",file=file, end="")
			added=1
			print(x.lower() + "=" + y+"pt",file=file,end="")
	print("]",file=file, end="")
	for x,y in zip(Node.attr,Node.values):
		if(x.upper()=="SRC"):
			link = y
			print("{" + link + "}",file=file,end="")
			return ""

def check_node(Node,file):
	if(Node.type=='tree'): #ROOT NODE
		check_node(Node.children[0],file)
		return
	elif(Node.value=='FONT'):
		end = handle_font(Node,file)
	elif(Node.value=='A'):
		end = handle_anchor(Node,file)
	elif(Node.value=='TABLE'):
		end = handle_table(Node,file)
	elif(html2latexdict.get(Node.value,"")=="" and Node.type!='text'):
		end = ""
	elif(Node.type=='starttag'):
		intro = html2latexdict[Node.value]
		if("begin" in intro):
			temp = intro.split("begin")
			end = temp[0] + "end" + temp[1]
			print(intro, file=file,end="")
		else:
			print(intro, file=file, end="")
			end = None
	elif(Node.type=='emptytag'):
		intro = html2latexdict[Node.value]
		print(intro, file=file, end="")
		end = None
	elif(Node.type=='text'):
		text = Node.value
		for x in spec_char.keys():
			text = text.replace(x,spec_char[x])
		print(text, file=file,end="")
		return
	if(Node.value=='BODY'):
		print("\\maketitle",file=file)
	elif(Node.value=='IMG'):
		end = handle_img(Node,file)
	if(end==None):
		print("{", file=file, end="")
	for x in Node.children:
		if(Node.value!='TABLE'):
			check_node(x,file)
	if(end == None):
		print("}", file=file,end="")
	else:
		print(end, file=file,end="")

def parse_tree(tree,file):
	print_init(file)
	check_node(tree,file)