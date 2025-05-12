def number_to_words(num):
    if num == 0:
        return 'ноль'
    
    units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 
             'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 
            'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот',
                'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    thousands = ['', 'тысяча', 'тысячи', 'тысяч']
    millions = ['', 'миллион', 'миллиона', 'миллионов']
    
    def convert_less_than_thousand(n, is_thousand=False):
        if n == 0:
            return ''
        res = []
        hundred = n // 100
        remainder = n % 100
        if hundred > 0:
            res.append(hundreds[hundred])
        if 10 <= remainder < 20:
            res.append(teens[remainder - 10])
        else:
            ten = remainder // 10
            unit = remainder % 10
            if ten > 1:
                res.append(tens[ten])
            if unit > 0:
                if is_thousand:
                    # Особые формы для тысяч
                    if unit == 1:
                        res.append('одна')
                    elif unit == 2:
                        res.append('две')
                    else:
                        res.append(units[unit])
                else:
                    res.append(units[unit])
        return ' '.join(res)
    
    parts = []
    
    # Миллионы
    million_part = num // 1_000_000
    if million_part > 0:
        parts.append(convert_less_than_thousand(million_part) + ' ' 
                     + get_plural_form(million_part, millions))
        num %= 1_000_000
    
    # Тысячи
    thousand_part = num // 1_000
    if thousand_part > 0:
        parts.append(convert_less_than_thousand(thousand_part, is_thousand=True) 
                     + ' ' + get_plural_form(thousand_part, thousands))
        num %= 1_000
    
    # Единицы
    if num > 0 or not parts:
        parts.append(convert_less_than_thousand(num))
    
    return ' '.join(parts).strip()

def get_plural_form(n, forms):
    n = n % 100
    if 11 <= n <= 19:
        return forms[3]
    n = n % 10
    if n == 1:
        return forms[1]
    if 2 <= n <= 4:
        return forms[2]
    return forms[3]

while True:
    try:
        number = int(input("Введите число от 1 до 900 000 000: "))
        if 0 <= number <= 900_000_000:
            break
        print("Число должно быть от 0 до 900 000 000")
    except ValueError:
        print("Пожалуйста, введите целое число")

print(f"{number} - {number_to_words(number)}")
