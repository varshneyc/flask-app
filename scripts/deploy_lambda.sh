#!/bin/bash
aws lambda update-function-code \
    --function-name chirag-flask-lambda \
    --zip-file fileb://app.zip
