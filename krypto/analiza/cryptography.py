def lookout(text, word="cryptography"):
    counter = 0
    slowo = ''
    for i in range(len(text)):
        if text[i] != ' ':
            slowo += text[i]
            counter += 1
        elif counter == len(word):
            print(slowo)
            slowo = ''
            counter = 0
        else:
            slowo = ''
            counter = 0

# Tekst z zastąpionymi literami odpowiadającymi znakowi spacji
text = "WQYZ  WBCW  YZ  FBBTBT  WG  PIZZ  WQB  DL#PWGRLIPQ#  ZMHXBDW  AGL  YW  DGFWIYFZ  I  TBZDLYPWYGF  GA  I  DL#PWGRLIPQ#  WIZO  AGL  WQB  RLGMP  NMBHBD"

lookout(text)