import sqlite3

# 连接到SQLite数据库
# 数据库文件是'tracks_database.db'，如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('tracks_database.db')

# 创建一个Cursor对象，用于执行SQL语句
cursor = conn.cursor()

# "轨道参数"表的创建
cursor.execute('''
CREATE TABLE IF NOT EXISTS orbital_parameters (
    id INTEGER PRIMARY KEY,
    name TEXT,
    data_format TEXT,
    line_1 TEXT,
    line_2 TEXT,
    line_3 TEXT,
    description TEXT
)
''')

# 提交事务
conn.commit()

# 关闭Cursor
cursor.close()

# 关闭Connection
conn.close()

class OrbitalParameter:
    def __init__(self, id=None, name=None, data_format=None, line_1=None, line_2=None, line_3=None, description=None):
        self.id = id
        self.name = name
        self.data_format = data_format
        self.line_1 = line_1
        self.line_2 = line_2
        self.line_3 = line_3
        self.description = description

    @staticmethod
    def get_parameter_by_id(id):
        conn = sqlite3.connect('tracks_database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM orbital_parameters WHERE id = ?', (id,))
        param_data = cursor.fetchone()

        conn.close()

        if param_data:
            return OrbitalParameter(*param_data)
        else:
            return None

    def insert_into_database(self):
        conn = sqlite3.connect('tracks_database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT MAX(id) FROM orbital_parameters')
        max_id = cursor.fetchone()[0]
        new_id = max_id + 1 if max_id is not None else 1

        cursor.execute('''
        INSERT INTO orbital_parameters (id, name, data_format, line_1, line_2, line_3, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (new_id, self.name, self.data_format, self.line_1, 
              self.line_2, self.line_3, self.description))

        conn.commit()
        conn.close()

    def update_database_record(self):
        conn = sqlite3.connect('tracks_database.db')
        cursor = conn.cursor()

        cursor.execute('''
        UPDATE orbital_parameters
        SET name = ?, data_format = ?, line_1 = ?, line_2 = ?, 
            line_3 = ?, description = ?
        WHERE id = ?
        ''', (self.name, self.data_format, self.line_1, self.line_2, 
              self.line_3, self.description, self.id))

        conn.commit()
        conn.close()

    def delete_from_database(self):
        conn = sqlite3.connect('tracks_database.db')
        cursor = conn.cursor()

        cursor.execute('DELETE FROM orbital_parameters WHERE id = ?', (self.id,))

        conn.commit()
        conn.close()

    # Getters
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_data_format(self):
        return self.data_format

    def get_line_1(self):
        return self.line_1

    def get_line_2(self):
        return self.line_2

    def get_line_3(self):
        return self.line_3

    def get_description(self):
        return self.description

    # Setters
    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_data_format(self, data_format):
        self.data_format = data_format

    def set_line_1(self, line_1):
        self.line_1 = line_1

    def set_line_2(self, line_2):
        self.line_2 = line_2

    def set_line_3(self, line_3):
        self.line_3 = line_3

    def set_description(self, description):
        self.description = description
        
    @staticmethod
    def get_all_parameters():
        conn = sqlite3.connect('tracks_database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM orbital_parameters')
        all_params = cursor.fetchall()

        conn.close()

        parameters = []
        for param in all_params:
            parameters.append(OrbitalParameter(*param))

        return parameters
    
    @staticmethod
    def get_parameter_by_name(name):
        conn = sqlite3.connect('tracks_database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM orbital_parameters WHERE name = ?', (name,))
        param_data = cursor.fetchone()

        conn.close()

        if param_data:
            return OrbitalParameter(*param_data)
        else:
            return None