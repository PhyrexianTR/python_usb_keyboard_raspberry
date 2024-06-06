import time

def send_key(key):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(key)

# Example: sending "Hello, world!"
keys = [
    b'\x00\x00\x0b\x00\x00\x00\x00\x00',  # 'H'
    b'\x00\x00\x08\x00\x00\x00\x00\x00',  # 'e'
    b'\x00\x00\x0f\x00\x00\x00\x00\x00',  # 'l'
    b'\x00\x00\x0f\x00\x00\x00\x00\x00',  # 'l'
    b'\x00\x00\x12\x00\x00\x00\x00\x00',  # 'o'
    b'\x00\x00\x2c\x00\x00\x00\x00\x00',  # ','
    b'\x00\x00\x2c\x00\x00\x00\x00\x00',  # ' '
    b'\x00\x00\x1a\x00\x00\x00\x00\x00',  # 'w'
    b'\x00\x00\x12\x00\x00\x00\x00\x00',  # 'o'
    b'\x00\x00\x15\x00\x00\x00\x00\x00',  # 'r'
    b'\x00\x00\x0f\x00\x00\x00\x00\x00',  # 'l'
    b'\x00\x00\x07\x00\x00\x00\x00\x00',  # 'd'
    b'\x00\x00\x2e\x00\x00\x00\x00\x00',  # '!'
]

for key in keys:
    send_key(key)
    time.sleep(0.1)
    send_key(b'\x00\x00\x00\x00\x00\x00\x00\x00')  # Release key
    time.sleep(0.1)
