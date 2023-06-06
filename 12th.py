sentence = input("Enter Sentence:").split(' ')
d={}
for word in sentence:
    d[word]=sentence.count(word)
print(d)