import statistics


class Calculator:
    def add(self, val1, val2):
        return val1 + val2

    def valid_age(self, value):
        return 1 <= value <= 100

    def max(self, val1, val2, val3):
        return max(val1, val2, val3)

    def isVocal(self, val):
        if val.isdigit():
            return 'numero'
        else:
            if val == 'a':
                return 'vocal'
            else:
                return 'consonante'

    def inversa(self, val):
        return val[::-1]

    def palindromo(self, word):
        reversed_word = word[::-1]
        if reversed_word == word:
            return True
        return False

    def numeros(self, val):
        mayor = max(val)
        minimo = min(val)
        prom = statistics.mean(val)
        val1 = [mayor, minimo, prom]
        return val1

    def pais(self, val):
        x = 0
        p = 0
        largo = len(val)
        for i in range(0, largo, 1):
            if x < len(val[i]):
                x = len(val[i])
                p = i
        return p

    def binary(self, val):
        return bin(val)

    def cant(self, val):
        return len(val)
