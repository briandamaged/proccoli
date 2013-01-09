from proccoli import stream_for, Popen_Mock

from subprocess import PIPE
from StringIO   import StringIO
from unittest   import TestCase


class Test_stream_for(TestCase):
  def test_it_wraps_strings_in_a_StringIO(self):
    retval = stream_for("hello")
    self.assertTrue(isinstance(retval, StringIO))
    self.assertEqual(retval.read(), "hello")

  def test_it_returns_the_input_when_the_input_is_not_a_string(self):
    input = object()
    retval = stream_for(input)
    self.assertEqual(id(input), id(retval))




class Test_Popen_Mock(TestCase):
  def setUp(self):
    self.popen = Popen_Mock(stdout = "this is stdout", stderr = "this is stderr")
  
  def test_communicate_returns_Nones_when_piping_disabled(self):
    p = self.popen(["echo", "fake"])
    self.assertEqual(p.communicate(), (None, None))


  def test_communicate_can_pretend_to_return_stdout(self):
    p = self.popen(["echo", "fake"], stdout = PIPE)
    
    self.assertEqual(p.communicate(), ("this is stdout", None))
    self.assertEqual(p.communicate(), ("", None))
    

  def test_communicate_can_pretend_to_return_stderr(self):
    p = self.popen(["echo", "fake"], stderr = PIPE)
    
    self.assertEqual(p.communicate(), (None, "this is stderr"))
    self.assertEqual(p.communicate(), (None, ""))


  def test_stdout_is_None_when_piping_disabled(self):
    p = self.popen(["echo", "something"], stderr = PIPE)
    self.assertEqual(p.stdout, None)

  def test_stdout_is_a_stream_when_piping_enabled(self):
    p = self.popen(["echo", "lkjsdf"], stdout = PIPE, stderr = PIPE)
    self.assertEqual(p.stdout.read(), "this is stdout")


  def test_stderr_is_None_when_piping_disabled(self):
    p = self.popen(["echo", "blah"], stdout = PIPE)
    self.assertEqual(p.stderr, None)
    
  def test_stderr_is_a_stream_when_piping_enabled(self):
    p = self.popen(["blarg", "blarg"], stdout = PIPE, stderr = PIPE)
    p.assertEqual(p.stderr.read(), "this is stderr")
    
  
  def test_communicate_empties_streams(self):
    p = self.popen(["lksdf"], stdout = PIPE, stderr = PIPE)
    self.assertEqual(p.communicate(), ("this is stdout", "this is stderr"))
    self.assertEqual(p.stdout.read(), '')
    self.assertEqual(p.stderr.read(), '')

