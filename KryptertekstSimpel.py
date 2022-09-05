alfabetet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z','Æ','Ø','Å']
noegle =    ['Å', 'P', 'E', 'S', 'U', 'F', 'L', 'X', 'K', 'T', 'O', 'A', 'N', 'Ø', 'Y', 'H', 'I', 'M', 'Æ', 'C', 'V', 'B', 'J', 'Q', 'R', 'Z', 'G', 'D']


def kryptertegn(tegn):
    index = alfabetet.index(tegn)
    return noegle[index]


with open("IkkeKrypteretTekst", encoding="utf8") as Text:
    for line in Text:
        for tegn in line:
            if tegn in noegle:
                encrypt = noegle[alfabetet.index(tegn.capitalize())]
                print(encrypt, end="")
            if tegn not in noegle:
                noegle.append(tegn.capitalize())
                alfabetet.append(tegn.capitalize())
                encrypt = noegle[alfabetet.index(tegn.capitalize())]
                print(encrypt, end="")