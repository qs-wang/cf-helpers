import aws_factory
import itertools
import functools

import logger_factory

logger = logger_factory.create_logger('cf-helper.cloudformation')

VALID_STACK_STATUSES = ['CREATE_IN_PROGRESS', 'CREATE_FAILED', 'CREATE_COMPLETE', 'ROLLBACK_IN_PROGRESS',
                            'ROLLBACK_FAILED', 'ROLLBACK_COMPLETE', 'DELETE_IN_PROGRESS', 'DELETE_FAILED',
                            'DELETE_COMPLETE', 'UPDATE_IN_PROGRESS', 'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS',
                            'UPDATE_COMPLETE', 'UPDATE_ROLLBACK_IN_PROGRESS', 'UPDATE_ROLLBACK_FAILED',
'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS', 'UPDATE_ROLLBACK_COMPLETE']


def stack_exists(name, region='us-east-1'):
    """
    Check if a CFN stack exists
    :param name: stack name
    :return: True/False
    :rtype: bool
    """
    client = aws_factory.create_aws_client('cloudformation', region)
    # conserve bandwidth (and API calls) by not listing any stacks in DELETE_COMPLETE state
    active_stacks = client.list_stacks( StackStatusFilter=[state for state in VALID_STACK_STATUSES
                                                            if state != 'DELETE_COMPLETE'])

    logger.debug(active_stacks)


    return name in [stack['StackName'] for stack in active_stacks['StackSummaries'] if stack['StackStatus']]
    # return False