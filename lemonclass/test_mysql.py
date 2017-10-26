#!/bin/env Python
# -*- coding:utf-8 -*-
import mysql.connector
import  configparser
#进行实例化
cf=configparser.ConfigParser()
#读取配置文件
cf.read("class_1021_config.conf",encoding="utf-8")   #自带Read函数读取
cnn=mysql.connector.connect(**eval(cf.get("Mysql","config")))
cursor=cnn.cursor()

sql_create_table='CREATE TABLE student1\
( id int(10) NOT NULL AUTO_INCREMENT,\
name varchar(10) DEFAULT NULL,\
age int(3) DEFAULT NULL,\
PRIMARY KEY (id))\
ENGINE=MyISAM DEFAULT CHARSET=utf8'

cursor.execute(sql_create_table)

cursor.close()
cnn.close()