StegoEmotions
=============


A steganographic tool to and reveal hide messages in tweets.


Installation
------------
````bash

pip install requests
pip install simplejson
pip install tweepy
pip install twython

#Windows: previous to install Crypto, you probably need to install Microsoft Visual C++ Compiler for Python 2.7  http://aka.ms/vcpython27
easyinstall crypto 
#Linux:
pip install pycrypto
````

Usage
-----
```bash
stegoEmotions.py 

Usage:
    stegoEmotions.py --hide
    stegoEmtions.py --reveal
    
Options: 
    --hide          hide a message
    --reveal        reveal a message

```

