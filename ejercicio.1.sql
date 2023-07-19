#Crea las siguientes consultas SQL:
#Obtener el id del usuario que su nombre es Juan.
"SELECT id FROM estudiantes WHERE nombre = 'Juan';"
#Inserta en la base de datos, el usuario Juan, con nombre, apellido y correo. La tabla tiene auto númerico.
"INSERT INTO estudiantes (nombre, apellido, correo) VALUES ('Juan', 'Garcia', 'JuanGarcia@juan.com');"
#Actualizar el campo edad de Juan a 60 años.
"UPDATE estudiantes SET age = 60 WHERE name = 'Juan';"
