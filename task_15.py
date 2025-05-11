def get_secret_number():
    while True:
        num = input("Ведущий, введите 4-значное число с неповторяющимися цифрами: ")
        if len(num) == 4 and num.isdigit() and len(set(num)) == 4:
            return num
        print("Ошибка! Число должно быть 4-значным с неповторяющимися цифрами.")

def calculate_bulls_and_cows(secret, guess):
    bulls = cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def play_game():
    secret = get_secret_number()
    print("\n" * 25)
    attempts = 10
    print("Игра началась! У вас 10 попыток отгадать число.")
    for attempt in range(1, attempts + 1):
        while True:
            guess = input(f"Попытка {attempt}. Введите ваш вариант: ")
            if len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4:
                break
            print("Ошибка! Введите 4-значное число с неповторяющимися цифрами.")
        
        if guess == secret:
            print("Победа!")
            return
        bulls, cows = calculate_bulls_and_cows(secret, guess)
        print(f"Быков: {bulls} Коров: {cows}")
    
    print(f"Проигрыш! Загаданное число было: {secret}")

play_game()
