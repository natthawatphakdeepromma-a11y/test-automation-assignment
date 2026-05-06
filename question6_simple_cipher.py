def simpleCipher(encrypted: str, k: int) -> str:
    result = []
    for char in encrypted:
        index = ord(char) - ord('A')
        decrypted_index = (index - k) % 26
        result.append(chr(decrypted_index + ord('A')))
    return ''.join(result)

if __name__ == "__main__":
    print(simpleCipher('VTAOG', 2))   # You should TRYME.
    print(simpleCipher('A', 1))       # You should Z.
    print(simpleCipher('HELLO', 0))   # You should HELLO.
