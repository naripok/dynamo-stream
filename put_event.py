import boto3
import logging
import uuid

logger = logging.getLogger(__name__)
db = boto3.resource('dynamodb')


def handler(event, context):
    try:
        table = db.Table('StreamTable')
        table.put_item(
            Item={
                "id": uuid.uuid4().__str__(),
                "body": "message"
            }
        )

        return {'statusCode': 200}

    except Exception as e:
        logger.error(e)
        return {'statusCode': 500, 'message': e.__str__()}
