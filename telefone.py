
class telefone:
   
    def __init__(self, identificador: str, numero: str):
        #Como poderemos remover um telefone pelo seu identificador,  é intererssante fazer uma 
        #condicional para verificar se existe identificador para tal telefone
        if not identificador:
            print("Identificador não pode ser vazio.")
        if not numero:
            print("Número não pode ser vazio.")
            
        self.identificador = identificador
        self.numero = numero

   