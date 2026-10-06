"""Exercise actual UI callbacks against shared temporary storage."""
import os
import sys
import tempfile
import unittest
from pathlib import Path

os.environ['QT_QPA_PLATFORM'] = 'offscreen'
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import tkinter as tk
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
from backend import TaskStore
from tkinter_ui import TaskWindow as TkWindow
from pyqt_ui import TaskWindow as QtWindow


class IntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        path = Path(self.temp.name) / 'tasks.db'
        self.tk_store, self.qt_store = TaskStore(path), TaskStore(path)
        self.root = tk.Tk()
        self.root.withdraw()
        self.tk = TkWindow(self.root, self.tk_store)
        self.qt = QtWindow(self.qt_store)

    def tearDown(self):
        self.qt.close()
        self.root.destroy()
        self.tk_store.close()
        self.qt_store.close()
        self.temp.cleanup()

    def test_cross_interface_add_toggle_delete(self):
        self.tk.entry.insert(0, 'Prepare Lab 4')
        self.tk.add()
        self.qt.refresh()
        self.assertEqual(self.qt.tasks.count(), 1)
        self.assertIn('Prepare Lab 4', self.qt.tasks.item(0).text())
        self.qt.tasks.setCurrentRow(0)
        self.qt.change('toggle')
        self.tk.refresh()
        item = self.tk.tree.get_children()[0]
        self.assertEqual(self.tk.tree.item(item)['values'][1], 'Done')
        self.tk.tree.selection_set(item)
        self.tk.change('delete')
        self.qt.refresh()
        self.assertEqual(self.qt.tasks.count(), 0)

    def test_pyqt_add_and_persistence(self):
        self.qt.entry.setText('  Review Git  ')
        self.qt.add()
        self.tk.refresh()
        self.assertEqual(self.tk_store.list_tasks()[0][1], 'Review Git')
        reopened = TaskStore(Path(self.temp.name) / 'tasks.db')
        self.assertEqual(reopened.list_tasks(), self.tk_store.list_tasks())
        reopened.close()

    def test_blank_title_rejected_and_parameterized_input(self):
        with self.assertRaises(ValueError):
            self.tk_store.add('   ')
        title = "Study 'Git'; DROP TABLE tasks;"
        self.tk_store.add(title)
        self.assertEqual(self.qt_store.list_tasks()[0][1], title)


if __name__ == '__main__':
    unittest.main()
