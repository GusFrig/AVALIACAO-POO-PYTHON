
from contato import contato

class agenda:
   
    def __init__(self):
        self.contatos: list[contato] = []

    def adicionar_contato(self, contato: contato):
       
        
        if not contato.telefones: # Verificando se a lista de telefones está vazia
            print("Não é possível adicionar um contato sem telefone.")
       

        self.contatos.append(contato)

    def remover_contato(self, nome: str):
       
        contato_remover = None
        for cont in self.contatos:
            if cont.nome == nome:
                contato_remover = cont
                break
        
        if contato_remover:
            self.contatos.remove(contato_remover)
            return print(f"O contato{contato_remover}foi removido com sucesso")
        
        else: return print("Contato não encontrado")

    def listar_contatos(self) -> list[contato]:
       
        
        return sorted(self.contatos, key=lambda contato: contato.nome)