import os
import re
import mysql.connector
from dotenv import load_dotenv 

load_dotenv

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        database=os.getenv('DB_NAME')
        )




# Cadastro alunos
class Alunos:
  def __init__(self):
      self.nome = ""
      self.matricula = ""
      self.nota = 0.0


  def cadastrar(self):
      conexao = conectar()
      cursor = conexao.cursor()
      self.nome = input("Digite o nome do aluno: ")
      self.matricula = str(input("Digite a matrícula do aluno: "))
      cursor.execute('SELECT matricula FROM tabelanota')
      matriculas = [m[0] for m in cursor.fetchall()]
      
    
      while self.matricula in matriculas:
          print("Matrícula já cadastrada. Digite outra matrícula.")
          self.matricula = input("Digite a matrícula do aluno: ")
      matriculas.append(self.matricula)
      print("Aluno cadastrado com sucesso!")

      #Cadastrar nota
      while True:
            try:
                nota_str = input(f"Digite a nota de {self.nome}: ")
                nota_str = nota_str.replace(",", ".")
                nota = float(nota_str)

                if 0 <= nota <= 10:
                    self.nota = nota
                    print("Nota cadastrada com sucesso!")
                    cursor.execute(f'INSERT INTO tabelanota (nome,matricula,nota) VALUES ("{self.nome}","{self.matricula}","{self.nota}")')
                    conexao.commit()
                      
            
                    break
                else:
                    print("Nota inválida! Digite um valor entre 0 e 10.")

            except ValueError:
                print("Entrada inválida! Digite um número válido.")
      cursor.close()
      conexao.close()
      
  def deletarAluno(self):
      conexao = conectar()
      cursor = conexao.cursor()
      self.matricula = input("Digite a Matrícula do aluno para deletar:")
      cursor.execute('SELECT matricula FROM tabelanota')
      self.matriculas = [m[0] for m in cursor.fetchall()]

      while self.matricula not in self.matriculas:
         print("Matrícula não encontrada.")    
         print(self.matriculas)
         self.matricula = input("Digite a Matrícula do aluno para deletar:")

      cursor.execute(f'DELETE FROM tabelanota WHERE matricula="{self.matricula}"')
      conexao.commit() 
      print("Matrícula deletada com sucesso!")
      
      cursor.close()
      conexao.close()
        

      
  def listarAlunos(self):
      conexao = conectar()
      cursor = conexao.cursor()
      cursor.execute('SELECT * FROM tabelanota')
      resultados = cursor.fetchall()
      for linha in resultados:
          id,nome,matricula,nota = linha 
          print(f"Id:{id} ,Nome:{nome}, Matricula:{matricula}, Nota: {nota}")
      
      conexao.close()
      cursor.close()


  def updateNota(self):
        conexao = conectar()
        cursor = conexao.cursor()
        self.matricula = input("Digite a Matrícula do aluno para atualizar nota:")
        cursor.execute('SELECT matricula FROM tabelanota')
        self.matriculas = [m[0] for m in cursor.fetchall()]

        while self.matricula not in self.matriculas:
            print("Matrícula não encontrada.")    
            print(self.matriculas)
            self.matricula = input("Digite a Matrícula do aluno para atualizar: ")
            
        nota_nova = float(input("Digit a nova nota: "))
        while nota_nova > 10.0 or nota_nova <0.0:
            nota_nova = float(input("Digite nota de 0 a 10: "))

        nota_new= str(nota_nova)
        cursor.execute('UPDATE tabelanota SET nota=%s WHERE matricula= %s',(nota_new,self.matricula))
        conexao.commit()
        conexao.close()
        cursor.close()
        print("Nota atualizada")
        
         

        


  def imprimir(self):
        arquivo = open(f"Notas.txt", "a")

        arquivo.write("--------Boletim--------\n")
        arquivo.write(f"Nome: {self.nome} | Matrícula: {self.matricula}\n")
        arquivo.write(f"Notas: {self.nota}\n")
        arquivo.write("------------------------\n")

        arquivo.close()

        print("Arquivo Salvo com sucesso!")





def limpar_tela():
  os.system('cls' if os.name == 'nt' else 'clear')


aluno = Alunos()
aluno.listarAlunos()
aluno.updateNota()

# while True:
#   resposta = input("Deseja cadastrar um novo aluno? (s/n): ")
#   print(resposta)
#   if resposta.lower() == "s":
#     aluno = Alunos()
#     aluno.cadastrar()
#     aluno.imprimir()
#     limpar_tela()
    
#   else:
#     resposta= input("Deseja deletar?(s/n): ")
#     if resposta.lower() == "s":
#         aluno = Alunos()
#         aluno.deletarAluno()
        
#     else:
#         break
        
          
      
  




