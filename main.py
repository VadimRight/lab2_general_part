import math
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Данные задачи
variant = 1  # Номер варианта
t_values = [i for i in range(101)]  # Время (0 до 100 часов)
lambda_values = {1: 0.005, 2: 0.006, 3: 0.003, 4: 0.004}  # Интенсивности отказов по вариантам
m_values = {1: 3, 2: 2, 3: 3, 4: 3}  # Количество резервных элементов

# Параметры для текущего варианта
lambda_ = lambda_values[variant]
m = m_values[variant]

# Задача 1: P(t) и f(t)
P_t = [math.exp(-lambda_ * t) for t in t_values]  # Вероятность безотказной работы
f_t = [lambda_ * math.exp(-lambda_ * t) for t in t_values]  # Плотность отказов

# Задача 2: P_c(t) для резервируемой системы
def P_c(t, lambda_, m):
    result = 0
    for k in range(m + 1):
        term = ((lambda_ * t) ** k) / math.factorial(k) * math.exp(-lambda_ * t)
        result += term
    return result

P_c_t = [P_c(t, lambda_, m) for t in t_values]

# Среднее время безотказной работы
def avg_uptime(lambda_, m):
    integrand = lambda t: P_c(t, lambda_, m)
    return quad(integrand, 0, math.inf)[0]

avg_time = avg_uptime(lambda_, m)

# Вывод результатов
print(f"Интенсивность отказа (λ): {lambda_}")
print(f"Количество резервных элементов (m): {m}")
print(f"Среднее время безотказной работы: {avg_time:.2f} часов")

# Построение графиков
plt.figure(figsize=(12, 6))

# График P(t) и f(t)
plt.subplot(1, 2, 1)
plt.plot(t_values, P_t, label="P(t) (безотказная работа)", color="blue")
plt.plot(t_values, f_t, label="f(t) (плотность отказов)", color="green")
plt.xlabel("Время (часы)")
plt.ylabel("Вероятность / Плотность")
plt.title("Безотказная работа и плотность отказов")
plt.legend()
plt.grid()

# График P_c(t)
plt.subplot(1, 2, 2)
plt.plot(t_values, P_c_t, label=f"P_c(t) (резервирование, m={m})", color='orange')
plt.xlabel("Время (часы)")
plt.ylabel("Вероятность")
plt.title("Вероятность безотказной работы системы с резервированием")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
