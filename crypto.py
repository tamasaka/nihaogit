#
from Crypto.Cipher import AES
import base64

message="自分がしてほしいと思うことを人にもするように"
password="xxxxxxxxxx"
iv="XXXXXXXXXXXXXXXX"
mode=AES.MODE_CBC

def mkpad(s,size):
    s=s.encode("utf-8")
    pad=b' '*(size-len(s)%size)

def encrypt(password,data):
    password=mkpad(password,16)
    data=mkpad(data,16)
    password=password[:16]
    aes=AES.new(password,mode,iv)
    data_cipher=aes.encrypt(data)
    return base64.b64encode(data_cipher).decode("utf-8")

def decrypt(password,encdata):
  password=mkpad(password,16)
  password=password[:16]
  aes=AES.new(password,mode,iv)
  encdata=base64.b64decode(encdata)
  data=aes.decrypt(encdata)
  return data.decode("utf-8")

enc=encrypt(password,message)

dec=decrypt(password,enc)

print("暗号化:",enc)
print("復号化:",dec)
