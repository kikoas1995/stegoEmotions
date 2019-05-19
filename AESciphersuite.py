import base64

from Crypto.Cipher import AES
import hashlib

BS = 32
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]


class AESciphersuite:

    def __init__( self, preKey ):
        sha_key = hashlib.sha256(preKey.encode()).hexdigest()
        final_key = sha_key[:32]
        self.key = final_key
        self.iv = "0123456789abcdef"

    def encrypt( self, raw ):
        raw = pad(raw)
        cipher = AES.new( self.key, AES.MODE_CBC, self.iv )
        return base64.b64encode( self.iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        textToDecrypt = enc[16:]
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return unpad( cipher.decrypt ( textToDecrypt ) )

