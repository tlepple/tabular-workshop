#!/bin/bash

spark-sql --packages \
  org.apache.iceberg:iceberg-spark-runtime-3.3_2.12:1.1.0 \
--properties-file /opt/spark/sql/conf.properties 
-f /opt/spark/sql/stream_customer_ddl.sql \
--verbose
