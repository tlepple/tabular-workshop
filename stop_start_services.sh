#!/bin/bash

##########################################################################################
#  Stop of Spark items
##########################################################################################

echo "stopping spark worker..."
/opt/spark/sbin/stop-worker.sh spark://$(hostname -f):7077
echo
sleep 5

echo "stopping spark master..."
/opt/spark/sbin/stop-master.sh
echo
sleep 5



##########################################################################################
#  Start of Spark items
##########################################################################################

echo "starting spark master..."
/opt/spark/sbin/start-master.sh
echo
sleep 5
echo "starting spark worker..."
/opt/spark/sbin/start-worker.sh spark://$(hostname -f):7077
echo
sleep 5

