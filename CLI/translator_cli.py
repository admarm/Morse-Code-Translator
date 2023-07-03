morse_code = { # English to Morse '/', ' '}
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--",
    "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "0" : "-----", "À" : ".--.-", "Å" : ".--.-", "Ä" : ".-.-", "Ą" : ".-.-", "Æ" : ".-.-", "Ć" : "-.-..", "Ĉ" : "-.-..", "Ç" : "-.-..", "Ch" : "----", "Ĥ" : "----",
    "Š" : "----", "Đ" : "..-..", "É" : "..-..", "Ę" : "..-..", "Ð" : "..--.", "È" : ".-..-", "Ł" : ".-..-", "Ĝ" : "--.-.", "Ĵ" : ".---.", "Ń" : "--.--", "Ñ" : "--.--",
    "Ó" : "---.", "Ö" : "---.", "Ø" : "---.", "Ś" : "...-...", "Ŝ" : "...-.", "Þ" : ".--..", "Ü" : "..--", "Ŭ" : "..--", "Ź" : "--..-.", "Ż" : "--..-", "1" : ".----",
    "2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....", "6" : "-....", "7" : "--...", "8" : "---..", "9" : "----.", "&" : ".-...", "'" : ".----.", "@" : ".--.-.",
    ")" : "-.--.-", "(" : "-.--.", ":" : "---...", "," : "--..--", "=" : "-...-", "!" : "-.-.--", "." : ".-.-.-", "-" : "-....-", "*" : "-..-", "%" : "----- -..-. -----",
    "+" : ".-.-.", "\"" : ".-..-.", "?" : "..--..", "/" : "-..-.", "¿" : "..-.-", ";" : "-.-.-.", "$" : "...-..-", "¡" : "--...-", "_" : "..--.-", " " : "/"
}

morse_code_reversed = {value: key for key, value in morse_code.items()}
morse_chars = {'.', '-', '/', ' '}

message = ""
inputed_message = input("Type your message: ").upper()

is_morse = False
is_normal = False

if all(char in morse_chars for char in inputed_message):
    is_morse = True

if is_morse:
    inputed_message = inputed_message.split(" ")

for char in inputed_message:
    if is_morse:
        if char in morse_code_reversed:
            is_morse = True
            message += morse_code_reversed[char]
        elif char == "":
            message += " "
    else:
        if char in morse_code:
            is_normal = True
            message += morse_code[char] + " "
        elif char == " ":
            message += "/ "

if is_normal:
    input("\nYour message in Morse Code: " + message)
elif is_morse:
    input("\nYour message converted from Morse Code: " + message)
