from funcionario import funcionario
class funcionarioPJ(funcionario):
    
    def __init__(self, nome_completo, cpf, salario_mensal, cnpj):
        # O super chamando os atributos da classe principal funcionário. Aqui precisaremos adicionar uma 
        #informação a mais a classe PJ: cnpj
        super().__init__(nome_completo, cpf, salario_mensal)
        self.cnpj = cnpj
    def levantamento_de_beneficios(self) -> float:
        # Como o PJ não tem direito a vale-refeição, só um super para chamar o que esse método
        # faz na classe mãe
        return super().levantamento_de_beneficios()