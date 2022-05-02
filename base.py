import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS responsible_person(
   person_id INTEGER PRIMARY KEY AUTOINCREMENT,
   fullname TEXT,
   phone TEXT,
   adres TEXT);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS auditorium(
   auditorium_id INTEGER PRIMARY KEY AUTOINCREMENT,
   num INT,
   places INT,
   responsible_person INT,
   FOREIGN KEY (responsible_person) REFERENCES responsible_person(person_id));
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS central_processor(
   cpu_id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT,
   cores INT,
   frequency REAL);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS computer(
   computer_id INTEGER PRIMARY KEY AUTOINCREMENT,
   computer_name TEXT,
   cpu INT,
   memory INT,
   auditorium INT,
   FOREIGN KEY (cpu) REFERENCES central_processor(cpu_id),
   FOREIGN KEY (auditorium) REFERENCES auditorium(auditorium_id));
""")
conn.commit()

persons = [("00001", "Ivan Ivanov", "88005553535", "st. Pushkina, 15"),("00002", "Alex Ram", "89999999999", "Kubsu")]
cur.executemany("INSERT OR IGNORE INTO responsible_person VALUES(?, ?, ?, ?);", persons)
conn.commit()

auditorios = [("00001", "101", "8", "00001"),("00002", "105", "10", "00001"),("00003", "106", "12", "00002")]
cur.executemany("INSERT OR IGNORE INTO auditorium VALUES(?, ?, ?, ?);", auditorios)
conn.commit()

cpus = [("00001","AMD A10-5757M", "4", "2.5"),("00002","Intel Core i7-840QM","4","1.867"),
        ("00003","AMD A12 PRO-8800B", "4", "2.1"),("00004","Intel Xeon X5365", "4", "3.0")]
cur.executemany("INSERT OR IGNORE INTO central_processor VALUES(?, ?, ?, ?);", cpus)
conn.commit()

comps = [("00001", "comp1", "00001", "8", "00001"),("00002", "comp2", "00003", "8", "00001"),
        ("00003", "comp3", "00001", "8", "00001"),("00004", "comp4", "00002", "8", "00002"),
        ("00005", "comp5", "00004", "8", "00002"),("00006", "comp6", "00001", "8", "00002"),
        ("00007", "comp7", "00002", "8", "00002"),("00008", "comp8", "00003", "8", "00003"),
        ("00009", "comp9","00001", "4", "00003"),("00010", "comp10", "00003", "8", "00003"),
        ("00011", "comp11", "00004", "8", "00003"),("00012", "admin", "00004", "16", "00001")]
cur.executemany("INSERT OR IGNORE INTO computer VALUES(?, ?, ?, ?, ?);", comps)
conn.commit()

cur.execute("SELECT * FROM responsible_person;")
three_results = cur.fetchmany(2)
print(three_results)

input()