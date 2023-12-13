import secrets
import zlib
import hashlib


def encrypt(data, password, compress_level=1):
    data = zlib.compress(data, compress_level)
    sha256 = hashlib.sha256(password.encode("utf-8")).hexdigest()
    head = sha256.encode() + len(data).to_bytes(8, "big")
    mask = hashlib.sha256((password * 2).encode("utf-8")).hexdigest()
    mask_num = int.from_bytes(mask.encode(), "little")

    encrypted = b''
    for i in range(0, len(data), 64):
        num = int.from_bytes(data[i:i + 64], "little")
        num_enc = num ^ mask_num
        encrypted += num_enc.to_bytes(64, "little")

    return head + encrypted[:len(data)]


def decrypt(encrypted, password):
    # print(password)
    encrypted = encrypted[1:]
    sha256 = encrypted[:64]
    # print(sha256)
    # print(hashlib.sha256(password.encode("utf-8")).hexdigest().encode())
    if hashlib.sha256(password.encode("utf-8")).hexdigest().encode() != sha256:
        raise TypeError("Invalid password")
    mask = hashlib.sha256((password * 2).encode("utf-8")).hexdigest()
    mask_num = int.from_bytes(mask.encode(), "little")
    length = int.from_bytes(encrypted[64:64 + 8], "big")

    data = b''
    for i in range(64 + 8, len(encrypted), 64):
        num_enc = int.from_bytes(encrypted[i:i + 64], "little")
        num = num_enc ^ mask_num
        data += num.to_bytes(64, "little")

    return zlib.decompress(data[:length])

# if __name__ == '__main__':
#     password = "131412"
#
#     d = decrypt(encrypt(secrets.token_hex(16).encode(), password), password)
#     print(d)