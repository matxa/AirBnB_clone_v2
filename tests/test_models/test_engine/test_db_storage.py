#!/usr/bin/python3
""" Module for testing db storage"""
import MySQLdb
import unittest
from console import HBNBCommand
from os import getenv
from sqlalchemy.sql.schema import ForeignKeyConstraint
from io import StringIO
from unittest.mock import patch
from models.engine.db_storage import DBStorage
from models.city import City
from models.base_model import BaseModel
from models import storage
from models.state import State


@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "Not using database")
class testDBStorage(unittest.TestCase):
    """tests DB storage"""
    args = {
        "user": getenv('HBNB_MYSQL_USER'),
        "passwd": getenv('HBNB_MYSQL_PWD'),
        "db": getenv('HBNB_MYSQL_DB'),
        "host": getenv('HBNB_MYSQL_HOST')
    }

    def SQLconnect(self):
        """ connects to mysql """
        self.db_connection = MySQLdb.connect(**self.args)
        self.cursor = self.db_connection.cursor()

    def SQLcloseConnection(self):
        """ closes down connection """
        try:
            self.cursor.close()
            self.db_connection.close()
        except:
            pass

    def test_a(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ test for new objects """
        new = State(**{'name': 'California'})
        new.save()
        self.assertIn(new, storage.all().values())
        new.delete()

    def test_all(self):
        """ __objects is properly returned """
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_save(self):
        """ DBStorage save method """
        new = State(name="California")
        self.assertNotIn(new, storage.all().values())
        new.save()
        self.assertIn(new, storage.all().values())
        new.delete()

    def test_delete(self):
        """ tests delete method"""
        new = State(**{'name': 'California'})
        new.save()
        self.assertIn(new, storage.all().values())
        new.delete()
        self.assertNotIn(new, storage.all().values())

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        from models.state import State
        new = State(**{'name': 'California'})
        new.save()
        self.assertIn(new, storage.all().values())
        storage.reload()
        self.assertNotIn(new, storage.all().values())
        new.delete()

    def testifDict(self):
        """ tests if object is dict """
        self.assertEqual(type(storage.all()), dict)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models import DBStorage
        self.assertEqual(type(storage), DBStorage)

    def testCreateCity(self):
        """ city creation test """
        self.cursor.execute('SELECT count(*) FROM cities;')
        length1 = self.cursor.fetchone()[0]
        self.cursor.close()
        self.db_connection.close()
        state_string = 'create State id="2" name="Connecticut"'
        city_string = 'create City id="1" state_id="2" name="New Haven"'
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(state_string)
            HBNBCommand().onecmd(city_string)
        self.db_connection = MySQLdb.connect(**self.args)
        self.cursor = self.db_connection.cursor()
        self.cursor.execute(
            'SELECT count(*) FROM cities WHERE state_id = 2;')
        length2 = self.cursor.fetchone()[0]
        self.assertEqual(length1 + 1, length2)

    def testCreatePlace(self):
        """ Tests Place creation """
        self.cursor.execute('SELECT count(*) FROM places;')
        length1 = self.cursor.fetchone()[0]
        self.cursor.close()
        self.db_connection.close()
        state_string = 'create State id="1" name="California"'
        city_string = 'create City id="2" state_id="1" name="Fremont"'
        user_string = 'create User id="42" email="42@gmail.com" password="pwd"'
        place_string = 'create Place user_id="42" city_id="2" name="Rad_Place"'
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(state_string)
            HBNBCommand().onecmd(city_string)
            HBNBCommand().onecmd(user_string)
            HBNBCommand().onecmd(place_string)
        self.db_connection = MySQLdb.connect(**self.args)
        self.cursor = self.db_connection.cursor()
        self.cursor.execute('SELECT count(*) FROM places;')
        length2 = self.cursor.fetchone()[0]
        self.assertEqual(length1 + 1, length2)

    def testDeleteState(self):
        """ Tests deleting a state with delete method """
        new = State(name="New Mexico", id="13")
        new.save()
        self.assertIn(new, storage.all().values())
        new.delete()
        self.assertNotIn(new, storage.all().values())

    def testDeleteCity(self):
        """ Tests deleting cities """
        new_state = State(name="Californiao", id="5280", cities=[
                          City(name="Denver", id="22", state_id="5280")])
        new_state.save()
        self.assertIn('cities', new_state.to_dict())
        new_state.delete()
        self.assertNotIn('cities', storage.all().values())

    def test_storage_type(self):
        """ Tests if storage type is db """
        self.assertEqual(type(storage), DBStorage)
