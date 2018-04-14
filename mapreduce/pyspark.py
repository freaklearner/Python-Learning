import sys
sys.path.append("/usr/lib/python2.7/dist-packages/")
from pyspark.sql import SparkSession
import os
from os import path

fl = open(path.join(os.getcwd(),'wordscount.txt'))
sparkSession = SparkSession.builder.appName("example-test-write-hadoop").getOrCreate()
data = fl.readlines()
df = sparkSession.createDataFrame(data)
df.write.text("hdfs://cluster/user/temp/wordscount.txt")
