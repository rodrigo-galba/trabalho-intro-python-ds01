import unittest
from lib import lib

class TestLib(unittest.TestCase):
    def test_inicializa_fornecedores(self):
        lines = list(["1",
                      "1",
                      "2"])
        fornecedores = lib.inicializa_fornecedores(lines)
        total_meses_inicio = 12 + 1
        fornecedor_01 = fornecedores[0]

        self.assertEqual(len(fornecedores), 2)
        self.assertEqual(len(fornecedor_01), total_meses_inicio)
        self.assertEqual(fornecedores[0][0], list([float('inf')] * total_meses_inicio))
        self.assertEqual(fornecedores[0][0][0], float('inf'))
        self.assertEqual(fornecedores[0][1], list([float('inf')] * total_meses_inicio))
        self.assertEqual(fornecedores[0][1][0], float('inf'))

    def test_processa_contratos(self):
        lines = list(["1 1 1 10",
                      "1 1 2 105.0",
                      "1 1 3 108.0",
                      "1 2 2 100.0",
                      "1 2 3 102.0",
                      "1 3 3 10.0",
                      "2 1 1 80",
                      "2 1 2 95.0",
                      "2 1 3 115.0",
                      "2 2 2 20.0",
                      "2 2 3 60.0",
                      "2 3 3 50.0"])
        contratos_por_fornecedor = lib.processa_contratos(lines)
        fornecedor_01 = contratos_por_fornecedor[0]
        fornecedor_02 = contratos_por_fornecedor[1]

        self.assertEqual(len(contratos_por_fornecedor), 2)

        self.assertEqual(fornecedor_01[1][1], 10)
        self.assertEqual(fornecedor_01[1][2], 105.0)
        self.assertEqual(fornecedor_01[1][3], 108.0)
        self.assertEqual(fornecedor_01[2][2], 100.0)
        self.assertEqual(fornecedor_01[2][3], 102.0)
        self.assertEqual(fornecedor_01[3][3], 10.0)
        self.assertEqual(fornecedor_01[2][5], float('inf'))

        self.assertEqual(fornecedor_02[1][1], 80)
        self.assertEqual(fornecedor_02[1][2], 95)
        self.assertEqual(fornecedor_02[1][3], 115)
        self.assertEqual(fornecedor_02[2][2], 20)
        self.assertEqual(fornecedor_02[2][3], 60)
        self.assertEqual(fornecedor_02[3][3], 50)
        self.assertEqual(fornecedor_02[2][5], float('inf'))


if __name__ == '__main__':
    unittest.main()