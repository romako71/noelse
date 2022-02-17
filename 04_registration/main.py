with open('registrations.txt', 'r', encoding='utf8') as people_file:
    for i_line in people_file:
        record = i_line.split()
        if len(record) != 3:
            raise IndexError('НЕ присутствуют все три поля')
        elif not record[0].isalpha():
            raise NameError('поле имени содержит НЕ только буквы')
        elif not ((record[1].count('@') == 1) and (record[1].count('.') == 1) and (record[1].index('@') > record[1].index('.'))):
            raise SyntaxError('поле емейл НЕ содержит @ и .(точку)')
        elif not (10 <= int(record[2]) < 100):
            raise ValueError('поле возраст НЕ является числом от 10 до 99')

