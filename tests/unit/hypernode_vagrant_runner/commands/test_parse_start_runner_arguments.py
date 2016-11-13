from mock import ANY, call

from hypernode_vagrant_runner.commands import parse_start_runner_arguments
from hypernode_vagrant_runner.settings import HYPERNODE_VAGRANT_PHP_VERSIONS, \
    HYPERNODE_VAGRANT_DEFAULT_USER, HYPERNODE_VAGRANT_DEFAULT_PHP_VERSION, \
    HYPERNODE_VAGRANT_USERS
from tests.testcase import TestCase


class TestParseStartRunnerArguments(TestCase):
    def setUp(self):
        self.argument_parser = self.set_up_patch('hypernode_vagrant_runner.commands.ArgumentParser')
        self.parse_arguments = self.set_up_patch('hypernode_vagrant_runner.commands.parse_arguments')

    def test_parse_start_runner_arguments_instantiates_argument_parser(self):
        parse_start_runner_arguments()

        self.argument_parser.assert_called_once_with(
            prog='hypernode-vagrant-runner',
            description=ANY
        )

    def test_parse_start_runner_arguments_parses_arguments(self):
        parse_start_runner_arguments()

        self.parse_arguments.assert_called_once_with(
            self.argument_parser.return_value
        )

    def test_parse_start_runner_adds_run_once_flag_with_default_true(self):
        parse_start_runner_arguments()

        expected_call = call(
            '--run-once', '-1',
            action='store_true',
            help=ANY
        )
        self.assertIn(
            expected_call,
            self.argument_parser.return_value.add_argument.mock_calls
        )

    def test_parse_start_runner_adds_project_path_flag(self):
        parse_start_runner_arguments()

        expected_call = call(
            '--project-path',
            help=ANY
        )
        self.assertIn(
            expected_call,
            self.argument_parser.return_value.add_argument.mock_calls
        )

    def test_parse_start_runner_adds_command_to_run_flag(self):
        parse_start_runner_arguments()

        expected_call = call(
            '--command-to-run', '-c',
            help=ANY
        )
        self.assertIn(
            expected_call,
            self.argument_parser.return_value.add_argument.mock_calls
        )

    def test_parse_start_runner_adds_path_flag_for_a_pre_existing_checkout_directory(self):
        parse_start_runner_arguments()

        expected_call = call(
            '--pre-existing-vagrant-path', '-p',
            help=ANY
        )
        self.assertIn(
            expected_call,
            self.argument_parser.return_value.add_argument.mock_calls
        )

    def test_parse_start_runner_adds_php_flag(self):
        parse_start_runner_arguments()

        expected_call = call(
            '--php',
            help=ANY,
            choices=HYPERNODE_VAGRANT_PHP_VERSIONS,
            default=HYPERNODE_VAGRANT_DEFAULT_PHP_VERSION
        )
        self.assertIn(
            expected_call,
            self.argument_parser.return_value.add_argument.mock_calls
        )

    def test_parse_start_runner_adds_user_flag(self):
        parse_start_runner_arguments()

        expected_call = call(
            '--user',
            help=ANY,
            choices=HYPERNODE_VAGRANT_USERS,
            default=HYPERNODE_VAGRANT_DEFAULT_USER
        )
        self.assertIn(
            expected_call,
            self.argument_parser.return_value.add_argument.mock_calls
        )

    def test_parse_start_runner_arguments_returns_parsed_arguments(self):
        ret = parse_start_runner_arguments()

        self.assertEqual(ret, self.parse_arguments.return_value)
