import pytest

from click.testing import CliRunner

from aotnr.app.main import login

class TestCLIAuth:
	def testLogin(self):
		runner = CliRunner()
		result = runner.invoke(login, input='test@abc.com\nq1w2e3\n')
		
		assert not result.exception
		assert 'Please enter your username: test@abc.com\nPlease enter your password: q1w2e3\nSuccessfully logged in.\n' == result.output
		
