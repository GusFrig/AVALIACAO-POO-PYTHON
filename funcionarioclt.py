from funcionario import funcionario

class funcionarioclt(funcionario):
    
    salario_minimo = 1320.00
    
    def __init__(self, nome_completo, cpf, salario_mensal):
        # Verificação na própria classe para ver de o salário está correto
        
        if salario_mensal < self.salario_minimo:
            
            print('Valor do salário de CLT é incoerente com o valor mínimo estabelecido!')
            
        super().__init__(nome_completo, cpf, salario_mensal)
    def levantamento_de_beneficios(self) -> float:
        auxilio_alimentacao = self.salario_mensal * 0.06
        auxilio_saude = super().levantamento_de_beneficios()
        
        return auxilio_alimentacao + auxilio_saude
        