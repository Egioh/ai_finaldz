# Импортируем нужные модули из Qiskit
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

# Определяем предикт для функции, которая является константной
# В этом случае предикт не делает ничего, так как функция всегда возвращает одно и то же значение
def oracle_constant(qc):
    pass

# Определяем предикт для функции, которая является балансированной
# В этом случае предикт применяет оператор X (переворачивает значение) ко всем выходным кубитам
def oracle_balanced(qc):
    qc.x(1)

# Определяем функцию для создания квантовой схемы и выполнения алгоритма Дойча-Йоза
def deutsch_jozsa(oracle):
    # Создаем квантовую схему с двумя кубитами и одним квантовым битом
    qc = QuantumCircuit(2, 1)
    
    # Переводим второй кубит в состояние |1>
    qc.x(1)
    
    # Применяем оператор Адамара ко всем кубитам
    qc.h(0)
    qc.h(1)
    
    # Применяем предикт
    oracle(qc)
    
    # Применяем оператор Адамара к первому кубиту
    qc.h(0)
    
    # Измеряем первый кубит
    qc.measure(0, 0)
    
    # Возвращаем схему
    return qc

# Выполняем алгоритм Дойча-Йоза для каждого из предиктов
for oracle in [oracle_constant, oracle_balanced]:
    qc = deutsch_jozsa(oracle)
    result = execute(qc, Aer.get_backend('qasm_simulator')).result()
    print(result.get_counts())