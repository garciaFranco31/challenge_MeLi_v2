from initialize import initialize
from create_db import setup_db
from db_handling import saving_files, modified_public_files


def main():
    setup_db()
    saving_files()
    modified_public_files()

if __name__ == "__main__":
    initialize()
    print("Cargando archivos y haciendo modificaciones...")
    main()
    print("Finalizado...")