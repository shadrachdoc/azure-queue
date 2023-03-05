import logging#
import sys
sys.path.append('/usr/local/lib/python3.9/site-packages')


import azure.functions as func

from azure.storage.queue import QueueServiceClient

# Set the connection string and queue name
connection_string = 'DefaultEndpointsProtocol=https;AccountName=mypro543;AccountKey=ShPeD3l6TpeJjjgymn2p8l/ITolLrF6wFGNnD4AGwPv66aNlHnkN5SExUbYguAy0xKyz0R6P2HOP+AStX6nDMg==;EndpointSuffix=core.windows.net'
queue_name = 'incoming'

# Create a QueueServiceClient object
queue_service_client = QueueServiceClient.from_connection_string(connection_string)

# Get a reference to the queue
queue_client = queue_service_client.get_queue_client(queue_name)

# Send a message to the queue
queue_client.send_message('Hello, Azure Queue675!')

print('Message sent to Azure Queue.')

