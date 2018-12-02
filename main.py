import nltk

f = open("textholder.txt")
text = f.read()
f.close()
sentences = nltk.sent_tokenize(text)
for i in sentences:
    print(i, end=" ")