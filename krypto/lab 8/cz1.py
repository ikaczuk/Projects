import random

alfabet = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "o", "ó", "p",
           "q", "r", "s", "ś", "t", "u", "v", "w", "x", "y", "z", "ź", "ż", " "]

def string_to_indices(secret):
    indices = [alfabet.index(char) for char in secret]
    return ''.join(format(index, '06b') for index in indices)  # 6-bit representation

def indices_to_string(binary):
    bits_per_char = 6
    indices = [int(binary[i:i + bits_per_char], 2) for i in range(0, len(binary), bits_per_char)]
    return ''.join(alfabet[index] for index in indices)

def generate_shares(secret):
    binary_secret = string_to_indices(secret)
    length = len(binary_secret)

    # Generate random binary strings (shares)
    share1 = ''.join(random.choice('01') for _ in range(length))
    share2 = ''.join(random.choice('01') for _ in range(length))

    # Create the third share to satisfy the equation: share1 XOR share2 XOR share3 = secret
    share3 = ''.join(str(int(binary_secret[i]) ^ int(share1[i]) ^ int(share2[i])) for i in range(length))
    return share1, share2, share3

def reconstruct_secret(share1, share2, share3):
    binary_secret = ''.join(str(int(share1[i]) ^ int(share2[i]) ^ int(share3[i])) for i in range(len(share1)))
    return indices_to_string(binary_secret)

# Example usage
secret = "pieniądze są zakopane pod starą jabłonią w ogrodzie"
share1, share2, share3 = generate_shares(secret)

print("Share 1:", share1)
print("Share 2:", share2)
print("Share 3:", share3)

reconstructed_secret = reconstruct_secret(share1, share2, share3)
print("Reconstructed Secret:", reconstructed_secret)
