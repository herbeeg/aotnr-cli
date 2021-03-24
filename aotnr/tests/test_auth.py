import pytest

from click.testing import CliRunner

from aotnr.app.main import login

class TestCLIAuth:
	def testLogin(self):
		runner = CliRunner()
		result = runner.invoke(login, input='test@abc.com\n')
		
		assert not result.exception
		assert 'Please enter your username: test@abc.com\n' in result.output
		
