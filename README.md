# 📊 Pesquisa de Opinião - TudoWeb

Projeto acadêmico desenvolvido em Python para realizar uma pesquisa de satisfação sobre o atendimento da empresa fictícia **TudoWeb**.

## 🎯 Objetivo

Coletar respostas de até **50 entrevistados**, registrando:

- Nome;
- Idade;
- Opinião sobre o atendimento.

As opções são:

- ⭐ Excelente
- 👍 Bom
- 😞 Ruim

Ao final, o programa contabiliza cada tipo de resposta e o total de respostas recebidas.

## 🛠️ Tecnologias

- Python 3
- Streamlit
- GitHub

## 📁 Estrutura do projeto

```text
pesquisa-opiniao-tudoweb/
├── app.py
├── main.py
├── README.md
├── requirements.txt
└── testes/
    └── teste_10_entrevistados.txt
```

### `app.py`
Versão com interface web desenvolvida em Streamlit.

### `main.py`
Versão em Python puro, utilizada para demonstrar a estrutura de repetição `for` e as estruturas de decisão `if`, `elif` e `else`.

### `requirements.txt`
Lista a biblioteca necessária para executar a interface.

### `testes/`
Contém o registro do teste realizado com 10 entrevistados.

## 🧪 Teste de validação

Para validar o funcionamento, foi definido um teste com 10 respostas:

- ⭐ Excelente: 4
- 👍 Bom: 3
- 😞 Ruim: 3
- 📋 Total: 10

## ▶️ Como executar o Streamlit

Instale as dependências:

```bash
pip install -r requirements.txt
```

Depois execute:

```bash
streamlit run app.py
```

O Streamlit abrirá a aplicação no navegador.

## 📚 Conceitos aplicados

- Variáveis;
- Entrada de dados;
- Saída de dados;
- Estrutura de repetição `for`;
- Estruturas de decisão `if`, `elif` e `else`;
- Contadores;
- Operadores;
- Interface web com Streamlit.

## 🚀 Possíveis melhorias

- Permitir o envio de sugestões diretamente pela interface;
- Exibir porcentagens de cada avaliação;
- Criar gráficos com os resultados;
- Adicionar botão para reiniciar a pesquisa;
- Exportar os resultados para um arquivo.

## 🎓 Projeto acadêmico

Projeto desenvolvido para aplicação dos conhecimentos de algoritmos, programação estruturada e desenvolvimento de aplicações em Python.
