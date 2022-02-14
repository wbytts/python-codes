
import struct

# struct.pack(fmt, *args)
data = struct.pack('>i4sh', 7, b'spam', 8)
print(data)

# struct.unpack('>i4sh', data)
value = struct.unpack('>i4sh', data)
print(value)
