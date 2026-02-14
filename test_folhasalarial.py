

import unittest


from funcionarioclt import funcionarioclt
from funcinariopj import funcionarioPJ
from folhasalarial import folhasalarial

class TestFolhaSalarial(unittest.TestCase):

    def setUp(self):
        self.folha = folhasalarial()
        
        self.clt1 = funcionarioclt(
            nome_completo="JOALISON", 
            cpf="111.111.111-11", 
            salario_mensal=2000.00
        )
        self.pj1 = funcionarioPJ(
            nome_completo="PEDRO PEDROSA", 
            cpf="222.222.222-22", 
            salario_mensal=5000.00, 
            cnpj="12.345.678/0001-99"
        )
        self.clt2 = funcionarioclt(
            nome_completo="MARQUINHOS", 
            cpf="333.333.333-33", 
            salario_mensal=1500.00
        )

    
    def test_criar_funcionario_clt(self):
        self.assertEqual(self.clt1.nome_completo, "JOALISON")
        self.assertEqual(self.clt1.cpf, "111.111.111-11")
        self.assertEqual(self.clt1.salario_mensal, 2000.00)

    def test_criar_funcionario_pj(self):
        self.assertEqual(self.pj1.nome_completo, "PEDRO PEDROSA")
        self.assertEqual(self.pj1.cpf, "222.222.222-22")
        self.assertEqual(self.pj1.salario_mensal, 5000.00)
        self.assertEqual(self.pj1.cnpj, "12.345.678/0001-99")

    def test_salario_clt_abaixo_minimo(self):
        #Verificação da condicional em funcionarioclt que nos diz se o salario minimo está correto
        with self.assertRaises(ValueError):
            funcionarioclt(
                nome_completo="CEBOLINHA", 
                cpf="444.444.444-44", 
                salario_mensal=1000.00
            )

    def test_salario_clt_no_minimo(self):
        clt_minimo = funcionarioclt(
            nome_completo="CASCÃO", 
            cpf="555.555.555-55", 
            salario_mensal=1320.00
        )
        self.assertEqual(clt_minimo.salario_mensal, 1320.00)

    
    def test_beneficios_pj(self):
        #  Deverá aparecer apenas auxílio-saúde (R$ 500,00)
        self.assertEqual(self.pj1.levantamento_de_beneficios(), 500.00)

    def test_beneficios_clt(self):
        # (2000.00 * 0.06) e 500.00 
        self.assertAlmostEqual(self.clt1.levantamento_de_beneficios(), 620 )
        
        # (1500.00 * 0.06) e 500.00 
        self.assertAlmostEqual(self.clt2.levantamento_de_beneficios(), 590)

    
    def test_adicionar_funcionarios_folha(self):
        self.folha.adicionar_funcionario_a_folha_salarial(self.clt1)
        self.folha.adicionar_funcionario_a_folha_salarial(self.pj1)
        self.assertEqual(len(self.folha.funcionarios), 2)
        
       

    def test_recuperar_dados_funcionario_pelo_cpf(self):
        self.folha.adicionar_funcionario_a_folha_salarial(self.clt1)
        self.folha.adicionar_funcionario_a_folha_salarial(self.pj1)
        
        dados_clt = self.folha.recuperar_dados_funcionario_pelo_cpf("111.111.111-11")
        self.assertAlmostEqual(dados_clt["beneficios"], 620.00) 

        dados_pj = self.folha.recuperar_dados_funcionario_pelo_cpf("222.222.222-22")
        self.assertAlmostEqual(dados_pj["beneficios"], 500.00)
        
    def test_calcular_total_folha(self):
        self.folha.adicionar_funcionario_a_folha_salarial(self.clt1) # 2000
        self.folha.adicionar_funcionario_a_folha_salarial(self.pj1)  # 5000
        self.folha.adicionar_funcionario_a_folha_salarial(self.clt2) # 1500
        self.assertAlmostEqual(self.folha.calcular_total_folha_salarial(), 8500.00)

    def test_calcular_total_beneficios(self):
        self.folha.adicionar_funcionario_a_folha_salarial(self.clt1) # 620
        self.folha.adicionar_funcionario_a_folha_salarial(self.pj1)  # 500
        self.folha.adicionar_funcionario_a_folha_salarial(self.clt2) # 590
        self.assertAlmostEqual(self.folha.calcular_total_beneficios(), 1710.00)


if __name__ == '__main__':
    unittest.main()