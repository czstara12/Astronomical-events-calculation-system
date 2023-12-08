import sqlite3

# 连接到SQLite数据库
# 数据库文件是'astronomical_database.db'，如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('astronomical_database.db')

# 创建一个Cursor对象，用于执行SQL语句
cursor = conn.cursor()

# 创建天文观测记录表
cursor.execute('''
CREATE TABLE IF NOT EXISTS astronomical_observations (
    id INTEGER PRIMARY KEY,
    observation_date DATETIME,
    location TEXT,
    celestial_body_name TEXT,
    celestial_body_type TEXT,
    observation_conditions TEXT,
    observer_name TEXT,
    notes TEXT
)
''')

# 在现有代码的基础上，添加"天文事件"表的创建
cursor.execute('''
CREATE TABLE IF NOT EXISTS astronomical_events (
    event_id INTEGER PRIMARY KEY,
    event_date DATETIME,
    event_name TEXT,
    event_type TEXT,
    event_description TEXT,
    location TEXT,
    organizer TEXT,
    notes TEXT
)
''')

# 在现有代码的基础上，添加"天体"表的创建
cursor.execute('''
CREATE TABLE IF NOT EXISTS celestial_objects (
    object_id INTEGER PRIMARY KEY,
    object_name TEXT,
    object_type TEXT,
    object_mass REAL,
    object_radius REAL,
    object_distance REAL,
    object_description TEXT,
    notes TEXT
)
''')

# 提交事务
conn.commit()

# 关闭Cursor
cursor.close()

# 关闭Connection
conn.close()

