import contextlib
import sys
import unittest

from pip.utils import captured_output, StreamWrapper

from mfs.mfs import MFS


@contextlib.contextmanager
def captured_output(stream_name):
    """Return a context manager used by captured_stdout and captured_stdin
    that temporarily replaces the sys stream *stream_name* with a StringIO."""
    orig_stdout = getattr(sys, stream_name)
    setattr(sys, stream_name, StreamWrapper.from_stream(orig_stdout))
    try:
        yield getattr(sys, stream_name)
    finally:
        setattr(sys, stream_name, orig_stdout)


def captured_stdout():
    """Capture the output of sys.stdout:

       with captured_stdout() as s:
           print "hello"
       self.assertEqual(s.getvalue(), "hello")
    """
    return captured_output("stdout")


def captured_stderr():
    return captured_output("stderr")


def captured_stdin():
    return captured_output("stdin")


class TestMFS(unittest.TestCase):
    def setUp(self):
        self.mfs = MFS()

        # def tearDown(self):
        # self.mfs.tree_display('/')

    def test_mkdir(self):
        with captured_stdout() as stdout:
            self.mfs.mkdir('root')
            self.mfs.mkdir('root/xxx')
            self.mfs.mkdir('/etc/xxx')
            self.mfs.ls()
        output = stdout.getvalue().strip()
        self.assertEqual('etc/' in output, True)
        self.assertEqual('root/' in output, True)

    def test_cd(self):
        with captured_stdout() as stdout:
            self.mfs.mkdir('root')
            self.mfs.mkdir('root/xxx')
            self.mfs.cd('root')
            self.mfs.ls()
        output = stdout.getvalue().strip()
        print(output)
        self.assertEqual('xxx/' in output, True)


if __name__ == '__main__':
    unittest.main()
