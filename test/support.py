import _tkinter
import functools
import re
import tkinter
import unittest
import os
import sys


# dummy value to run tests without test.support
verbose = 1   # Flag set to 0 by regrtest.py file in test folder.

# TEST_HOME_DIR refers to the top level directory of the "test" package
# that contains Python's regression test suite
TEST_SUPPORT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_HOME_DIR = os.path.dirname(TEST_SUPPORT_DIR)


# Class of cpython/Lib/test/support/__init__.py
class ResourceDenied(unittest.SkipTest):
    """Test skipped because it requested a disallowed resource.
    This is raised when a test calls requires() for a resource that
    has not be enabled.  It is used to distinguish between expected
    and unexpected skips.
    """


def findfile(filename, subdir=None):
    """Try to find a file on sys.path or in the test directory.  If it is not
    found the argument passed to the function is returned (this does not
    necessarily signal failure; could still be the legitimate path).
    Setting *subdir* indicates a relative path to use to find the file
    rather than looking directly in the path directories.
    """
    if os.path.isabs(filename):
        return filename
    if subdir is not None:
        filename = os.path.join(subdir, filename)
    path = [TEST_HOME_DIR] + sys.path
    for dn in path:
        fn = os.path.join(dn, filename)
        if os.path.exists(fn):
            return fn
    return filename


class AbstractTkTest:

    @classmethod
    def setUpClass(cls):
        cls._old_support_default_root = tkinter._support_default_root
        destroy_default_root()
        tkinter.NoDefaultRoot()
        cls.root = tkinter.Tk()
        cls.wantobjects = cls.root.wantobjects()
        # De-maximize main window.
        # Some window managers can maximize new windows.
        cls.root.wm_state('normal')
        try:
            cls.root.wm_attributes('-zoomed', False)
        except tkinter.TclError:
            pass

    @classmethod
    def tearDownClass(cls):
        cls.root.update_idletasks()
        cls.root.destroy()
        del cls.root
        tkinter._default_root = None
        tkinter._support_default_root = cls._old_support_default_root

    def setUp(self):
        self.root.deiconify()

    def tearDown(self):
        for w in self.root.winfo_children():
            w.destroy()
        self.root.withdraw()


def destroy_default_root():
    if getattr(tkinter, '_default_root', None):
        tkinter._default_root.update_idletasks()
        tkinter._default_root.destroy()
        tkinter._default_root = None


def simulate_mouse_click(widget, x, y):
    """Generate proper events to click at the x, y position (tries to act
    like an X server)."""
    widget.event_generate('<Enter>', x=0, y=0)
    widget.event_generate('<Motion>', x=x, y=y)
    widget.event_generate('<ButtonPress-1>', x=x, y=y)
    widget.event_generate('<ButtonRelease-1>', x=x, y=y)


tcl_version = tuple(map(int, _tkinter.TCL_VERSION.split('.')))


def requires_tcl(*version):
    if len(version) <= 2:
        return unittest.skipUnless(
            tcl_version >= version,
            'requires Tcl version >= ' + '.'.join(
                map(str, version)))

    def deco(test):
        @functools.wraps(test)
        def newtest(self):
            if get_tk_patchlevel() < version:
                self.skipTest(
                    'requires Tcl version >= ' + '.'.join(
                        map(str, version)))
            test(self)
        return newtest
    return deco


_tk_patchlevel = None


def get_tk_patchlevel():
    global _tk_patchlevel
    if _tk_patchlevel is None:
        tcl = tkinter.Tcl()
        patchlevel = tcl.call('info', 'patchlevel')
        m = re.fullmatch(r'(\d+)\.(\d+)([ab.])(\d+)', patchlevel)
        major, minor, releaselevel, serial = m.groups()
        major, minor, serial = int(major), int(minor), int(serial)
        releaselevel = {'a': 'alpha', 'b': 'beta', '.': 'final'}[releaselevel]
        if releaselevel == 'final':
            _tk_patchlevel = major, minor, serial, releaselevel, 0
        else:
            _tk_patchlevel = major, minor, 0, releaselevel, serial
    return _tk_patchlevel


def tcl_obj_eq(actual, expected):
    if actual == expected:
        return True
    if isinstance(actual, _tkinter.Tcl_Obj):
        if isinstance(expected, str):
            return str(actual) == expected
    if isinstance(actual, tuple):
        if isinstance(expected, tuple):
            return (len(actual) == len(expected) and
                    all(tcl_obj_eq(act, exp)
                        for act, exp in zip(actual, expected)))
    return False
