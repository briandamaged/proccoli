from   StringIO   import StringIO
from   subprocess import Popen, PIPE
import mock



class MockPopen(object):
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

    retval.stdout = StringIO(self.stdout) if stdout == PIPE else None
    retval.stderr = StringIO(self.stderr) if stderr == PIPE else None

    def communicate(stdin = None):
      o = retval.stdout.read() if retval.stdout else None
      e = retval.stderr.read() if retval.stderr else None
      return (o, e)
    
    retval.communicate.side_effect = communicate
    
    retval.wait.return_value = self.result
    return retval

