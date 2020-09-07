import mock
from click.testing import CliRunner

from pygameweb.run import run_front


def test_run(config):
    """ test the pygameweb_front command.
    """
    runner = CliRunner()
    with mock.patch('pygameweb.run.run_simple') as run_simple:
        result = runner.invoke(run_front, ['--port',  '8080'])
        assert result.exit_code == 0
        assert run_simple.called
        assert config.HOST == run_simple.call_args[0][0]
        assert 8080 == run_simple.call_args[0][1]
