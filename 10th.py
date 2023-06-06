x=input("Enter String:")
vowel=0
conso=0
blank=0
for char in x:
    if char in "aeiouAEIOU":
        vowel+=1
    elif char==' ':
        blank+=1
    elif char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        conso+=1
print("Vowel:",vowel)
print("Consonent:",conso)
print("Blank Spaces:",blank)

