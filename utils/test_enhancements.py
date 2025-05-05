import unittest
from utils.enhancements import platform_command, run_command, send_telegram_message

class TestEnhancements(unittest.TestCase):
    def test_platform_command(self):
        self.assertIn(platform_command(), ["Linux", "Windows", "Darwin"])

    def test_run_command_success(self):
        output = run_command("echo Hello")
        self.assertIn("Hello", output)

    def test_run_command_failure(self):
        output = run_command("nonexistent_command_12345")
        self.assertTrue("not found" in output or "is not recognized" in output)

    def test_telegram_mock(self):
        result = send_telegram_message(message="This is a test")
        self.assertIn(result, [True, False, "Missing token or chat_id"])

if __name__ == '__main__':
    unittest.main()
