def save_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(' '.join(map(str, data)))

# Zapis do plików
save_to_file('KeyStream.txt', [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1])
save_to_file('PlainMessage.txt', [1, 1, 1, 1, 1, 1])
save_to_file('CipherText.txt', [0, 0, 1, 1, 0, 0])
save_to_file('CipherText-Error.txt', [0, 0, 1, 0, 0, 0])
save_to_file('Decrypted.txt', [1, 1, 1, 1, 1, 1])
save_to_file('Decrypted-Error.txt', [1, 1, 1, 0, 1, 1])
save_to_file('CipherText-Shifted.txt', [0, 1, 1, 0, 0, 0])
save_to_file('Decrypted-Shifted.txt', [1, 0, 1, 0, 1, 1])
