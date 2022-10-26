from ensurepip import bootstrap
import imp
import json

from kafka import KafkaConsumer
from kafka import KafkaProducer

ORDER_KAFKA_TOPIC="order_details"
ORDER_CONFIRMED_KAFKA_TOPIC="order_confirmed"


consumer=KafkaConsumer(
    ORDER_KAFKA_TOPIC,
    bootstrap_servers="localhost:9092"
)
producer=KafkaProducer(
    bootstrap_servers="localhost:9092"
)

print("Gonna start listening")

while True:

    for message in consumer:
        print("Ongoing transactions")
        cosumed_message=json.loads(message.value.decode())
        print(cosumed_message)

        user_id=cosumed_message["user_id"]
        total_cost=cosumed_message["total_cost"]

        data={
            "customer_id":user_id,
            "customer_email":f"{user_id}@gmail.com",
            "total_cost":total_cost
        }


        print("Successful Transactions...")

        producer.send(
            ORDER_CONFIRMED_KAFKA_TOPIC,
            json.dumps(data).encode("utf-8")
        )