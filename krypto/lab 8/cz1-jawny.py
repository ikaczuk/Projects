import random

alfabet = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "o", "ó", "p",
           "q", "r", "s", "ś", "t", "u", "v", "w", "x", "y", "z", "ź", "ż", " "]

def generate_shares(secret):
    length = len(secret)

    # Generate random shares as strings of random letters from the alphabet
    share1 = ''.join(random.choice(alfabet) for _ in range(length))
    share2 = ''.join(random.choice(alfabet) for _ in range(length))

    # Create the third share to satisfy: share1 XOR share2 XOR share3 = secret
    share3 = ''.join(
        alfabet[
            (alfabet.index(secret[i]) - alfabet.index(share1[i]) - alfabet.index(share2[i])) % len(alfabet)
        ] for i in range(length)
    )

    return share1, share2, share3

def reconstruct_secret(share1, share2, share3):
    length = len(share1)
    secret = ''.join(
        alfabet[
            (alfabet.index(share1[i]) + alfabet.index(share2[i]) + alfabet.index(share3[i])) % len(alfabet)
        ] for i in range(length)
    )
    return secret

# Example usage
secret = "pieniądze są zakopane pod starą jabłonią w ogrodzie"
share1, share2, share3 = generate_shares(secret)

print("Share 1:", share1)
print("Share 2:", share2)
print("Share 3:", share3)

reconstructed_secret = reconstruct_secret(share1, share2, share3)
print("Reconstructed Secret:", reconstructed_secret)
