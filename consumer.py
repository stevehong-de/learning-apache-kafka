from kafka import KafkaConsumer

def kafka_python_consumer():
    consumer = KafkaConsumer("mytesttopic", group_id="mypythonconsumer", bootstrap_servers="localhost:9094",)
    
    for msg in consumer:
        print(msg)

print("Start Consuming")

kafka_python_consumer()

print("Done!")