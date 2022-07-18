alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']

def polyalpthabit ():
    message = input("write a message : ")
    passward = input("enter the passward : ")
    passward = passward * len(message)
    cypher_text = ''
    count = 0
    for i in message:
        
        # index of letters of passward
        shift = alphabet.index(passward[count])
        # index of letters it self
        letter_index = alphabet.index(i)
        # index of the letter + index of passward
        cypher_letter = alphabet[(letter_index + shift ) % 26]
        cypher_text = cypher_text + cypher_letter
    count +=1
        
    return print(f"the cypher text is: {cypher_text}")
polyalpthabit()    
    