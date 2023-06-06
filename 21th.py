def removeDuplicate(sentence):
    list =[]
    for word in sentence:
        if word not in list:
            list.append(word)
    list.sort()
    return list

print(removeDuplicate(input("Enter Sentence:").split(' ')))
    