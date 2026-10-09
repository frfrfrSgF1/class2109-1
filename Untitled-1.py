a = float(input("Введите число a: "))
b = float(input("Введитпе число b: "))
sum_val = a + b
result_minus = a - b
if b != 0:
    result = a / b
    print(f" Result: {sum_val}, {result}, {result_minus}")
else:
    print(f" Result: {sum_val}, деление на ноль невозможно, {result_minus}")