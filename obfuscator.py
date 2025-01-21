## text obfuscator by oxunem

char_map = {
    'а': 'a', 'б': '6', 'в': 'B', 'г': 'r', 'д': 'D', 'е': 'e', 'ё': 'e', 'ж': '}|{', 'з': '3', 'и': 'u', 'й': 'u',
    'к': 'K', 'л': 'JI', 'м': 'M', 'н': 'H', 'о': 'O', 'п': 'n', 'р': 'P', 'с': 'C', 'т': 'T', 'у': 'y', 'ф': 'qp',
    'х': 'X', 'ц': 'u,', 'ч': '4', 'ш': 'W', 'щ': 'W,', 'ъ': 'b"', 'ы': 'bI', 'ь': 'b', 'э': '-)', 'ю': 'IO', 'я': '9I',
    'А': 'A', 'Б': '6', 'В': 'B', 'Г': 'R', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': '}|{', 'З': '3', 'И': 'U', 'Й': 'U',
    'К': 'K', 'Л': 'JI', 'М': 'M', 'Н': 'H', 'О': 'O', 'П': 'n', 'Р': 'P', 'С': 'C', 'Т': 'T', 'У': 'Y', 'Ф': 'QP',
    'Х': 'X', 'Ц': 'U,', 'Ч': '4', 'Ш': 'W', 'Щ': 'W,', 'Ъ': 'b"', 'Ы': 'BI', 'Ь': 'b', 'Э': '-)', 'Ю': 'IO', 'Я': '9I',
    ' ': ' ', ',': ',', '.': '.', '-': '-', '!': '!', '?': '?', ':': ':', ';': ';'
}

def convert_to_obfuscated_text(text):
    converted_text = []
    for char in text:
        if char in char_map:
            converted_text.append(char_map[char])
        else:
            converted_text.append(char)
    return ''.join(converted_text)

def main():
    print("Добро пожаловать в программу преобразования текста!")
    text = input("Введите текст для преобразования: ")
    result = convert_to_obfuscated_text(text)
    print("Результат преобразования:", result)

if __name__ == "__main__":
    main()