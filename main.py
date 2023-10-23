from SAScipher import vigener as v
from SAScipher import caesar as c
from SAScipher import binar_code as b

# print(v.encryption('☐ x²', 'q'))
# print(v.decryption('⛴!yƖ', 'q'))

a = b.encryption('⛴i!yƖ')
print(a)
print(b.decryption(a))
