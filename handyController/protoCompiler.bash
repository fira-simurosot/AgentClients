#!/bin/bash

rm common_pb2.py
rm -rf REF2CLI
python3 -m grpc_tools.protoc -I=../FIRAMessage --python_out=. ../FIRAMessage/common.proto
python3 -m grpc_tools.protoc -I=../FIRAMessage --python_out=. ../FIRAMessage/REF2CLI/messages.proto
python3 -m grpc_tools.protoc -I=../FIRAMessage --python_out=. --grpc_python_out=. ../FIRAMessage/REF2CLI/service.proto
