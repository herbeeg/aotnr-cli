import pytest

from click.testing import CliRunner

from aotnr.app.main import default

class TestMainCLI:
    def testMainOutput(self):
        runner = CliRunner()
        result = runner.invoke(default)

        assert 0 == result.exit_code
        assert 'Welcome to the aotnr-cli interface. Please state your purpose or use --help to guide you.' in result.output
