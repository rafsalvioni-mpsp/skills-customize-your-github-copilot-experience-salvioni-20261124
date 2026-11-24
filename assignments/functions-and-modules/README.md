# 📘 Atividade: Funções e Módulos

## 🎯 Objetivo

Escrever funções reutilizáveis com parâmetros e valores de retorno, e organizar o código em módulos que são importados por outro arquivo Python.

## 📝 Tarefas

### 🛠️ Criar funções com retorno

#### Descrição
Implemente as funções do [starter code](starter-code.py) que recebem dados, processam e retornam um resultado. Não use `print` dentro delas.

#### Requisitos
O programa concluído deve:

- Implementar `calcular_media(notas)`, que retorna a média de uma lista de números
- Implementar `encontrar_maior(numeros)`, que retorna o maior valor de uma lista
- Retornar `None` em `calcular_media` quando a lista estiver vazia

Exemplo:

```python
calcular_media([6, 8, 10])  # 8.0
```


### 🛠️ Usar parâmetros padrão

#### Descrição
Crie uma função com um parâmetro opcional e chame-a com e sem esse argumento.

#### Requisitos
O programa concluído deve:

- Implementar `saudacao(nome, prefixo="Olá")`, que retorna a string `"<prefixo>, <nome>!"`
- Retornar `"Olá, Ana!"` ao chamar `saudacao("Ana")`
- Retornar `"Oi, Ana!"` ao chamar `saudacao("Ana", prefixo="Oi")`


### 🛠️ Organizar o código em módulos

#### Descrição
Mova as funções para um módulo separado e importe-as de um programa principal.

#### Requisitos
O programa concluído deve:

- Criar um arquivo `utilidades.py` contendo as três funções
- Criar um arquivo `main.py` que importa essas funções com `from utilidades import ...`
- Executar a lógica de teste somente dentro de `if __name__ == "__main__":`
