


from telefone import telefone

class contato:
  
    def __init__(self, nome: str):
        if not nome:
            print("Nome do contato não pode ser vazio.")
        self.nome = nome
        #Contato receberá uma lista de telefones
        self.telefones: list[telefone] = []

    def adicionar_telefone(self, identificador: str, numero: str):
       
        #  Evitando identificadores duplicados, que ocasionalmente poderiam acabar 
        # criando números duplicados
        for tel in self.telefones:
            if tel.identificador == identificador:
                print(f"Identificador '{identificador}' já existe para este contato.")
        
        novo_telefone = telefone(identificador, numero)
        self.telefones.append(novo_telefone)

    def remover_telefone(self, identificador: str):
       #Aqui, ele irá pegar o telefone pelo identificador, retornando caso seja feito o processo ou não
        telefone_remover = None
        for tel in self.telefones:
            if tel.identificador == identificador:
                telefone_remover = tel
                break
        
        if telefone_remover is not None:
            self.telefones.remove(telefone_remover)
            return (f"telefone{telefone_remover} foi removido")
        else:
            return ("Telefone não encontrado")

   