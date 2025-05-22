#!/bin/bash
aws lambda update-function-code \
    --function-name YOUR_LAMBDA_FUNCTION_NAME \
    --zip-file fileb://app.zip
