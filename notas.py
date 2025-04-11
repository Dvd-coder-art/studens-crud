import os
import re
import mysql.connector
from dotenv import load_dotenv 

load_dotenv()

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        database=os.getenv('DB_NAME'),
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
                    cursor.execute('INSERT INTO tabelanota (nome,matricula,nota) VALUES (%s,%s,%s)',(self.nome,self.matricula,self.nota))
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

      cursor.execute('DELETE FROM tabelanota WHERE matricula=%s', (self.matricula))
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
            
        nota_nova = input("Digit a nova nota: ")
        nota_float = float(nota_nova.replace(",", "."))
        
        while nota_float > 10.0 or nota_float <0.0:
            nota_nova = input("Digite nota de 0 a 10: ")
            nota_float = float(nota_nova.replace(",", "."))

        nota_new= str(nota_float)
        cursor.execute('UPDATE tabelanota SET nota=%s WHERE matricula= %s',(nota_float,self.matricula))
        conexao.commit()
        conexao.close()
        cursor.close()
        print("Nota atualizada")
        
         

  def gerarRelatorio(self):
      conexao = conectar()
      cursor = conexao.cursor()
      cursor.execute("SELECT nota FROM tabelanota")
      resultado = [float(m[0]) for m in cursor.fetchall()]
      tamanho = len(resultado)
      self.soma = sum(resultado)/tamanho
      
      self.maior_nota = resultado[0]

      for i in range(1,(len(resultado))):
          self.maior_nota = max(resultado)
          if(resultado[i] > self.maior_nota):
             self.maior_nota =  resultado[i]

      self.menor_nota = min(resultado)
      
    
          
      cursor.close()
      conexao.close()

      print(f"""
            Média da turma: {self.soma:.1f}\n
            Maior nota da Turma: {self.maior_nota}\n
            Menor nota da Turma: {self.menor_nota}\n
            """)
      
      
  def imprimir(self):
        
        arquivo = open(f"Relatorio.txt", "a")

        arquivo.write("--------Boletim--------\n")
        arquivo.write(f"Menor Nota: {self.menor_nota}\n")
        arquivo.write("------------------------\n")
        arquivo.write(f"Maior Nota: {self.maior_nota}\n")
        arquivo.write("------------------------\n")
        arquivo.write(f"Média da turma: {self.soma:.1f}\n")

        arquivo.close()

        print("Arquivo Salvo com sucesso!")    
      


  




def limpar_tela():
  os.system('cls' if os.name == 'nt' else 'clear')




while True:
    print("""[1] Cadastrar aluno\n
    [2] Deletar aluno\n
    [3] Atualizar nota\n
    [4] Listar alunos\n
    [5] Gerar relatório\n
    [6] Sair\n
          """)
    resposta = input("Escolha uma opção: ")
    if resposta == "1":
        aluno = Alunos()
        aluno.cadastrar()
        limpar_tela()
    
    elif resposta == "2":
        resposta= input("Deseja deletar?(s/n): ")
        aluno = Alunos()
        aluno.deletarAluno()
        
         
    
    elif resposta == "3":
        aluno = Alunos()
        aluno.updateNota()
        

    elif resposta == "4":
        aluno = Alunos()
        aluno.listarAlunos()
        
        

    elif resposta == "5":
        aluno = Alunos()
        aluno.gerarRelatorio()
        aluno.imprimir()
        

    elif resposta == "6":
        
        print("Até outro dia!")
        break 
        
          
      
  




