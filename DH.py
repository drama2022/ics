from random import randint

if __name__ == '__main__':

	# Both the persons will be agreed upon the
	# public keys G and P
	# A prime number P is taken
	P = 23
	
	# A primitive root for P, G is taken
	G = 11
	
	
	print("The Value of Prime no. choosen  is : %d" %(P))
	print("The Value of root 'G' is : %d" %(G))
	
	# Alice will choose the private key a
	a = int(input("Enter Private key no. for Alice : "))
	print("The Private Key 'a' for Alice is : %d" %(a))
	
	# gets the generated key
	x = int(pow(G,a,P))
	
	# Bob will choose the private key b
	b = int(input("Enter Private key no. for Bob : "))
	print("The Private Key 'b' for Bob is : %d" %(b))
	
	# gets the generated key
	y = int(pow(G,b,P))
	
	
	# Secret key for Alice
	ka = int(pow(y,a,P))
	
	# Secret key for Bob
	kb = int(pow(x,b,P))
	
	print("Secret key for the Alice is : %d" %(ka))
	print("Secret Key for the Bob is : %d" %(kb))
