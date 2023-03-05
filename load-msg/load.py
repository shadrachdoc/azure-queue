from azure.storage.queue import QueueServiceClient
import datetime

# Define connection string and queue name
connection_string = "DefaultEndpointsProtocol=https;AccountName=mypro543;AccountKey=ShPeD3l6TpeJjjgymn2p8l/ITolLrF6wFGNnD4AGwPv66aNlHnkN5SExUbYguAy0xKyz0R6P2HOP+AStX6nDMg==;EndpointSuffix=core.windows.net"
queue_name = "incoming"

# Create a queue service client
queue_service_client = QueueServiceClient.from_connection_string(connection_string)

# Get a queue client
queue_client = queue_service_client.get_queue_client(queue_name)

# Peek at the next message in the queue
messages = queue_client.receive_messages()
if messages:
    message = list(messages)[0]
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Last Message received at {}: {}".format(current_time, message.content))
else:
    print("No messages in the queue.")