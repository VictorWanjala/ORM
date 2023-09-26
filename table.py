from config import CONN, CURSOR

class Cat:

    all = []

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.add_cat_to_all(self)

    @staticmethod
    def create_table():
        sql = """
              CREATE TABLE IF NOT EXISTS cats (
              id INTEGER PRIMARY KEY,
              name TEXT,
              age INTEGER,
              breed TEXT
              )
        """
        CURSOR.execute(sql)
        

    @classmethod
    def add_cat_to_all(cls, cat):
        cls.all.append(cat)

    def save(self, cursor):
        cursor.execute(
            'INSERT INTO cats (name,breed,age) VALUES(?,?,?)',
            (self.name, self.breed, self.age)
        )
        CONN.commit()

    def show_details():
        con = CURSOR.execute(
            'SELECT * FROM cats'
        )
        rows = con.fetchall()
        for vic in rows:
            if vic[0] is  'Tana' or vic[2] is not 3:
                print(vic)
        

Cat('Maru', 'scotish fold', 3)
Cat("Hana", "tortoiseshell", 1)
Cat("HON", "tortoiseshell", 1)
Cat("Tana", "scotish fold", 1)


Cat.create_table()
for cat in Cat.all:
    cat.save(CURSOR)

Cat.show_details()
