import pika, sys, os, json, time
from util import getConfig
from download import download

def main():
    config = getConfig()

    def callback(ch, method, properties, body):
        message = json.loads(body)
        if message["action"] == 'download':
            print(f"recieved message to download: {message['url']}")
            download(message['url'])
            print("done")
        
        else:
            print("Unknown action sent")
        
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # establish connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(config["location"]))
    channel = connection.channel()

    # make sure queue exists
    channel.queue_declare(queue=config["queue"], durable=True)

    # Only process 1 message at a time (wait until done to pick up another)
    channel.basic_qos(prefetch_count=1)

    # subscribe callback to queue
    channel.basic_consume(queue=config["queue"], on_message_callback=callback)

    print("Listener started. Ctrl-C to stop.")

    # enter listener loop
    channel.start_consuming()



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard interupt")

        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)