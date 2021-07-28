# import subprocess library
import subprocess
# ls command to list content
subprocess.run('ls')

output = subprocess.Popen(["hadoop", "fs", "-ls", "/Sample"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
for line in output.stdout:
    print(line)

# to get data from HDFS to local storage
subprocess.Popen(["hadoop", "fs", "-get", "/Sample/PracticeSample/data.txt", "/home/ubuntu/Documents"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# to put data from local to HDFS
subprocess.Popen(["hadoop", "fs", "-put","/home/ubuntu/Documents/data.txt","/Sample/PracticeSample"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# to copy data from local to HDFS
subprocess.Popen(["hadoop", "fs", "copyFromLocal","/home/ubuntu/Documents/data.txt","/Sample/PracticeSample"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# to copy data from HDFS To local
subprocess.Popen(["hadoop", "fs", "-copyToLocal", "/Sample/PracticeSample/data.txt", "/home/ubuntu/Documents"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# to remove directory from HDFS
subprocess.Popen(["hadoop", "fs", "-rm","-r" "/Sample/PracticeSample"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# to display content of file
subprocess.Popen(["hadoop", "fs", "-cat" "/Sample/PracticeSample"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# making directory
subprocess.Popen(["hadoop", "fs", "-mkdir" "/hadoop"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# to movie directory in HDFS
subprocess.Popen(["hadoop", "fs", "-mv" "/hadoop", "/Sample"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
