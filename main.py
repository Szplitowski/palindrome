def palin(word):
    backw = ''.join(reversed(word))
    if backw == word:
        return True
    return False
    
word = "kajak"
yes = palin(word)

if yes:
    print("To słowo jest palindormem")
else:
    print("To słowo nie jest palindormem")
