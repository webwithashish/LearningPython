# myfile = open("my_file.txt", 'r')
# print(myfile.read())
# print(myfile.read(4))
# print(myfile.readline())
# print(myfile.readline(3))
# myfile = open("D:\#Full Stack developer\#PROGRAMMING TECH\Python", "r")
# print(myfile.read())
"""f = open("my_file.txt", 'r')
jf = f.read()
print(f"this is the actual length of the string with including the spaces:\t {len(jf)} ")
jf = jf.split()
jf = "".join(jf)
print(f"the string without spaces:\t {jf}")
print(f"the total letters in the file= \t{len(jf)}")
vowel = 0
consonant = 0
space = 0
for i in jf:
    if i.lower() in ["a", "e", "i", "o", "u"]:
        vowel += 1
    else:
        consonant += 1
print(f"vowels count =\t {vowel}")
print(f"consonant count =\t {consonant}")"""

"""# this is the write mode it will delete all the existing data and write all new
myfile = open("my_file.txt", "w")
myfile.write(" hey this file is over written by using write mode")

# this is append mode for adding a new data in the file
myfile = open("my_file.txt", "a")
myfile.write("\nhey this file is over written by using write mode")"""

f = open("my_file.txt", 'r')
jf = f.read()
print(f"the actual length with including the spaces:\t {len(jf)} ")
jf = jf.split()
jf = "".join(jf)
print(f"the string without spaces:\t {jf}")
print(f"the total letters in the string = \t{len(jf)}")
vowel = 0
consonant = 0
space = 0
punctuation = 0
for i in jf:
    if i.lower() in ["a", "e", "i", "o", "u"]:
        vowel += 1
    elif i == "," or i == ".":
        punctuation += 1
    else:
        consonant += 1
print(f"vowels count =\t {vowel}")
print(f"consonant count =\t {consonant}")
print(f"punctuation count =\t{punctuation}")
