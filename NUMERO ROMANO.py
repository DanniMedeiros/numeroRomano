def converte(numeroEmRomano):
    tabela = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    acumulador = 0
    ultimovizinhodireita = 0

    for i in reversed(range(len(numeroEmRomano))):
        atual = tabela[numeroEmRomano[i]]
        multiplicador = -1 if atual < ultimovizinhodireita else 1
        acumulador += atual * multiplicador
        ultimovizinhodireita = atual

    return acumulador


import unittest

class TestConverteNumerosRomanos(unittest.TestCase):

    def test_I(self):
        self.assertEqual(converte('I'), 1)

    def test_V(self):
        self.assertEqual(converte('V'), 5)

    def test_II(self):
        self.assertEqual(converte('II'), 2)

    def test_XXII(self):
        self.assertEqual(converte('XXII'), 22)

    def test_IX(self):
        self.assertEqual(converte('IX'), 9)

    def test_XXIV(self):
        self.assertEqual(converte('XXIV'), 24)


if __name__ == '__main__':
    unittest.main(exit=False)

    numeros_romanos = ['I', 'V', 'II', 'XXII', 'IX', 'XXIV']
    for numero in numeros_romanos:
        valor = converte(numero)
        print(f"O número romano '{numero}' corresponde a {valor}.")