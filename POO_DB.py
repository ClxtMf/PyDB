import pymysql.cursors


class Aluno:
    def __init__(self, nome, idade, curso, nota):
        self.nome = nome
        self.curso = curso
        self.idade = idade
        self.nota = nota
        self.matricula = 0

#DAO (DATA ACCESS OBJECT)
class DAO:
    def __init__(self):
        self.conexao = pymysql.connect(host='localhost',
                                  user='root',
                                  password='',
                                  database='escola',
                                  cursorclass=pymysql.cursors.DictCursor)

    def inserir(self, aluno):
        with self.conexao.cursor() as cursor:
            # Sql que desejamos executar
            sql = "INSERT INTO alunos (nome, curso, idade, nota)" \
                  "VALUES (%s, %s, %s, %s)"


            # Tratando os parâmetros %s pelos valores que desejamos inserir
            cursor.execute(sql, (aluno.nome,
                           aluno.curso,
                           aluno.idade,
                           aluno.nota))

            self.conexao.commit()

aluno = Aluno('Carmelita', 16, 'Fotografia', 7.8)
dao = DAO()
dao.inserir(aluno)
