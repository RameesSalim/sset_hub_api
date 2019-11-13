data =[[]]
json = {}
for i in data:
  if(float(i[5])>75):
    snip = (float(i[4])-(float(i[1])*.75))/.75
    a = isinstance(snip, float)
    if(a ==True):
      snip=(int(snip)+1)
    print("You can snip ",i[0],"for",snip)
  elif(i[5]==75):
    print("You can Snip",i[0],"0 hours")

  else:
    snip = ((.75*float(i[1]))-float(i[4]))/.25
    a = isinstance(snip, float)
    if(a ==True):
      snip=(int(snip)+1)
    print("You need to attend",i[0],"for",snip)
