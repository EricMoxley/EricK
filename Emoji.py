message = input (">")
words = message.split(' ')
emojis = {
    ":)": "SMILE"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)

