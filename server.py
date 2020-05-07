import pika
from core.vachellia import Vachellia, get_json
from termcolor import colored

print(
    colored(
        """
██    ██  █████   ██████ ██   ██ ███████ ██      ██      ██  █████  
██    ██ ██   ██ ██      ██   ██ ██      ██      ██      ██ ██   ██ 
██    ██ ███████ ██      ███████ █████   ██      ██      ██ ███████ 
 ██  ██  ██   ██ ██      ██   ██ ██      ██      ██      ██ ██   ██ 
  ████   ██   ██  ██████ ██   ██ ███████ ███████ ███████ ██ ██   ██ 
                                                                    
    """
    )
)
print(f"[ {colored('C TYPE', 'green')}  ] -> [ GENERIC ]")
print(f"[ {colored('VERSION', 'green')} ] -> [ 0.01 ]")

vachellia = Vachellia(get_json(r"vachellia.json"))
connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.0.9"))
channel = connection.channel()
channel.queue_declare(queue="cell_1")
channel.queue_declare(queue="master")


def callback(ch, method, properties, in_data):
    # print(f"[{colored('OK', 'green')}][callback][in_data] -> [ {in_data} ]")
    out_data = vachellia.operate_request(in_data)
    channel.basic_publish(exchange="", routing_key="master", body=out_data)


channel.basic_consume(queue="cell_1", on_message_callback=callback, auto_ack=True)
print(f"[ {colored('STARTED', 'green')} ] -> [ To exit press CTRL+C ]")
channel.start_consuming()
