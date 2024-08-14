from kafka import KafkaProducer

# Create message
msg = "Kafka message"

# Create producer
producer = KafkaProducer(bootstrap_servers="localhost:9094")

# Function to send message into Kafka
def kafka_python_producer_async(producer, msg):
    producer.send("mytesttopic", msg).add_callback(success).add_errback(error)
    producer.flush()

def success(metadata):
    print(metadata.topic)

def error(exception):
    print(exception)

print("Start Producing")

# Produce the message
kafka_python_producer_async(producer, b"Kafka message") # Serialize into bytes

print("Done!")