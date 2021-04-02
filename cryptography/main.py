from art import art



def cryptography():
  print(art)
  
 
cryptography()
def endecode():
    while True:
        en_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        #making sure users put in only encode and decode
        while en_decode.lower() != 'encode' and en_decode.lower() != 'decode':
            en_decode = input("\nInvalid answer.... Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        
        message = input("\nType your Message: \n")
        while message == '':
            message = input("\nPlease type a valid message: \n")

        #prompt users for the key and it make sure users put in a number as a key   
        key = input("\nType encryption/decryption key:\n")
        while key.isnumeric() == False:
            if key == '':
                key = '0'
            else:
                key = input("\nInvalid encryption/decryption key, please try again:\n")
        key = int(key)

        #running the crypto function
        print(crypto(en_decode,message,key))

        #Used in asking if the users want to continue or end the program
        end = input("\nType 'yes' if you want to go again, otherwise type 'no': \n")
        if end == 'yes':
            continue
        elif end == 'no':
            break
    return "\nThanks for using our cryptography service"

# This function encrypt or decrypt the message
def crypto(endec, msg, enkey): 
    charct = " "
    for s in msg:
        if ord(s) > 122 or ord(s) < 96:
            charct += s
        else:
            if endec == 'encode':
                charctin = ord(s) + enkey
                if charctin > 122:
                    charctin = (charctin % 122) + 96
                charct += chr(charctin)
            elif endec == 'decode':
                charctin = ord(s) - enkey
                if charctin < 97:
                    charctin = 122 - (96 - charctin)
                charct += chr(charctin)
    return f"\nHere is the coded result: {charct}"

    


print(endecode())