# AVALIACAO-POO-PYTHON
AVALIAÇÃO VIA UFC, DE PROGRAMAÇÃO ORIENTADA A OBJETOS USANDO PYTHON,


# Sistema de Gerenciamento de Folha Salarial

Este projeto é um sistema desenvolvido em Python para a gestão de funcionários e cálculos de proventos, aplicando conceitos fundamentais de **Programação Orientada a Objetos (POO)** e validação através de **Testes Unitários**.

[Image of a UML class diagram showing Employee as a base class and CLT and PJ as subclasses]

## 🏗️ Arquitetura do Sistema

O projeto está organizado em módulos que separam as responsabilidades de negócio, tipos de contratação e gestão financeira.

### 1. Modelagem de Funcionários (Herança)
* **`funcionario.py`**: A classe base que define os atributos comuns: `nome_completo`, `cpf` e `salario_mensal`. Estabelece um benefício padrão de **R$ 500,00** (Auxílio-saúde) acessível a todos os colaboradores.
* **`funcionarioclt.py`**: Subclasse para regime CLT. Define um piso salarial de **R$ 1.320,00**. O cálculo de benefícios é polimórfico: soma o auxílio-saúde base a um **Auxílio-alimentação de 6% sobre o salário mensal**.
* **`funcinariopj.py`**: Subclasse para regime PJ. Introduz o atributo `cnpj`. Diferente do regime CLT, este modelo de contrato mantém apenas o benefício padrão da classe mãe.

### 2. Gestão da Folha (`folhasalarial.py`)
Responsável por consolidar as informações financeiras da empresa:
* **Adição de Funcionários**: Permite o cadastro de diferentes tipos de funcionários em uma lista centralizada.
* **Busca por CPF**: Método que percorre os registros para retornar um dicionário com o salário e o levantamento detalhado de benefícios do colaborador.
* **Totalização**: Fornece os valores agregados da folha bruta e do somatório de benefícios de todos os cadastrados.

---

## 🧪 Qualidade e Testes (`test_folhasalarial.py`)

A integridade das regras de negócio é garantida por uma suite de testes automatizados utilizando a biblioteca `unittest`.

**Cenários testados:**
* **Validação de Cadastro**: Garante que os atributos de CLT e PJ (incluindo CNPJ) sejam instanciados corretamente.
* **Regras Salariais**: Verifica se o sistema identifica e bloqueia salários CLT abaixo do mínimo legal.
* **Cálculos Matemáticos**: Valida a precisão dos benefícios proporcionais (6% para CLT) e os totais acumulados da folha de pagamento.

---

## 🚀 Como Executar

Para validar a lógica do sistema e rodar os testes unitários, utilize o terminal:

python test_folhasalarial.py 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 📒 Sistema de Agenda de Contatos

Este projeto é uma implementação em **Python** de um sistema de gerenciamento de contatos utilizando **Programação Orientada a Objetos (POO)**. O sistema é modular, separando as responsabilidades entre a agenda, o contato e os telefones, garantindo uma estrutura limpa e organizada.

## 🗂 Estrutura do Projeto

O projeto está dividido em módulos específicos para facilitar a manutenção e a escalabilidade:

### 1. `telefone.py`
Representa a unidade mais básica do sistema.
- **Responsabilidade:** Armazenar o número e um identificador (ex: "casa", "trabalho").
- **Validação:** Garante que o número e o identificador não sejam vazios ao criar o objeto.

### 2. `contato.py`
Representa um indivíduo na agenda.
- **Atributos:** Possui um `nome` e uma lista de objetos `telefone`.
- **Funcionalidades:**
  - Adicionar telefones (com verificação de identificadores duplicados para evitar redundância).
  - Remover telefones pelo identificador.
  - *Regra de Negócio:* O nome do contato é obrigatório.

### 3. `agenda.py`
Gerencia a coleção de contatos.
- **Funcionalidades:**
  - Adicionar novos contatos.
  - Remover contatos pelo nome.
  - Listar contatos (retorna a lista ordenada alfabeticamente).
- **Regra de Negócio:** Não permite adicionar um contato à agenda se ele não possuir pelo menos um telefone vinculado.

### 4. `test_agenda.py`
Conjunto de testes unitários utilizando o framework `unittest`.
- Cobre cenários de sucesso e falha (ex: tentar adicionar contato sem telefone, duplicidade de identificadores, remoção de itens inexistentes).

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Teste:** Unittest (Biblioteca padrão)

---

## 🚀 Como Usar

Abaixo está um exemplo simples de como as classes interagem entre si, baseado na lógica dos arquivos:

```python
from agenda import agenda
from contato import contato

# 1. Instanciar a agenda
minha_agenda = agenda()

# 2. Criar um contato
novo_contato = contato("Ana")

# 3. Adicionar telefones ao contato (Obrigatório antes de ir para a agenda)
novo_contato.adicionar_telefone("celular", "11 99999-0000")
novo_contato.adicionar_telefone("trabalho", "11 3333-4444")

# 4. Adicionar o contato na agenda
minha_agenda.adicionar_contato(novo_contato)

# 5. Listar contatos
todos_contatos = minha_agenda.listar_contatos()
for c in todos_contatos:
    print(f"Nome: {c.nome}")


