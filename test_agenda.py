

import unittest


from agenda import agenda
from contato import contato


class TestAgenda(unittest.TestCase):

    def setUp(self):
        
        self.agenda = agenda()

    
    def test_criar_contato_e_telefones(self):
        cont = contato("MATIAS")
        self.assertEqual(cont.nome, "MATIAS")
        self.assertEqual(len(cont.telefones), 0)
        
        cont.adicionar_telefone("casa", "88 99999-1111")
        self.assertEqual(len(cont.telefones), 1)
        self.assertEqual(cont.telefones[0].identificador, "casa")
        self.assertEqual(cont.telefones[0].numero, "88 99999-1111")
        
        cont.adicionar_telefone("trabalho", "88 99999-2222")
        self.assertEqual(len(cont.telefones), 2)

    def test_adicionar_telefone_identificador_duplicado(self):
        cont = contato("Fulano")
        cont.adicionar_telefone("casa", "1111")
        with self.assertRaises(ValueError):
            cont.adicionar_telefone("casa", "2222") # Tentando adicionar "casa" denovo

    def test_remover_telefone(self):
        cont = contato("Beltrano")
        cont.adicionar_telefone("casa", "1111")
        cont.adicionar_telefone("celular", "2222")
        
        removido = cont.remover_telefone("casa")
        self.assertTrue(removido)
        self.assertEqual(len(cont.telefones), 1)
        self.assertEqual(cont.telefones[0].identificador, "celular")

    def test_remover_telefone_inexistente(self):
        cont = contato("Beltrano")
        cont.adicionar_telefone("casa", "1111")
        
        removido = cont.remover_telefone("trabalho")
        self.assertFalse(removido)
        self.assertEqual(len(cont.telefones), 1)

   
    def test_adicionar_contato_valido(self):
        cont_valido = contato("Ana")
        cont_valido.adicionar_telefone("celular", "1234")
        
        # Instancia Agenda (importada de agenda.py)
        self.agenda.adicionar_contato(cont_valido)
        self.assertEqual(len(self.agenda.contatos), 1)
        self.assertIn(cont_valido, self.agenda.contatos)

    def test_adicionar_contato_sem_telefone(self):
        cont_invalido = contato("Bruno") # Criado sem telefone
        
        with self.assertRaises(ValueError) as context:
            self.agenda.adicionar_contato(cont_invalido)
        
        self.assertEqual(
            str(context.exception), 
            "Não é possível adicionar um contato sem telefone."
        )
        self.assertEqual(len(self.agenda.contatos), 0)

    def test_listar_contatos_ordem_alfabetica(self):
        c1 = contato("Zidane")
        c1.adicionar_telefone("celular", "1")
        
        c2 = contato("Ana")
        c2.adicionar_telefone("celular", "2")
        
        c3 = contato("Bruno")
        c3.adicionar_telefone("celular", "3")
        
        self.agenda.adicionar_contato(c1)
        self.agenda.adicionar_contato(c2)
        self.agenda.adicionar_contato(c3)
        
        lista_ordenada = self.agenda.listar_contatos()
        
        self.assertEqual(len(lista_ordenada), 3)
        self.assertEqual(lista_ordenada[0].nome, "Ana")
        self.assertEqual(lista_ordenada[1].nome, "Bruno")
        self.assertEqual(lista_ordenada[2].nome, "Zidane")

    def test_remover_contato_da_agenda(self):
        c1 = contato("Daniela")
        c1.adicionar_telefone("casa", "123")
        self.agenda.adicionar_contato(c1)
        self.assertEqual(len(self.agenda.contatos), 1)
        
        removido = self.agenda.remover_contato("Daniela")
        self.assertTrue(removido)
        self.assertEqual(len(self.agenda.contatos), 0)

    def test_remover_contato_inexistente(self):
        c1 = contato("Elisa")
        c1.adicionar_telefone("casa", "123")
        self.agenda.adicionar_contato(c1)
        
        removido = self.agenda.remover_contato("Fábio") # Nome não existe
        self.assertFalse(removido)
        self.assertEqual(len(self.agenda.contatos), 1)


if __name__ == '__main__':
    unittest.main()