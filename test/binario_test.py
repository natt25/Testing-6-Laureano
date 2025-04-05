    # Write test cases that achieve 100%  
    # Statement coverage of add8. You  
    # will need to call add8 multiple  
    # times in order to do this. 

import unittest
from binario import add8 
import unittest
from binario import add8  # Importar la función add8 del archivo principal

class TestAdd8Function(unittest.TestCase):

    # Cao: ninguna de las condiciones (s1, s2, ..., s8) es verdadera
    def test_case_1(self):
        result = add8(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(result, (False, False, False, False, False, False, False, False, False))

    # Caso: todas las condiciones son verdaderas (caso maximo)
    def test_case_2(self):
        result = add8(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0)
        self.assertEqual(result, (False, True, True, True, True, True, True, True, True))

    # Caso: s1 es True y el resto son False
    def test_case_3(self):
        result = add8(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(result, (True, False, False, False, False, False, False, False, False))

    # Caso: s2 es True 
    def test_case_4(self):
        result = add8(0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(result, (False, True, False, False, False, False, False, False, False))

    # Caso: s3 es True
    def test_case_5(self):
        result = add8(0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(result, (False, False, True, False, False, False, False, False, False))

    # Caso: c1 es True 
    def test_case_6(self):
        result = add8(1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(result, (False, True, True, False, False, False, False, False, False))

    # Caso: acarreo en bits posteriores influye en los valores s 
    def test_case_7(self):
        result = add8(1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0)
        self.assertEqual(result, (False, True, False, False, False, False, False, True, False))

    # Caso: combinación de condiciones verdaderas y falsas para acarreo y valores s
    def test_case_8(self):
        result = add8(1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0)
        self.assertEqual(result, (False, True, True, True, True, False, False, False, False))

if __name__ == '__main__':
    unittest.main()