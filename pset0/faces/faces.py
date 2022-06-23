def main():
    message = input()
    convert(message)

def convert(msg):
    words = msg.split(' ')
    emojis = {
        ":)": "🙂",
        ":(": "🙁",
        ":D": "😃",
        ":'(": "🥲"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return print(output)

main()