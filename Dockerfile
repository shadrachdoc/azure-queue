# Set the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the necessary files to the working directory
COPY requirements.txt .
COPY send_message.py .

# Install the required packages
RUN pip install -r requirements.txt
RUN apt-get update && apt-get -y install cron
# Set environment variables
ENV AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=mypro543;AccountKey=EOsReWtTxbt3hIzQLfBr8/UqcEVV0c3Z/Xfehmr4G72G9V42rGnRFEy6VAFu436m7pFjE8gMAjbb+AStNA6zgw==;EndpointSuffix=core.windows.net
ENV AZURE_STORAGE_QUEUE_NAME=incoming

# Run the Python script every minute using cron
USER root
RUN echo "* * * * * /usr/bin/python3 /app/send_message.py >> /var/log/cron.log 2>&1" >> /etc/cron.d/send_message_cron
RUN chmod 0644 /etc/cron.d/send_message_cron
RUN crontab /etc/cron.d/send_message_cron
RUN touch /var/log/cron.log

# Install Azure Functions Core Tools
USER root
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/microsoft-prod.list
RUN apt-get update && apt-get install azure-functions-core-tools -y

# Start cron
USER root
CMD cron && tail -f /var/log/cron.log

