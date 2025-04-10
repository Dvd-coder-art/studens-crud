# 🧩 Desafio: Sistema de Notas com Relatórios e Atualização de Dados
Seu objetivo é evoluir o sistema atual para um sistema de gerenciamento de notas com as seguintes funcionalidades novas:

## ✅ 1. Listar todos os alunos cadastrados
Crie um método listarAlunos() que busque e imprima no terminal todos os alunos cadastrados com nome, matrícula e nota.

Dica: `SELECT * FROM tabelanota`

## ✅ 2. Atualizar nota de um aluno
Crie um método atualizarNota() que:

- Solicite a matrícula do aluno;

- Verifique se a matrícula existe;

- Permita atualizar a nota com as mesmas validações de antes (entre 0 e 10);

- Atualize no banco e imprima uma confirmação.

Dica: `UPDATE tabelanota SET nota = ? WHERE matricula = ?`

## ✅ 3. Gerar relatório com média geral da turma
Crie um método gerarRelatorio() que:

- Calcule a média geral das notas dos alunos;

- Identifique o aluno com maior e menor nota;

- Imprima essas informações no terminal e salve num arquivo `relatorio.txt`.

Dica: use `AVG(nota)`, `MAX(nota)` e `MIN(nota)` no SQL.

## ✅ 4. Evitar SQL Injection
Troque os comandos com f-strings por placeholders seguros:

```
cursor.execute("INSERT INTO tabelanota (nome, matricula, nota) VALUES (%s, %s, %s)", (self.nome, self.matricula, self.nota))
```

## ✅ 5. Desafio bônus (nível ninja 🥷)
Organize tudo em um menu principal com as opções:

```
[1] Cadastrar aluno
[2] Deletar aluno
[3] Atualizar nota
[4] Listar alunos
[5] Gerar relatório
[6] Sair
```
Use while True com input() para escolher as opções dinamicamente.

