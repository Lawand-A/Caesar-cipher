import argparse

#cipher 
def encrypt(p,k): 
    result = "" 
  
    # Function to encrypt
    for i in range(len(p)): 
        char = p[i] 
  
        # Encrypt uppercase
        if (char.isupper()): 
            result += chr((ord(char) + k-65) % 26 + 65) 
  
        # Encrypt lowercase  
        elif (char.islower()): 
            result += chr((ord(char) + k - 97) % 26 + 97)
        
        #ignore other
        else:
            result += char
  
    return result 

parser = argparse.ArgumentParser(description='caeser')
parser.add_argument('-k', '--k', type= int, help= 'key')
parser.add_argument('-p', '--p', type= str, help= 'text')

args = parser.parse_args()

if args.k and args.p:
	print(encrypt(args.p, args.k))

