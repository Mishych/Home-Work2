import struct

def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

def sha1(message):
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    original_length = (8 * len(message)) & 0xffffffffffffffff
    message += b'\x80'

    while (len(message) % 64) != 56:
        message += b'\x00'

    message += struct.pack('>Q', original_length)

    chunks = [message[i:i + 64] for i in range(0, len(message), 64)]

    for chunk in chunks:
        w = list(struct.unpack('>16I', chunk))

        if len(w) < 80:
            w += [0] * (80 - len(w))

        for i in range(16, 80):
            w[i] = left_rotate(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16], 1)

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for i in range(80):
            if i < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif i < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif i < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = left_rotate(a, 5) + f + e + k + w[i] & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

# Функція для гешування даних
def hash_data(data):
    return sha1(data.encode())


while True:
    # Введення даних для гешування
    data = input("Введіть дані для гешування: ")
    hashed_data = hash_data(data)
    print("Гешовані дані:", hashed_data)
    a = input("Продовжити? (Так/Ні) \n")
    if a == 'Так':
        continue
    elif a == 'Ні':
        break
    else:
        print("Невірна команда! \n")
        a = input("Бажаєте продовжити? (Так/Ні) \n")
        if a == 'Так':
            continue
        elif a == 'Ні':
            break
        else:
            print("Невірна команда! \n")
            a = input("Бажаєте продовжити? (Так/Ні) \n")
        
    