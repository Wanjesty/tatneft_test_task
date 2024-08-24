# Задание 1:
# Дано: число N
# Требуется: Написать функцию, возвращающую все простые числа до N

def get_prime_numbers(max_number: int) -> list[int]:
    """Получить простые числа до max_number включительно"""

    if max_number < 2:
        return []
    elif max_number == 2:
        return [2]
    else:
        prime_numbers = [2]
        for number in range(3, max_number + 1, 2):
            if (number > 10) and (number % 10 == 5):
                continue
            for previous_prime in prime_numbers:
                if number % previous_prime == 0:
                    break
            else:
                prime_numbers.append(number)
        return prime_numbers


if __name__ == '__main__':
    max_number = int(input('N = '))
    prime_numbers = get_prime_numbers(max_number)
    print(', '.join(map(str, prime_numbers)))
