def node_from_tag(text):
	clean = text.split("<")[1].split(">")[0]
	if(clean[-1]=='/'):
		clean = clean[:-2]
	elif(clean[0]=='/'):
		clean = clean[1:]
	clean = clean.split()

	tag = clean[0].upper()
	attr = []
	values = []
	i = 0
	while(True and len(clean)>1):
		i = i + 1
		if(i==len(clean)):
			break
		if "=" in clean[i]:
			temp = clean[i].split("=")
			attr.append(temp[0].strip())
			if(temp[1]!=""):
				values.append(temp[1].replace("\"","").replace("\'","").strip())
			else:
				values.append(clean[i+1].replace("\"","").replace("\'","").strip())
				i = i+1
		else:
			attr.append(clean[i])
			temp = clean[i+1].split("=")
			if(temp[1]!=""):
				values.append(temp[1].replace("\"","").replace("\'","").strip())
				i = i+1
			else:
				values.append(clean[i+2].replace("\"","").replace("\'","").strip())
				i = i+2
	return tag,attr,values