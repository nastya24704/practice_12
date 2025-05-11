def determine_winner(cities_sequence):
    cities = cities_sequence.split()
    previous_city = cities[0]
    current_player = "Вася" 
    
    for i in range(1, len(cities)):
        current_city = cities[i]
        if current_city[0].lower() != previous_city[-1].lower():
            return "Петя" if current_player == "Вася" else "Вася"
        
        previous_city = current_city
        current_player = "Вася" if current_player == "Петя" else "Петя"

    return "Петя" if current_player == "Вася" else "Вася"

input_sequence = "Москва Архангельск Красноярск Кемерово"
winner = determine_winner(input_sequence)
print(f"Победитель: {winner}")
