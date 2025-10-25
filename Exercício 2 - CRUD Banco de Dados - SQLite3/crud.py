import sqlite3

conexao = sqlite3.connect('escola.db')

cursor = conexao.cursor()

print('conexao criada com sucesso')

cursor.execute('''
               
    CREATE TABLE IF NOT EXISTS alunos (
        id INTENGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        email TEXT NOT NULL     
    );                     
               ''')


'''cursor.execute("INSERT INTO alunos('nome', 'idade', 'email')  VALUES (?,?,?)",('Heloisa Duarte de Almeida',17, 'hdheloduarte@gmail.com'))
cursor.execute("INSERT INTO alunos('nome', 'idade', 'email')  VALUES (?,?,?)",('Guilherme Henrique da Graça',17, 'guilhermehenrique2@gmail.com'))
cursor.execute("INSERT INTO alunos('nome', 'idade', 'email')  VALUES (?,?,?)",('Aurora',18, 'auroraduartehermenildo@gmail.com'))'''

conexao.commit()
conexao.close()


consulta = cursor.execute("SELECT * FROM alunos")

for lista in consulta.fetchall():
    print(f'alunos: {lista[1]} - nome: {lista[2]} - idade: {lista[3]} - email: {lista[4]}')

print ('\n___________________________________________________________________________________________________________________________\n')

conexao.execute("SELECT * FROM alunos WHERE id = ?", (17,18,))


conexao.execute("UPDATE alunos SET nome = ? WHERE id = ?", ('Heloisa',1))

cursor.execute('DELETE from alunos WHERE id= ?', (2,))
conexao.commit()
conexao.close()


