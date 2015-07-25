from __future__ import absolute_import

from traits.testing.unittest_tools import unittest, UnittestTools

from ..constant import CANCEL, NO, OK, YES
from ..gui import GUI
from ..toolkit import toolkit_object
from ..application_window import ApplicationWindow

ModalDialogTester = toolkit_object('util.modal_dialog_tester:ModalDialogTester')
no_modal_dialog_tester = (ModalDialogTester.__name__ == 'Unimplemented')


class TestWindow(unittest.TestCase, UnittestTools):

    def setUp(self):
        self.gui = GUI()
        self.window = ApplicationWindow()


    def test_destroy(self):
        # test that destroy works even when no control
        self.window.destroy()

    def test_open_close(self):
        # test that openaing and closing works as expected
        with self.assertTraitChanges(self.window, 'opening', count=1):
            with self.assertTraitChanges(self.window, 'opened', count=1):
                self.window.open()
        self.gui.process_events()
        with self.assertTraitChanges(self.window, 'closing', count=1):
            with self.assertTraitChanges(self.window, 'closed', count=1):
                self.window.close()
        self.gui.process_events()

    def test_show(self):
        # test that openaing and closing works as expected
        self.window._create()
        self.window.show(True)
        self.gui.process_events()
        self.window.show(False)
        self.gui.process_events()
        self.window.destroy()

    def test_activate(self):
        # test that activation works as expected
        self.window.open()
        self.gui.process_events()
        self.window.activate()
        self.gui.process_events()
        self.window.close()

    def test_position(self):
        # test that default position works as expected
        self.window.position = (100, 100)
        self.window.open()
        self.gui.process_events()
        self.window.close()

    def test_reposition(self):
        # test that changing position works as expected
        self.window.open()
        self.gui.process_events()
        self.window.position = (100, 100)
        self.gui.process_events()
        self.window.close()

    def test_size(self):
        # test that default size works as expected
        self.window.size = (100, 100)
        self.window.open()
        self.gui.process_events()
        self.window.close()

    def test_resize(self):
        # test that changing size works as expected
        self.window.open()
        self.gui.process_events()
        self.window.size = (100, 100)
        self.gui.process_events()
        self.window.close()

    def test_title(self):
        # test that default title works as expected
        self.window.title = "Test Title"
        self.window.open()
        self.gui.process_events()
        self.window.close()

    def test_retitle(self):
        # test that changing title works as expected
        self.window.open()
        self.gui.process_events()
        self.window.title = "Test Title"
        self.gui.process_events()
        self.window.close()
