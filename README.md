# Registrador-de-produtos-estoque
Neste projeto, foquei em aprofundar meu domínio sobre funções em Python e boas práticas de modularização. Implementei rotinas estruturadas para captura, validação e inserção de dados, reforçando a organização e a reutilização de código.

## 🎯 Objetivos do Projeto
* Praticar a modularização de código por meio do isolamento de funções com responsabilidades únicas.
* Utilizar estruturas de dados baseadas em tabelas hash (dicionários aninhados) para consultas eficientes de produtos.
* Implementar validações de entrada e formatação consistente de dados textuais.

## ⚙️ Funcionalidades
- **Cadastro de Produtos:** Registro com verificação prévia de duplicidade, quantidade em estoque e valor unitário.
- **Consulta de Inventário:** Busca direta pela chave do produto com tratamento para itens não localizados.
- **Formatação de Saída:** Normalização de strings (`strip()`, `lower()`, `title()`) e formatação monetária padrão BRL.
- **Interface Interativa:** Menu em loop contínuo com opções de navegação e tratamento para opções inválidas.

## 🛠️ Tecnologias e Estruturas Utilizadas
* **Python 3.x**
* **Dicionários Aninhados (Hash Maps):** Estrutura `dict` para armazenamento dos produtos com complexidade de busca otimizada ($O(1)$).
* **Funções com Escopo Local e Parâmetros:** Isolamento da lógica de persistência e consulta sem dependência direta de variáveis globais.
