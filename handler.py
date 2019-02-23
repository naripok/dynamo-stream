import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def handler(event, context):
    try:
        logger.info('Stream event captured')
        record = event['Records'][0]

        if record['eventName'] == 'INSERT':
            logger.info('Insert event')
        elif record['eventName'] == 'MODIFY':
            logger.info('Modify event')
        else:
            logger.info('Unexpected event')
            return {'status': 'Unexpected event'}

        return {'statusCode': 200}

    except Exception as e:
        logger.error(e)
        return {'statusCode': 500, 'message': e.__str__()}
