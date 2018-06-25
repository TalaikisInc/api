#!/bin/bash

sudo apt-get install openjdk-9-jre-headless
wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -O swagger-codegen-cli.jar
java -jar swagger-codegen-cli.jar generate -i http://localhost:3000/ -l ruby -o /home/ubuntu/blueblood/ruby/
java -jar swagger-codegen-cli.jar generate -i http://localhost:3000/ -l go -o /home/ubuntu/blueblood/go/
java -jar swagger-codegen-cli.jar generate -i http://localhost:3000/ -l python -o /home/ubuntu/blueblood/python/
java -jar swagger-codegen-cli.jar generate -i http://localhost:3000/ -l typescript -o /home/ubuntu/blueblood/typescript/
