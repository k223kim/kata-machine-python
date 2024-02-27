#!/bin/bash

if [ $# -eq 1 ]
  then msg="-k $1"
fi
pytest $msg
