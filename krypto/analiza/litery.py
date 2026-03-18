def upload_files(plik):
    with open(plik, "r") as file:
        text = file.read().strip().upper()
    return text

text = upload_files("szyfr1.txt")
text1 = upload_files("szyfr2.txt")

t = upload_files("kp.txt")
print(len(t))
# print("1: ", len(text))
# print("2: ", len(text1))