# Hadoop-Commands-MapReduce

## HADOOP COMMANDS

### To get hadoop HDFS version:_
$ hadoop version

### To create a folder inside HDFS:-
Note:- Here sample is directory name that we want to create
$hadoop fs -mkdir /Sample

### To enlist files in HDFS directory:-
$ Hadoop fs -ls /Sample

### To put file from local to HDFS:-
Note:- Here first path is of file in local directory and second is
Destination folder on HDFS
$ Hadoop fs -put /home/ubuntu/Documents/hadoop_practice/data.txt /Sample

### copyFromLocal:-
$hadoop fs -copyFromLocal ~/Documents/hadoop_practice/data.txt /Sample

### Get file from HDFS to local machine:-
$ hadoop fs -get /Sample/data.txt /home/ubuntu/Documents/hadoop_practice

### copyToLocal:-
$ hadoop fs -copyToLocal /Sample/data.txt ~/Documents/hadoop_practice

### To display the content of file 
$ hadoop fs -cat /sample/data.txt

### To remove directory
$ hadoop fs -rm -r /Sample/PracticeSample


# WORD COUNT PROGRAM

### Create a text file in your local machine and add text into it.
nano data.txt
cat > data.txt

### Create a directory in HDFS, where to kept text file.
$hadoop fs -mkdir /Sample

### Add data.txt on HDFS
$ Hadoop fs -put ~/Documents/hadoop_practice/data.txt /Sample

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
-file ~/Documents/HadoopWorkspace/Hadoop/MapReducePrograms/WordCount/word_count_mapper.py
-mapper word_count_mapper.py
-file ~/Documents/HadoopWorkspace/Hadoop/MapReducePrograms/WordCount/word_count_reducer.py
-reducer word_count_reducer.py
-input /Sample/PracticeSample/data.txt 
-output /output2
	