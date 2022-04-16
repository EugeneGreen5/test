import Lexer_prog

while True:
    text=input('Текст: ')
    if text == 'exit':
        print('Конец программыы.')
        exit()
    result = Lexer_prog.run(text)
    print(result)