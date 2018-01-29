import sys
import cloudformation
import logger_factory

logger =  logger_factory.create_logger('cf-helper.stackexists')


def main():
    if len(sys.argv)!=2:
        print('Usage python stackexists.py stackname')
        sys.exit(1)

    stack_name = sys.argv[1]

    if stack_name == None:
        sys.exit(1)

    logger.debug('Checking stack: {}'.format(stack_name))

    #TODO: region is hard coded
    if cloudformation.stack_exists(stack_name,'ap-southeast-2'):
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
