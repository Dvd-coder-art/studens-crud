import mysql.connector 

conexao = mysql.connector.connect(
    host='localhost',
    user="root",
    password="root",
    database="bdpython"
  )

cursor=conexao.cursor()

cursor.execute('INSERT INTO tabletest (name, age) VALUES ("David", "18")')
conexao.commit()

cursor.execute('SELECT * FROM tabletest')
resultado = cursor.fetchone()
print(resultado)

cursor.close()
conexao.close()

