import hashlib
from binascii import unhexlify,hexlify
import sys



m = hashlib.md5()
m1 = '0e306561559aa787d00bc6f70bbdfe3404cf03659e704f8534c00ffb659c4c8740cc942feb2da115a3f4155cbb8607497386656d7d1f34a42059d78f5a8dd1ef'
m2 = '0e306561559aa787d00bc6f70bbdfe3404cf03659e744f8534c00ffb659c4c8740cc942feb2da115a3f415dcbb8607497386656d7d1f34a42059d78f5a8dd1ef'



# m1 = unhexlify('4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa200a8284bf36e8e4b55b35f427593d849676da0d1555d8360fb5f07fea2' )

# m2 = '4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa202a8284bf36e8e4b55b35f427593d849676da0d1d55d8360fb5f07fea2'

# m1='d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70'

# m2='d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70'

# d131dd02c5e6eec4693d9a0698aff95c2fcab58-12467eab4004583eb8fb7f8955ad340609f4b30283e4888325-1415a085125e8f7cdc99fd91dbdX280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2-487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f965-b6ff72a70




m1=unhexlify(m1)
m2=unhexlify(m2)

word = "hello"
if (len(sys.argv)>1):
	word=str(sys.argv[1])

a =word.encode()

mm1 = hashlib.md5()
mm2 = hashlib.md5()
print (hexlify(m1),"\n MD5 Hash Value:",mm1.digest().hex())
print ("\n",hexlify(m2),"\n MD5 Hash Value:",mm2.digest().hex())
print ("\nNow adding: ",word)
mm1.update(m1+a)
mm2.update(m2+a)
print (hexlify(m1+a),"\n MD5 Hash Value:",mm1.digest().hex())
print ("\n",hexlify(m2+a),"\n MD5 Hash Value",mm2.digest().hex())
