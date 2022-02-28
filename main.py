print("~WELCOME~")
file_name=input("Enter file name")
file = open(file_name,"r")

word = ["stupid","idiot","mad","nonsense","repeat","dumb","cool","sober"]

s = " "
# Here we will the each line of list into elements of list
def add(file):
    count = 0
    L = file.readlines()
    for i in L:
        L2 = i.split()
        # The split() method splits a string into a list.
        list = [x.lower() for x in L2]
        # Here it will we convert each word into lower case
        for n in word:
            if n in list:
                # Here the list will iterate over the the each word of the document
                print(("Sorry you cannot send your document further there are mistakes that needs to be changed\n").upper())
                print(n, ":", "This word is found in line no.", count, ":", i)
                count = count + 1

a=add(file)

print(a)

# file=input("plese enter a file name")
# d={}
# with open(file) as fhand:
#     lcount=0
#     wcount=0
#     ccount=0
#     for line in fhand:
#         lcount+=1
#         ccount+=len(line)
#         ls=line.split()
#         for word in ls:
#             if(word not in d.keys()):
#                 d[word]=1
#             else:
#                 d[word]=d[word]+1
#         wcount+=len(ls)
# print(lcount)
# print(ccount)
# print(wcount)
# print(d)

# itemsMaxValue=max(d.items(),key=lambda x:x[1])
#
# listofkeys=list()
# for key,value in d.items():
#     if value == itemsMaxValue[1]:
#         listofkeys.append(key)
# print("words mmost frequently used ",listofkeys)
# fhand.close()