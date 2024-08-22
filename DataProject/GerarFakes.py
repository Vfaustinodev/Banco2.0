import sqlite3
from faker import Faker 
import os
from random import randint

PATH_FILE_DIR = os.path.dirname(__file__)

locales = 'pt-BR'
fake = Faker(locales)



try:
    connect = sqlite3.connect(PATH_FILE_DIR+'/users_registed.db')
    cursor = connect.cursor()

except:
    print('NÃO FOI FEITA A CONEXÃO COM O BANCO DE DADOS')
    exit()

for repeat in range(10):

    fake_name = fake.name()
    fake_number = fake.cellphone_number()
    fake_user = fake.user_name()
    fake_pass = fake.password()
    fake_age = randint(0, 120)
    fake_country = fake.country()
    fake_birth = randint(1940, 2025)
    fake_cpf = fake.cpf()
    fake_email = fake.free_email()
    fake_registed = '00:00:00'
    fake_gender = 'Outros'
    fake_date = '05/08/2024'
    #Enviando as informações obtidas na entrada para o banco de dados.
    cursor.execute(f'''INSERT INTO tb_users_registed
    (name_registed, phone_number, login_user, password_user, age, country, year_of_birthday, cpf_user, email_user, registed_hour, gender_user, registed_date) 
    VALUES ('{fake_name}', '{fake_number}', '{fake_user}', '{fake_pass}', '{fake_age}', '{fake_country}',
    '{fake_birth}', '{fake_cpf}', '{fake_email}',
    '{fake_registed}', '{fake_gender}', '{fake_date}')
    ''')
#Confirmando o envio dos dados ao Banco de Dados.
connect.commit()