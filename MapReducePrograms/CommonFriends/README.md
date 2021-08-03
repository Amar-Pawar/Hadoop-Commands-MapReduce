### Create a two text file in your local machine and add friend list into it.
nano friend_data.txt
cat > friend_data.txt

### start all hadoop deamons
$ start-all.sh

### check the running status
$ jps

### Create a directory in HDFS, where to kept text file.
$hadoop fs -mkdir /Sample

### Add data.txt on HDFS
$ Hadoop fs -put ~/Documents/hadoop_practice/friend_data.txt /Sample

### Write a map reduce code in python.
Note:-There should be seperate files mapper.py, reducer.py

To run this program we have to download hadoop streaming jar
For specified version of hadoop

Run the code through terminal with following command

Note:- Here we have to explicitly call python before
Mapper and reducer as framework itself does not
Know how to run mapper and reducer.

$ hadoop jar /home/ubuntu/Documents/hadoop_practice/
hadoop-streaming-3.3.1.jar
-file ~/Documents/HadoopWorkspace/Hadoop/MapReducePrograms/CommonFriends/mapper.py
-mapper mapper.py
-file ~/Documents/HadoopWorkspace/Hadoop/MapReducePrograms/CommonFriends/reducer.py
-reducer reducer.py
-input /Sample/friend_data.txt 
-output /common_friends