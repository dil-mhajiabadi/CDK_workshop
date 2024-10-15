from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    # aws_sqs as sqs,
)
from constructs import Construct
from hitcounter import HitCounter
from cdk_dynamo_table_view import TableViewer


class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

class MahdiHelloWorldStack(Stack):
    
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        my_lambda = _lambda.Function(self, 'HelloHandler', runtime = _lambda.Runtime.PYTHON_3_10,
                                      code = _lambda.Code.from_asset('lambda'),
                                     handler='hello.handler',)
        
        hello_with_counter = HitCounter(
            self, 'HelloHitCounter',
            downstream=my_lambda,
        )

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=hello_with_counter.handler,
        )
        TableViewer(self, 'ViewHitCounter',title = 'Hello Hits' ,table=hello_with_counter.table)

