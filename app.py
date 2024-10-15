#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk.cdk_stack import CdkStack, MahdiHelloWorldStack
from pipeline_stack import WorkshopPipelineStack



app = cdk.App()
MahdiHelloWorldStack(app, "mahdi-helloworld",)
app.synth()
