from google_drive import obtaining_files

import mysql.connector
import os
from dotenv import load_dotenv
from send_email import send_email

load_dotenv()

def saving_files():
    """
    Función encargada de almacenar los archivos obtenidos desde google drive en la base de datos.

    Almacena:
        - file_id: id del archivo
        - mimeType: extensión del archivo
        - title: titulo del archivo
        - owner: creador del archivo
        - modified_date: fecha de última modificación
        - acces: si es public o private
        - was_public: si el archivo fue publico alguna vez
    """
    files = obtaining_files()

    db = mysql.connector.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE"),
    )

    try:
        for file in files:
            if (file[4] == True):
                file_access = "Public"
            elif (file[4] == False):
                file_access = "Private"
            mycursor = db.cursor()
            mycursor.execute(
                "INSERT INTO files (file_id, mimeType, title, owner, access, ownerEmail, modifiedDate, wasPublic) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (file[0], file[1], file[2], file[3], file_access, file[5], file[6], False),
            )
            db.commit()
    except mysql.connector.errors.IntegrityError as e:
        print("Los archivos ya fueron cargados, modificando archivos publicos")


def modified_public_files():
    """
        Función encargada de modificar el acceso a un archivo:
            Si el archivo es de acceso público, lo modifica para que sea de acceso privado.
    """
    db = mysql.connector.connect(
   db = mysql.connector.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE"),
    )

    cursor_files = db.cursor()
    cursor_files.execute("SELECT file_id, access, wasPublic, ownerEmail, title FROM files")
    
    result = cursor_files.fetchall()
    for res in result:
        if (res[1] == 'Public'):
            id_file = res[0]
            cursor_files.execute("UPDATE files SET access = 'Private', wasPublic= %s WHERE file_id = %s",(True, id_file))
            db.commit()
            send_email(res[3], res[4])


