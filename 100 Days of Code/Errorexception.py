#FileNotFound
# with open("afile.txt") as file:
#     file.read()

# KeyError
# adictionary = {"key":"value"}
# value = adictionary["nonexistkey"]

# IndexError
# fruitlist = ["Apple","Banana","Pear"]
# fruit = fruitlist[3]

# TypeError
# text = "abc"
# print(text + 5)

#try: -> something that might cause an exception
#except: -> kalo ada exception lakuin ini
#else: -> kalo ga ada exception lakuin ini
#finally: -> ini akan dijalankan apapun yang terjadi

#FileNotFound
# try:
#     file = open("afile.txt")
# except:
#     file = open("afile.txt","w")
# coba buka file ini kalo gada, 'except' bikin file afile.txt pake mode = "w"

# try:
#     print("hello")
# except:
#     print("If hello fail i got run")
# finally:
#     raise TypeError("This is an error that I made up.")