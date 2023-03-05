# Set the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the necessary files to the working directory
COPY requirements.txt .
COPY load.py .

# Install the required packages
RUN pip install -r requirements.txt

# Set environment variables
USER root
ENV AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=mypro543;AccountKey=EOsReWtTxbt3hIzQLfBr8/UqcEVV0c3Z/Xfehmr4G72G9V42rGnRFEy6VAFu436m7pFjE8gMAjbb+AStNA6zgw==;EndpointSuffix=core.windows.net
ENV AZURE_STORAGE_QUEUE_NAME=incoming

# Run the Python script to load message and run container service
CMD python load.py

