
import pandas as pd 
from kafka import KafkaConsumer,KafkaProducer
from time import sleep
from json import dumps
import json 


producer= KafkaProducer(bootstrap_servers=['3.110.49.155:9092'],
                        value_serializer=lambda x:
                         dumps(x).encode('utf-8'))


producer.send('demo_test',value="whatsapp")
producer.send('demo_test',value="whatsapp1")


df=pd.read_csv('indexProcessed.csv')

df.describe()