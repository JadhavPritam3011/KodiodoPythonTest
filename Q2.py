# Q.2). Write a program to input string and print the count of
#       vowels and consonants in the string.


def Vowels_and_Consonants(string):
    vowels="aeiouAEIOU"
    consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    vowels_count=0
    consonants_count=0

    for i in string:
        if i in vowels:
            vowels_count += 1
        elif i in consonants:
            consonants_count += 1
    
    return vowels_count, consonants_count    
user=input("Enter a String:")
vowels_count,consonants_count=Vowels_and_Consonants(user)

print(vowels_count,"Number of vowels is present in the string")
print(consonants_count,"Number of consonants is present in the string")












