from base64 import b64encode
from zlib import compress, decompress


def decode_image(data):
    data = compress(data)
    returnable = b64encode(decompress(data)).decode("utf-8")
    return returnable
