import os
import pickle
import unittest
from tkinter import TclError, Tk
from tkmacosx import ColorVar, DictVar, SaveVar
from test.support import findfile


class TestBase(unittest.TestCase):

    _filename = findfile('testSaveVar.pkl')

    def checkSavefile(self, var, filename):
        with open(filename, 'rb') as file:
            d = pickle.load(file)
            if d.get(str(var)):
                return d[str(var)]

    def remove_file(self):
        if os.path.exists(self._filename):
            os.remove(self._filename)

    def setUp(self):
        self.remove_file()
        self.root = Tk()

    def tearDown(self):
        del self.root
        self.remove_file()


class TestColorVar(TestBase):

    def test_default(self):
        v = ColorVar(self.root)
        self.assertEqual("white", v.get())

    def test_get(self):
        v = ColorVar(self.root, "#333", "name")
        self.assertEqual("#333", v.get())
        self.root.globalsetvar("name", "#ff0000")
        self.assertEqual("#ff0000", v.get())

    def test_invalid_value(self):
        v = ColorVar(self.root, "#00ff00", "name")
        self.root.globalsetvar("name", "value")
        with self.assertRaises((ValueError, TclError)):
            v.get()


class TestDictVar(TestBase):

    def test_default(self):
        v = DictVar(self.root)
        self.assertEqual({}, v.get())

    def test_get(self):
        v = DictVar(self.root, {'1': 'abc'}, 'name')
        self.assertEqual({'1': 'abc'}, v.get())
        self.root.globalsetvar("name", {2: 'xyz'})
        self.assertEqual({2: 'xyz'}, v.get())


class TestSaveVar(TestBase):
    _default = 'blue'

    def _create(self, **kw):
        return SaveVar(
            var=kw.get('var', ColorVar),
            master=kw.get('master', self.root),
            value=kw.get('value', self._default),
            name=kw.get('name', 'name'),
            filename=kw.get('filename', self._filename))

    def test_default(self):
        v = self._create()
        self.assertEqual(
            self._default, self.checkSavefile(v, self._filename)[0])
        self.assertEqual(
            self._default, self.checkSavefile(v, self._filename)[1])

    def test_saved_value(self):
        v = self._create()
        v.set('#15234d')
        self.assertEqual("#15234d", v.get())
        self.assertEqual(v.get(), self.checkSavefile(v, self._filename)[0])
        self.assertEqual(
            self._default, self.checkSavefile(v, self._filename)[1])

    def test_file_created(self):
        v = self._create()
        file = open(self._filename, 'r')
