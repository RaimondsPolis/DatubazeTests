import sqlite3

conn = sqlite3.connect("dati.db", check_same_thread=False)

def tabulas_izveide():
    cur=conn.cursor()
    # cur.execute("DROP TABLE cilveki")
    cur.execute(

        """
        CREATE TABLE skoleni(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL
        )
        """

    )
    conn.commit()
def skolotaju_tabulas_izveide():
    cur=conn.cursor()
    # cur.execute("DROP TABLE cilveki")
    cur.execute(

        """
        CREATE TABLE skolotaji(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL
        )
        """

    )

def prieksmetu_tabulas_izveide():
    cur=conn.cursor()
    # cur.execute("DROP TABLE cilveki")
    cur.execute(

        """
        CREATE TABLE prieksmeti(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        prieksmets TEXT NOT NULL
        )
        """

    )

# tabulas_izveide()
# skolotaju_tabulas_izveide()
#prieksmetu_tabulas_izveide()
def pievienot_skolenu(vards, uzvards):
    print(vards, uzvards)
    cur=conn.cursor()
    cur.execute(

        f"""
        INSERT INTO skoleni(vards, uzvards) VALUES("{vards}","{uzvards}")
        """

    )
    conn.commit()



def pievienot_skolotaju(vards, uzvards):
    cur=conn.cursor()
    cur.execute(  
        f"""
        INSERT INTO skolotaji(vards, uzvards) VALUES("{vards}","{uzvards}")
        """

    )

def pievienot_prieksmetu(prieksmets):
    cur=conn.cursor()
    cur.execute(  
        f"""
        INSERT INTO prieksmeti(prieksmets) VALUES("{prieksmets}")
        """

    )

def iegut_skolenus():
    cur=conn.cursor()
    cur.execute(
    
        f"""
        SELECT vards, uzvards FROM skoleni
        """

    )
    conn.commit()
    dati = cur.fetchall()
    return dati

def iegut_skolotajus():
    cur = conn.cursor()
    cur.execute(
        """SELECT vards, uzvards, id FROM skolotaji"""
    )
    conn.commit()
    dati = cur.fetchall()
    return dati
def iegut_prieksmetu():
    cur = conn.cursor()
    cur.execute(
        """SELECT prieksmets FROM prieksmeti """
    )
    conn.commit()
    dati = cur.fetchall()
    return dati