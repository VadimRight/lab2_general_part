# Калькулятор стоимости окраски автомобиля

def calculate_paint_cost(part, color):
    # Базовая стоимость
    base_cost = 12000

    # Коэффициенты для цветов
    color_coefficients = {
        "Белый": 1,
        "Синий": 1,
        "Желтый": 1.1,
        "Красный": 1,
        "Перламутровый": 1.2,
        "Серый металлик": 1.3
    }

    # Коэффициенты для деталей
    part_coefficients = {
        "Капот": 1,
        "Передняя дверь": 1.2,
        "Задняя дверь": 1.1,
        "Передний бампер": 1,
        "Задний бампер": 1,
        "Крыша": 1.1
    }

    # Проверка на наличие цвета и детали в таблицах
    if color not in color_coefficients:
        return f"Ошибка: цвет '{color}' не найден в таблице."

    if part not in part_coefficients:
        return f"Ошибка: деталь '{part}' не найдена в таблице."

    # Расчет итоговой стоимости
    color_coeff = color_coefficients[color]
    part_coeff = part_coefficients[part]
    total_cost = base_cost * color_coeff * part_coeff

    return f"Стоимость окраски детали '{part}' в цвете '{color}': {total_cost:.2f} рублей"

# Пример использования
if __name__ == "__main__":
    print("Калькулятор стоимости окраски автомобиля")
    part = input("Введите наименование детали (например, 'Капот', 'Передняя дверь'): ")
    color = input("Введите цвет (например, 'Белый', 'Синий'): ")
    result = calculate_paint_cost(part, color)
    print(result)
