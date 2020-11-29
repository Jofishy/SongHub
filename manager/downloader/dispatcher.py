import pika, json
from downloader.util import getConfig

def download(url):
    config = getConfig()

    # establish connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(config["location"]))
    channel = connection.channel()

    # create queue
    channel.queue_declare(queue=config["queue"], durable=True)
    
    # send message through exchange
    channel.basic_publish(exchange='',
        routing_key=config["queue"],
        body=json.dumps({"url":url, "action":"download"}),
        properties=pika.BasicProperties(delivery_mode=2)) # make message persistent

    print("Message sent!")

    # close connection
    connection.close()

    return True

if __name__ == "__main__":
    download("https://www.youtube.com/watch?v=-oLsIJFzPro")