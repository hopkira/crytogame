import base64
import binascii

def binary_encode(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_decode(binary):
    return ''.join(chr(int(byte, 2)) for byte in binary.split())

def caesar_encode(text, shift=3):
    return ''.join(chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else
                   chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() else char
                   for char in text)

def caesar_decode(text, shift=3):
    return caesar_encode(text, -shift)

def reverse_text(text):
    return text[::-1]

def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    return base64.b64decode(text).decode()

def rot13(text):
    return ''.join(chr((ord(char) - 65 + 13) % 26 + 65) if char.isupper() else
                   chr((ord(char) - 97 + 13) % 26 + 97) if char.islower() else char
                   for char in text)

def hex_encode(text):
    return binascii.hexlify(text.encode()).decode()

def hex_decode(hex_text):
    return binascii.unhexlify(hex_text).decode()

# Example usage
message = "GOOD DOG"
encoded = base64_encode(caesar_encode(message))
print(f"Encoded: {encoded}")
decoded = caesar_decode(base64_decode(encoded))
print(f"Decoded: {decoded}")en
