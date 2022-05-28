def find_anagram(word, anagram):

    if(sorted(word)== sorted(anagram)):
        answer=True
    else:
        answer=False
    return answer
word=input("Enter the first word: ")
anagram=input("Enter the Second word: ")
answer=find_anagram(word,anagram)
print(answer)
print(find_anagram("hello","check"))
print(find_anagram("below","elbow"))