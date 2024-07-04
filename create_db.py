import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def setup_db():
    """
        Crea la BD utilizando los datos que se encuentran en el archivo db_info.json, el cual está encriptado para que no se pueda obtener la información sensible de acceso a la BD.
    """

 db = mysql.connector.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
    )
    mycursor = db.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS drive_inventory")

    mycursor = db.cursor()
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS Files (file_id VARCHAR(255) PRIMARY KEY, mimeType VARCHAR(50), title VARCHAR(100) NOT NULL, owner VARCHAR(50), access VARCHAR(20), ownerEmail VARCHAR(50), modifiedDate DATETIME, wasPublic BOOL)"
    )
    db.commit()

    #return db