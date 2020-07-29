word=input("")
def most_frequent(word):
    d = dict()
    
    for i in word:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d
    
print (most_frequent(word))
d=most_frequent(word)




l=list(reverse_d.items())
l.sort(reverse=True) #sort in reverse order
print('Decresing order of frequency is',l)
