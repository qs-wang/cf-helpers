import cloudformation
import unittest
import logging
import logger_factory

logger = logger_factory.create_logger('cf-helper.cloudformation.test')

class TestCloudFormation(unittest.TestCase):
    """
    Test the add function from the mymath library
    """

    def test_statck_exists(self):
        """
        Test that the addition of two integers returns the correct total
        """
        try:
            result = cloudformation.stack_exists(name='bot-api-prod',region='ap-southeast-2')

            self.assertTrue(result)

        except Exception as ex:
            logger.error(ex)
            self.fail()

    def test_statck_not_exists(self):
        """
        Test that the addition of two integers returns the correct total
        """
        try:
            result = cloudformation.stack_exists(name='not-exists',region='ap-southeast-2')

            self.assertFalse(result)

        except Exception as ex:
            logger.error(ex)
            self.fail()

if __name__ == '__main__':
    unittest.main()
