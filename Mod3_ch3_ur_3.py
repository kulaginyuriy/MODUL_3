def chislo(cifra):
    cifra = map(str, cifra)
    cifra = sorted(cifra, key=lambda x: x * 3 , reverse=True)
    return ''.join(cifra)

print(chislo([56,9,11,2]))