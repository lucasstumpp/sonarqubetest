def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5

notas = [0, 0, 9.0, 8.0, 5.0, 10.0, 7.0,
         7.5, 4.0, 10.0, 7.0, 7.0, 8.0, 8.0, 7.5]
soma_das_notas = sum(notas)
print(soma_das_notas)