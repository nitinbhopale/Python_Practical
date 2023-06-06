sentence = input("Enter Sentence:").split(' ')
list =[]
for word in sentence:
    if word not in list:
        list.append(word)
list.sort()
print(list)
    