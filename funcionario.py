class funcionario:
   
    def __init__(self, nome_completo: str, cpf: str, salario_mensal: float):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.salario_mensal = salario_mensal

    
    def levantamento_de_beneficios(self) -> float:
        #Todos os funcionários tem direito ao auxilio-saúde
        return 500.00