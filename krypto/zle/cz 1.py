import random

def string_to_binary(secret):
    return ''.join(format(ord(char), '08b') for char in secret)


def binary_to_string(binary):
    chars = [binary[i:i + 8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)


def generate_shares(secret):
    binary_secret = string_to_binary(secret)
    length = len(binary_secret)

    # Generate random binary strings (shares)
    share1 = ''.join(random.choice('01') for _ in range(length))
    share2 = ''.join(random.choice('01') for _ in range(length))

    # Create the third share to satisfy the equation: share1 XOR share2 XOR share3 = secret
    share3 = ''.join(str(int(binary_secret[i]) ^ int(share1[i]) ^ int(share2[i])) for i in range(length))

    return share1, share2, share3


def reconstruct_secret(share1, share2, share3):
    binary_secret = ''.join(str(int(share1[i]) ^ int(share2[i]) ^ int(share3[i])) for i in range(len(share1)))
    return binary_to_string(binary_secret)


# Example usage
secret = "Pieniądze są zakopane pod starą jablłonią w ogrodzie"
share1, share2, share3 = generate_shares(secret)

print("Share 1:", share1)
print("Share 2:", share2)
print("Share 3:", share3)

reconstructed_secret = reconstruct_secret(share1, share2, share3)
print("Reconstructed Secret:", reconstructed_secret)
