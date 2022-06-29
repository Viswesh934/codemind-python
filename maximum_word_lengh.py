def freq(str):
	k=[]
	strl = str.split()
	u= set(strl)
	
	for words in u :
	    k.append(len(words))
	print(max(k))
str =input()
freq(str)