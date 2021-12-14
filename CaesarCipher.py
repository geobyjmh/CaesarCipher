MESSAGE = 'Hello Julian'
E_KEY = 5
D_KEY = -5
  
def main():  
    encripted_message = message_encode(MESSAGE, E_KEY)
    print(encripted_message)

    decripted_message = message_encode(encripted_message, D_KEY)
    print(decripted_message)
       
def message_encode(message, key):
    msgs = [letter_encode(l, key) for l in list(message.upper())]
    return ''.join(msgs)

def letter_encode(letter, key):
    result = ' '
    if letter != ' ':
        result = shift_ascii_letter(letter, key)
    return result

def shift_ascii_letter(letter, shift_key):
    ascii_num_code = ord(letter) + shift_key
    ascii_num_code = rap_arround_ascii_letter(ascii_num_code)
    return chr(ascii_num_code)
    
def rap_arround_ascii_letter(ascii_code):
    if ascii_code > ord('Z'):
        ascii_code = ascii_code - 26
    if ascii_code < ord('A'):
        ascii_code = ascii_code + 26
    return ascii_code
    

if __name__ == '__main__':
    main()
