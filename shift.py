
def shift_encrypt(text,shift):
    etext=""
    for i in range(len(text)):
        char = text[i]
        if char ==" ":
            etext+=" "
            continue
        if char.isupper():
            etext+=chr((ord(char)+shift -65)%26+65)
        else:
            etext+=chr((ord(char)+shift -97)%26+ 97)
    return etext
shift=6
entext=shift_encrypt("Hello World",shift);
print(entext, shift_encrypt(entext,-shift))