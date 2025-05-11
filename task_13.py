def is_lucky_ticket(ticket):
    if not ticket.isdigit():
        return False
    
    length = len(ticket)
    if length % 2 != 0:
        return False
    
    half = length // 2
    first_half = ticket[:half]
    second_half = ticket[half:]
    
    sum_first = sum(int(d) for d in first_half)
    sum_second = sum(int(d) for d in second_half)
    return sum_first == sum_second

def find_lucky_ticket():
    count = 0
    while True:
        ticket = input("Введите номер билета: ").strip()
        count += 1
        if is_lucky_ticket(ticket):
            print(f"Найден счастливый билет! Его порядковый номер: {count}")
            return

find_lucky_ticket()
