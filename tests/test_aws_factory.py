import aws_factory
import unittest
import logging
import logger_factory

logger = logger_factory.create_logger('cf-helper.aw_factory.test')
 
class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """
 
    def test_create_aws_client(self):
        """
        Test that the addition of two integers returns the correct total
        """
        try:
            result = aws_factory.create_aws_client('cloudformation')
            self.assertIsNotNone(result)
        except Exception as ex:
            logger.error(ex)
            self.fail()

    def test_create_aws_client_failed(self):
        """
        Test that the addition of two integers returns the correct total
        """
        try:
            result = aws_factory.create_aws_client('1')
            self.fail()
        except Exception as ex:
            logger.error(ex)
            
if __name__ == '__main__':
    unittest.main()