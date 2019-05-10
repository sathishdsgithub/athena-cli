
import unittest

from cmd2.parsing import StatementParser

from athena_cli import Athena, AthenaShell


class TestCLI(unittest.TestCase):

    def setUp(self):
        pass

    def test_use_schema(self):

        athena = Athena(profile=None, region='eu-west-1', bucket='s3://', debug=False)

        shell = AthenaShell(athena, db='sampledb')
        self.assertEqual(shell.dbname, 'sampledb')
        shell.do_use('clean')
        self.assertEqual(shell.dbname, 'clean')

    def test_parser(self):

        parser = StatementParser()

        line = """
        SELECT *
        FROM elb_logs
        """
        statement = parser.parse(line)
        self.assertEqual(statement.command, 'SELECT')
        self.assertEqual(statement.command_and_args, 'SELECT * FROM elb_logs')

        line = """
        select *
        from elb_logs
        """
        statement = parser.parse(line)
        self.assertEqual(statement.command, 'select')
        self.assertEqual(statement.command_and_args, 'select * from elb_logs')
