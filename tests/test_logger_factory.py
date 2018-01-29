import logger_factory
import unittest
import sys
import logging


class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """

    def test_create_logger(self):
        """
        Test that the addition of two integers returns the correct total
        """
        try:
            result = logger_factory.create_logger(
                'stackchat.logger.factory.test')
            self.assertIsNotNone(result)
            self.assertEqual(result.getEffectiveLevel(), logging.INFO)

            result.info('hello logger')

        except Exception:
            self.fail()

    if __name__ == '__main__':
        unittest.main()