class AstronomicalObservation:
    def __init__(self, id=None, observation_date=None, location=None, celestial_body_name=None, celestial_body_type=None, observation_conditions=None, observer_name=None, notes=None):
        self.id = id
        self.observation_date = observation_date
        self.location = location
        self.celestial_body_name = celestial_body_name
        self.celestial_body_type = celestial_body_type
        self.observation_conditions = observation_conditions
        self.observer_name = observer_name
        self.notes = notes

    @staticmethod
    def get_observation_by_id(id):
        conn = sqlite3.connect('astronomical_database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM astronomical_observations WHERE id = ?', (id,))
        observation_data = cursor.fetchone()

        conn.close()

        if observation_data:
            return AstronomicalObservation(*observation_data)
        else:
            return None

    def update_database_record(self):
        conn = sqlite3.connect('astronomical_database.db')
        cursor = conn.cursor()

        # 执行 SQL 更新操作，根据对象的属性值更新数据库记录
        cursor.execute('''
        UPDATE astronomical_observations
        SET observation_date = ?, location = ?, celestial_body_name = ?, celestial_body_type = ?, 
            observation_conditions = ?, observer_name = ?, notes = ?
        WHERE id = ?
        ''', (self.observation_date, self.location, self.celestial_body_name, self.celestial_body_type,
              self.observation_conditions, self.observer_name, self.notes, self.id))

        conn.commit()
        conn.close()

    def insert_into_database(self):
        conn = sqlite3.connect('astronomical_database.db')
        cursor = conn.cursor()

        # 生成一个新的ID
        cursor.execute('SELECT MAX(id) FROM astronomical_observations')
        max_id = cursor.fetchone()[0]
        new_id = max_id + 1 if max_id is not None else 1

        # 执行 SQL 插入操作，将对象的属性值插入到数据库中
        cursor.execute('''
        INSERT INTO astronomical_observations (id, observation_date, location, celestial_body_name, celestial_body_type, 
            observation_conditions, observer_name, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (new_id, self.observation_date, self.location, self.celestial_body_name, self.celestial_body_type,
              self.observation_conditions, self.observer_name, self.notes))

        conn.commit()
        conn.close()
    
    def delete_from_database(self):
        conn = sqlite3.connect('astronomical_database.db')
        cursor = conn.cursor()

        # 执行 SQL 删除操作，根据对象的ID删除数据库记录
        cursor.execute('DELETE FROM astronomical_observations WHERE id = ?', (self.id,))
        
        conn.commit()
        conn.close()

    @staticmethod
    def get_first_observation_id():
        conn = sqlite3.connect('astronomical_database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT id FROM astronomical_observations ORDER BY id ASC LIMIT 1')
        first_id = cursor.fetchone()

        conn.close()

        if first_id:
            return first_id[0]
        else:
            return None

    @staticmethod
    def get_next_observation_id(id):
        conn = sqlite3.connect('astronomical_database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT id FROM astronomical_observations WHERE id > ? ORDER BY id ASC LIMIT 1', (id,))
        next_id = cursor.fetchone()

        conn.close()

        if next_id:
            return next_id[0]
        else:
            return None

    def get_observation_date(self):
        return self.observation_date

    def get_location(self):
        return self.location

    def get_celestial_body_name(self):
        return self.celestial_body_name

    def get_celestial_body_type(self):
        return self.celestial_body_type

    def get_observation_conditions(self):
        return self.observation_conditions

    def get_observer_name(self):
        return self.observer_name

    def get_notes(self):
        return self.notes
    
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
        
    def set_observation_date(self, observation_date):
        self.observation_date = observation_date

    def set_location(self, location):
        self.location = location

    def set_celestial_body_name(self, celestial_body_name):
        self.celestial_body_name = celestial_body_name

    def set_celestial_body_type(self, celestial_body_type):
        self.celestial_body_type = celestial_body_type

    def set_observation_conditions(self, observation_conditions):
        self.observation_conditions = observation_conditions

    def set_observer_name(self, observer_name):
        self.observer_name = observer_name

    def set_notes(self, notes):
        self.notes = notes
    

class AstronomicalEvent:
    def __init__(self, event_id=None, event_date=None, event_name=None, event_type=None, event_description=None, location=None, organizer=None, notes=None):
        self.event_id = event_id
        self.event_date = event_date
        self.event_name = event_name
        self.event_type = event_type
        self.event_description = event_description
        self.location = location
        self.organizer = organizer
        self.notes = notes


    @staticmethod
    def get_event_by_id(event_id):
        conn = sqlite3.connect('astronomical_database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM astronomical_events WHERE event_id = ?', (event_id,))
        event_data = cursor.fetchone()

        conn.close()

        if event_data:
            return AstronomicalEvent(*event_data)
        else:
            return None

    def insert_into_database(self):
        conn = sqlite3.connect('astronomical_database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT MAX(event_id) FROM astronomical_events')
        max_id = cursor.fetchone()[0]
        new_id = max_id + 1 if max_id is not None else 1

        cursor.execute('''
        INSERT INTO astronomical_events (event_id, event_date, event_name, event_type, event_description,
            location, organizer, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (new_id, self.event_date, self.event_name, self.event_type,
              self.event_description, self.location, self.organizer, self.notes))

        conn.commit()
        conn.close()

    def update_database_record(self):
        conn = sqlite3.connect('astronomical_database.db')
        cursor = conn.cursor()

        cursor.execute('''
        UPDATE astronomical_events
        SET event_date = ?, event_name = ?, event_type = ?, event_description = ?,
            location = ?, organizer = ?, notes = ?
        WHERE event_id = ?
        ''', (self.event_date, self.event_name, self.event_type,
              self.event_description, self.location, self.organizer, self.notes, self.event_id))

        conn.commit()
        conn.close()


    @staticmethod
    def get_first_event_id():
        conn = sqlite3.connect('astronomical_database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT event_id FROM astronomical_events ORDER BY event_id ASC LIMIT 1')
        first_event_id = cursor.fetchone()

        conn.close()

        return first_event_id[0] if first_event_id else None

    @staticmethod
    def get_next_event_id(current_event_id):
        conn = sqlite3.connect('astronomical_database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT event_id FROM astronomical_events WHERE event_id > ? ORDER BY event_id ASC LIMIT 1', (current_event_id,))
        next_event_id = cursor.fetchone()

        conn.close()

        return next_event_id[0] if next_event_id else None


    def delete_from_database(self):
        conn = sqlite3.connect('astronomical_database.db')
        cursor = conn.cursor()

        cursor.execute('DELETE FROM astronomical_events WHERE event_id = ?', (self.event_id,))

        conn.commit()
        conn.close()
    
    def set_event_date(self, event_date):
        self.event_date = event_date

    def get_event_date(self):
        return self.event_date

    def set_event_name(self, event_name):
        self.event_name = event_name

    def get_event_name(self):
        return self.event_name

    def set_event_type(self, event_type):
        self.event_type = event_type

    def get_event_type(self):
        return self.event_type

    def set_event_description(self, event_description):
        self.event_description = event_description

    def get_event_description(self):
        return self.event_description

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def set_organizer(self, organizer):
        self.organizer = organizer

    def get_organizer(self):
        return self.organizer

    def set_notes(self, notes):
        self.notes = notes

    def get_notes(self):
        return self.notes
    
    def get_id(self):
        return self.event_id
    
    def set_id(self, id):
        self.event_id = id

class CelestialObject:
    def __init__(self, object_id=None, object_name=None, object_type=None, object_mass=None, object_radius=None, object_distance=None, object_description=None, notes=None):
        self.object_id = object_id
        self.object_name = object_name
        self.object_type = object_type
        self.object_mass = object_mass
        self.object_radius = object_radius
        self.object_distance = object_distance
        self.object_description = object_description
        self.notes = notes


    @staticmethod
    def get_object_by_id(object_id):
        conn = sqlite3.connect('astronomical_database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM celestial_objects WHERE object_id = ?', (object_id,))
        object_data = cursor.fetchone()

        conn.close()

        if object_data:
            return CelestialObject(*object_data)
        else:
            return None

    def insert_into_database(self):
        conn = sqlite3.connect('astronomical_database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT MAX(object_id) FROM celestial_objects')
        max_id = cursor.fetchone()[0]
        new_id = max_id + 1 if max_id is not None else 1

        cursor.execute('''
        INSERT INTO celestial_objects (object_id, object_name, object_type, object_mass, object_radius, object_distance, object_description, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (new_id, self.object_name, self.object_type, self.object_mass,
              self.object_radius, self.object_distance, self.object_description, self.notes))

        conn.commit()
        conn.close()

    def update_database_record(self):
        conn = sqlite3.connect('astronomical_database.db')
        cursor = conn.cursor()

        cursor.execute('''
        UPDATE celestial_objects
        SET object_name = ?, object_type = ?, object_mass = ?, object_radius = ?, 
            object_distance = ?, object_description = ?, notes = ?
        WHERE object_id = ?
        ''', (self.object_name, self.object_type, self.object_mass, self.object_radius,
              self.object_distance, self.object_description, self.notes, self.object_id))

        conn.commit()
        conn.close()

    def delete_from_database(self):
        conn = sqlite3.connect('astronomical_database.db')
        cursor = conn.cursor()

        cursor.execute('DELETE FROM celestial_objects WHERE object_id = ?', (self.object_id,))

        conn.commit()
        conn.close()

    @staticmethod
    def get_first_object_id():
        conn = sqlite3.connect('astronomical_database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT object_id FROM celestial_objects ORDER BY object_id ASC LIMIT 1')
        first_id = cursor.fetchone()

        conn.close()

        if first_id:
            return first_id[0]
        else:
            return None

    @staticmethod
    def get_next_object_id(current_id):
        conn = sqlite3.connect('astronomical_database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT object_id FROM celestial_objects WHERE object_id > ? ORDER BY object_id ASC LIMIT 1', (current_id,))
        next_id = cursor.fetchone()

        conn.close()

        if next_id:
            return next_id[0]
        else:
            return None

    def set_object_name(self, object_name):
        self.object_name = object_name

    def get_object_name(self):
        return self.object_name

    def set_object_type(self, object_type):
        self.object_type = object_type

    def get_object_type(self):
        return self.object_type

    def set_object_mass(self, object_mass):
        self.object_mass = object_mass

    def get_object_mass(self):
        return self.object_mass

    def set_object_radius(self, object_radius):
        self.object_radius = object_radius

    def get_object_radius(self):
        return self.object_radius

    def set_object_distance(self, object_distance):
        self.object_distance = object_distance

    def get_object_distance(self):
        return self.object_distance

    def set_object_description(self, object_description):
        self.object_description = object_description

    def get_object_description(self):
        return self.object_description

    def set_notes(self, notes):
        self.notes = notes

    def get_notes(self):
        return self.notes

    def get_id(self):
        return self.object_id
    
    def set_id(self, id):
        self.object_id = id