import sqlite3

conexao = sqlite3.connect('escola.db')

cursor = conexao.cursor()

print('conexao criada com sucesso')

cursor.execute('''
               
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        email TEXT NOT NULL     
    );                     
               ''')


'''cursor.execute("INSERT INTO alunos('nome', 'idade', 'email')  VALUES (?,?,?)",('Heloisa Duarte de Almeida',17, 'hdheloduarte@gmail.com'))
cursor.execute("INSERT INTO alunos('nome', 'idade', 'email')  VALUES (?,?,?)",('Guilherme Henrique da Graça',17, 'guilhermehenrique2@gmail.com'))
cursor.execute("INSERT INTO alunos('nome', 'idade', 'email')  VALUES (?,?,?)",('Aurora',18, 'auroraduartehermenildo@gmail.com'))'''


consulta = cursor.execute("SELECT * FROM alunos")

for lista in consulta.fetchall():
    print(f'alunos: {lista[0]} - nome: {lista[1]} - idade: {lista[2]} - email: {lista[3]}')

print ('\n___________________________________________________________________________________________________________________________\n')

consulta2 = cursor.execute("SELECT * FROM alunos WHERE id = ?", (2,))
print('Pesquisa por ID')
for lista2 in consulta2.fetchall():
    print(f'alunos: {lista2[0]} - nome: {lista2[1]} - idade: {lista2[2]} - email: {lista2[3]}')



'''conexao.execute("UPDATE alunos SET nome = ? WHERE id = ?", ('Heloisa',1))'''

'''cursor.execute('DELETE from alunos WHERE id = ?', (2))'''
conexao.commit()
conexao.close()


