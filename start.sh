#!/bin/bash
app="lclz.test"
docker build -t ${app} .
docker run -p 8000:80 ${app}