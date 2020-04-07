import re



def search(messageText):
   lineByLine =re.split("\n|,", messageText)
   lines= [x for x in lineByLine if x !=""] #removing emptystrings
   dict ={}
   for i in lines:
       a=i.split(":")
       dict[a[0]]=a[1]
   print(dict)
   return(dict)




