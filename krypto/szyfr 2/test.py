def create_matrix(text, cols=95, rows=18):
    # Remove any line breaks in the text
    text = text.replace("\n", "")

    # Ensure the text is long enough to fill the matrix
    if len(text) < cols * rows:
        raise ValueError("The text is too short to fill the matrix.")

    # Create the matrix by splitting the text into rows of 'cols' length
    matrix = [list(text[i * cols: (i + 1) * cols]) for i in range(rows)]

    return matrix


# Example usage
text = """thequickbrownfoxjumpsoverthelazydogagainandagaintherearesomanythingstoseeintheworldbutthefoxfindsjoyinrunningfreelythroughfieldsofgreenwiththedaysunshiningbrightandtheskyblueabovethetreesstandtallandthebirdssingsongsasitlistensquietlytheworldaroundisvibrantaliveandteemingwithenergythisisaworldthatweliveinfullofwondersbigandsmallitseemsthatthereisalwayssomethingnewaroundthecornerwaitingforthecurioustoexploreandwhenthenightrisesandthestarscometolightthefoxrestsundertheclearskywaitingforthechancetorunagainatdawntheresalwaysanotherdaytoseekadventuresandtosharejoythequickbrownfoxdoesnotstopitmovesforwardrelentlesslythroughthenightanddayrelivingthosewonderfulmomentsthatkeepitmovingsteadilyforwardforeverandevertheresnobetterjoythanthisitgoesonwithagreateagernesstofinditsnextdestinationandtoembracelifeonceagainjustlikethedaybeforekryptografiaisasecretartthequickbrownfoxloveslearningnewwaysitwandersthroughvariousforestsseekingwisdomhiddenamongthetreesandtheshadowsoflostpathwaysthereisasecretincrypticmessagesencryptedthroughouttheworldknownaskryptografiathismysteriouscraftholdsanswersfromancientdaysandmodernmindsthefoxwondersifthispowerofkryptografiasecretlyshapestheworldarounditwithunseenhandsonedaynotherfoxappearedonewhoskillfullyunraveledthemostcomplexofcodewordsbringingdeeperunderstandingoftheworldcryptographywasnottheenditwasjustthebeginningofthejourneythroughwhichthefoxfoundevenmoresignificanttruthslatentinplainviewsuchthattruthislayeredhiddenineverythingweknowforeverythoughtandactioncanbeasecretcodeneedinguncoveringtounlockthedeepesttruthscontinuingitsjourneythefoxlearnedtoseetheworldnotjustasitisbutasithasthepotentialtobeandthroughthepowerofkryptografiainitsmentaltoolkititcoulddecodethemysteriesoftheuniverseatlasttheresnoendtothemindseekinganddiscoveringmakingcryptographythefoxfavorite"""

matrix = create_matrix(text)

def encryption(matrix, col=95, row=18):
    zaszyfrowane = ""

    # Wypisuję wszystkie kolumny po kolei
    for i in range(col):
        for j in range(row):
            zaszyfrowane += matrix[j][i]

    return zaszyfrowane


def decryption(text, rows=18):
    # Dzielimy tekst na wiersze o określonej długości
    wiersze = [list(text[i: i + rows]) for i in range(0, len(text), rows)]

    # Odwracam tablicę, zamieniając wiersze na kolumny
    kolumny = list(zip(*wiersze))

    # Zwracam listę kolumn
    odszyfrowane = [list(kolumna) for kolumna in kolumny]

    # Zmienia listę na tekst ciągły
    string_convert = ''
    for i in range(len(odszyfrowane)):
        for j in range(len(odszyfrowane[i])):
            string_convert += odszyfrowane[i][j]

    return string_convert







# Display the matrix
for row in matrix:
    print(''.join(row))

# print()
#
# zaszyfrowane = encryption(matrix)
#
# print()
# print(zaszyfrowane)
#
# print()
# print(decryption(zaszyfrowane))