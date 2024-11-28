import math
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Заданные параметры
lambda_ = 0.05  # Интенсивность отказа, 1/ч
m = 2  # Кратность резерва
t_values = [i for i in range(101)]  # Время от 0 до 100 часов

# Функция вероятности безотказной работы для системы с резервом замещением
def P_c(t, lambda_, m):
    """Вычисление вероятности безотказной работы системы с резервированием."""
    result = 0
    for k in range(m + 1):  # Суммирование по числу резервов (0...m)
        term = ((lambda_ * t) ** k) / math.factorial(k) * math.exp(-lambda_ * t)
        result += term
    return result

# Вычисление вероятности P_c(t) для всех t
P_c_t = [P_c(t, lambda_, m) for t in t_values]

# Среднее время безотказной работы системы
def avg_uptime(lambda_, m):
    """Среднее время безотказной работы системы."""
    integrand = lambda t: P_c(t, lambda_, m)  # Интегрируемая функция
    return quad(integrand, 0, math.inf)[0]

avg_time = avg_uptime(lambda_, m)

# Вероятность безотказной работы системы с постоянно включенным резервом
P_parallel = [math.exp(-(lambda_ / (m + 1)) * t) for t in t_values]

# Вывод результатов
print(f"Интенсивность отказа (λ): {lambda_}")
print(f"Кратность резерва (m): {m}")
print(f"Среднее время безотказной работы системы: {avg_time:.2f} часов")

# Построение графиков
plt.figure(figsize=(10, 6))

# График P_c(t) для системы с резервом замещением
plt.plot(t_values, P_c_t, label=f"P_c(t) (резервирование, m={m})", color="blue")

# График P_parallel(t) для постоянно включенного резерва
plt.plot(t_values, P_parallel, label=f"P_parallel(t) (постоянно включённый резерв)", color="green", linestyle="--")

# Оформление графика
plt.xlabel("Время (часы)")
plt.ylabel("Вероятность")
plt.title("Вероятность безотказной работы системы")
plt.legend()
plt.grid()
plt.show()
