from funcionario import funcionario

class folhasalarial:
    def __init__(self):
        self.funcionarios = []
    
    def adicionar_funcionario_a_folha_salarial(self, funcionario: funcionario):
       
        self.funcionarios.append(funcionario)
        
    def recuperar_dados_funcionario_pelo_cpf(self, cpf: str):
       # Aqui cria-se um laço para verificar, dentro do dicionario funcionarios, a busca de um certo
       # funcionario pelo seu CPF
        for x in self.funcionarios:
            if x.cpf == cpf:
                return {
                    "cpf": x.cpf,
                    "salario": x.salario_mensal,
                    "beneficios": x.levantamento_de_beneficios()
                }
            else:
                print("Funcionário não existe no banco de arquivos!")
        return None
    # Métodos de verificação dos salários e beneficios através do dicionario 'funcionarios'
    def calcular_total_folha_salarial(self) -> float:
        
        return sum(x.salario_mensal for x in self.funcionarios)

    def calcular_total_beneficios(self) -> float:
       
        return sum(x.levantamento_de_beneficios() for x in self.funcionarios)
        