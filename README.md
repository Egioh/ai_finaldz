Алгоритм Дойча-Йоза решает следующую задачу: у вас есть "черный ящик" (оракул), который выполняет некоторую функцию f(x), 
принимающую на вход n-битовые строки и выдающую 0 или 1. Эта функция либо константна (всегда выдает 0 или всегда выдает 1), 
либо балансирована (выдает 0 для половины входных строк и 1 для другой половины). Ваша задача - определить, является ли данная функция f(x) константной или балансированной.

В данном примере реализовано два оракула: oracle_constant и oracle_balanced. oracle_constant не изменяет состояние кубитов, 
тем самым моделирует константную функцию. oracle_balanced, с другой стороны, применяет оператор X (смена значения) к кубиту, имитируя балансированную функцию.

В конце алгоритма мы измеряем первый кубит и смотрим на результаты измерения. В результате исполнения программы, 
для oracle_constant мы ожидаем всегда видеть '0', что означает, что функция константная, и для oracle_balanced мы ожидаем всегда видеть '1', что означает, что функция балансированная.

Алгоритм Дойча-Йоза показывает преимущество квантовых вычислений, потому что он определяет, 
является ли функция константной или балансированной, за одну операцию, тогда как классический компьютер должен был бы проверить хотя бы половину всех возможных входных значений.
