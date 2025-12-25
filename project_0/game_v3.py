import numpy as np

def game_core_v3(number: int = 1) -> int:
    """ Алгоритм пытается угадать число, затрачивая минимальное количество попыток.
    Функция принимает загаданное число и возвращает число попыток.
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0 
    low_border, high_border = 1, 100 
    
    # Цикл, сдвигающий нижнюю или верхнюю границу в зависимости от того,
    # больше или меньше число, чем заданное
    while True: 
        count += 1 
        predict_number = (low_border + high_border) // 2
        if predict_number > number: 
            print ("Число должно быть меньше!") 
            high_border = predict_number - 1 
        elif predict_number < number: 
            print ("Число должно быть больше!") 
            low_border = predict_number + 1 
        elif number == predict_number: 
            break
            
    return count
    
def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает алгоритм
    Args:
        random_predict (_type_): функция угадывания
        
    Returns:
        int: среднее количество попыток
    """

    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    # Цикл, который считает среднее количество попыток, за которые алгоритм угадывает число
    for number in random_array:
        count_ls.append(game_core_v3(number))
        count = int(np.mean(count_ls))
        print(f'Ваш алгоритм угадывает в среднем за: {count} попыток')
        return(count)

    return count

print('Run benchmarking for game_core_v3: \n', end='')
score_game(game_core_v3)