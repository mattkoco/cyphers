import base64
import random
import binascii

# Written in Python 3 if that matters to you


# Change from "False" to "True" if decoding
def complex_cipher(message, key1, key2, key3, decode=False):
    if decode:
        message = base64.b64decode(message)

    encrypted_message = b''
    for i, c in enumerate(message):
        key_c1 = ord(key1[i % len(key1)])
        key_c2 = ord(key2[i % len(key2)])
        key_c3 = ord(key3[i % len(key3)])
        if not decode:
            encrypted_message += bytes(
                [(((ord(c) + key_c1) + key_c2) + key_c3) % 256])
        else:
            encrypted_message += bytes([(((c - key_c1) -
                                       key_c2) - key_c3) % 256])

    if not decode:
        return base64.b64encode(encrypted_message)
    return encrypted_message


def main():
    message = "message1"  # if decrypting, will take the form of: b'encryptedmessage'
    key1 = "key1"
    key2 = "key2"
    key3 = "key3"
    try:
        decrypted_message = complex_cipher(
            message, key1, key2, key3, decode=False)  # Change from "False" to "True" if decoding
        print(decrypted_message)
    except binascii.Error:
        print("An error occurred while decoding the message.")


if __name__ == "__main__":
    main()

# copyright @mattkoco on github (sorta)
#
# feel free to add more keys for better encryption
#
