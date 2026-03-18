characters = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "o", "ó", "p", "q", "r", "s", "ś", "t", "u", "v", "w", "x", "y", "z", "ź", "ż", " "]
message = "Pieniądze są zakopane pod starą jabłonią w ogrodzie"

indices = [characters.index(char.lower()) for char in message]

def lagrange_interpolation(x, y, x_val):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_val - x[j]) / (x[i] - x[j])
        result += term
    return result

x = list(range(len(indices)))
y = indices

x_val = 10
interpolated_value = lagrange_interpolation(x, y, x_val)
print(f"Interpolowana wartość dla x={x_val}: {interpolated_value}")

decoded_message = ''.join([characters[int(lagrange_interpolation(x, y, i))] for i in range(len(message))])
print(f"Odkodowane zdanie: {decoded_message}")
