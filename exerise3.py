words = ['this' , 'is', 'a', 'sentence', 'word' ,'.']

def swapwords( array):
    x= 0 # leftside index
    y = len(array)-1 #rightside index
    while x <=y:
        array[x], array[y] = array[y], array[x]
        x=x+1
        y=y-1
    print(array)


def swapletters(array):
    n=0 #index
    for word in array:
        wordlist=list(word)
        x= 0 # leftside index
        y = len(wordlist)-1 #rightside index
        while x <=y:
            wordlist[x], wordlist[y] = wordlist[y], wordlist[x]
            x=x+1
            y=y-1
        backword="".join(wordlist)
        
        array[n]=backword
        n+=1
    print(array)
swapwords(words)
swapletters(words)
