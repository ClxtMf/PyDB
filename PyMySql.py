from tkinter import N
from colorama import Cursor
import pymysql.cursors

conexao = pymysql.connect(host = 'localhost',
                          user = 'root',
                          password = 'admin',
                          database = 'escola',
                          cursorclass = pymysql.cursors.DictCursor)

"""
Inserir alunos > Abaixo
"""
nome = input('Digite o seu nome: ')
with conexao.cursor() as cursor:
    # Sql que desejamos executar
    sql = "INSERT INTO alunos (nome, curso, idade, nota)" \
          "VALUES (%s, %s, %s, %s)"

    #Tratando os parâmetros %s pelos valores que desejamos inserir
    resultado = cursor.execute(sql, (nome, 'Metaverso', 22, 6.5))
    if resultado >= 1:
        print('Aluno cadastrado com sucesso!!!')
    conexao.commit()

"""
Upgrade de alunos > Abaixo
"""
matricula = int(input('Digite a matricula que você deseja alterar: '))
with conexao.cursor() as cursor:
    # Sql que desejamos executar
    sql = "UPDATE alunos SET nome = %s, curso = %s, idade = %s, nota = %s" \
          "WHERE matricula = %s"

    #Tratando os parâmetros %s pelos valores que desejamos inserir
    cursor.execute(sql, ('Gabriel Ferreira', 'Fotografia', 27, 9.1, matricula))
    conexao.commit()


"""
Delete de alunos > Abaixo
"""
matricula = int(input('Digite a matricula do aluno: '))
with conexao.cursor() as cursor:
    # Sql que desejamos executar
    sql = "DELETE FROM alunos WHERE matricula = %s"

    #Tratando os parâmetros %s pelos valores que desejamos inserir
    cursor.execute(sql, (matricula,))
    conexao.commit()


"""
Exibição de alunos > Abaixo
"""
#Criando um cursor, o responsável por executar nossas querys
with conexao.cursor() as cursor:
    cursor.execute("SELECT * FROM alunos")

    #Separa os nossos registros linha por linha
    resultado = cursor.fetchall()
    for aluno in resultado:
        print(aluno)


conexao.close()
