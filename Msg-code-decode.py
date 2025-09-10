def convert_text(text, mode):
    result = []
    text = text.upper()

    if mode == "1":  # Alphabet → Number
        for char in text:
            if char.isalpha():
                result.append(str(ord(char) - 64))
            else:
                result.append(char)
        return " ".join(result)

    elif mode == "2":  # Number → Alphabet
        for part in text.split():
            if part.isdigit():
                num = int(part)
                if 1 <= num <= 26:
                    result.append(chr(num + 64))
                else:
                    result.append("?")
            else:
                result.append(part)
        return "".join(result)


# Example usage
choice = input("Type '1' for Alphabet→Number, '2' for Number→Alphabet: ")
user_input = input("Enter text: ")
print("Converted:", convert_text(user_input, choice))
