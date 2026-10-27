word = input()
for i in range(len(word)-1,-1,-1):
    for j in range(i+1):
        print(word[j], end="")
    print()