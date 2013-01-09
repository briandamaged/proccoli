from   StringIO   import StringIO
from   subprocess import Popen, PIPE
import mock

class MockPopen:
  def __init__(self, stdout = '', stderr = '', result = 0):
    self.stdout = stdout
    self.stderr = stderr
    self.result = 0

  def __prepare(self, config, data):
    if config == PIPE:
      return (data, StringIO(data))
    else:
      return (None, None)

  def __call__(self, args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, *leftover_args, **kwargs):
    retval = mock.MagicMock()

    (sout, retval.stdout) = self.__prepare(stdout, self.stdout)
    (serr, retval.stderr) = self.__prepare(stderr, self.stderr)
    
    retval.communicate.return_value = (sout, serr)
    
    retval.wait.return_value = self.result
    return retval

