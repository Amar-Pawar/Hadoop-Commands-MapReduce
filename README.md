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