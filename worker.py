def workerr(path):
    print(path)
    import sqlite3
    #path = r''
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("""
    create table if not exists cadastro(
        restart integer default 0
    );
    """)
    return True

if __name__ == '__main__':
    workerr(1)
else:
    pass