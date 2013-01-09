from proccoli import stream_for

from StringIO import StringIO
from unittest import TestCase


class Test_stream_for(TestCase):
  def test_it_wraps_strings_in_a_StringIO(self):
    retval = stream_for("hello")
    self.assertTrue(isinstance(retval, StringIO))
    self.assertEqual(retval.read(), "hello")

  def test_it_returns_the_input_when_the_input_is_not_a_string(self):
    input = object()
    retval = stream_for(input)
    self.assertEqual(id(input), id(retval))


