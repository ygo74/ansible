# https://github.com/pika/pika/blob/main/examples/asynchronous_consumer_example.py
# https://github.com/ttestscripting/event-driven-ansible/blob/add-rabbitmq-event_source/plugins/event_source/rabbitmq.py
"""rabbitmq.py.

An ansible-rulebook event source plugin for receiving events via a rabbitmq topic.

Arguments:
---------
    host:      The host where the rabbitmq topic is hosted
    port:      The port where the rabbitmq server is listening
    cafile:    The optional certificate authority file path containing certificates
               used to sign rabbitmq broker certificates
    certfile:  The optional client certificate file path containing the client
               certificate, as well as CA certificates needed to establish
               the certificate's authenticity
    keyfile:   The optional client key file path containing the client private key
    password:  The optional password to be used when loading the certificate chain
    check_hostname:  Enable SSL hostname verification. [True (default), False]
    verify_mode: Whether to try to verify other peers' certificates and how to
               behave if verification fails. [CERT_NONE, CERT_OPTIONAL,
               CERT_REQUIRED (default)]
    encoding:  Message encoding scheme. Default to utf-8
    topic:     The rabbitmq topic
    group_id:  A rabbitmq group id
    offset:    Where to automatically reset the offset. [latest, earliest]
               Default to latest
    security_protocol: Protocol used to communicate with brokers. [PLAINTEXT, SSL,
               SASL_PLAINTEXT, SASL_SSL]. Default to PLAINTEXT
    sasl_mechanism: Authentication mechanism when security_protocol is configured.
               [PLAIN, GSSAPI, SCRAM-SHA-256, SCRAM-SHA-512, OAUTHBEARER].
               Default to PLAIN.
    sasl_plain_username: Username for SASL PLAIN authentication
    sasl_plain_password: Password for SASL PLAIN authentication



"""

import asyncio
from typing import Any, Dict

import pika
import json
import logging

from ssl import CERT_NONE, CERT_OPTIONAL, CERT_REQUIRED

def callback(ch, method, properties, body):

    print(f" [x] Received {body}")
    raise ValueError('A very specific bad thing happened.')


async def main(queue: asyncio.Queue, args: Dict[str, Any]):
    """Receive events via a rabbitmq topic."""

    def callback(ch, method, properties, body):

        print(f" [x] Received {body}")
        raise ValueError('A very specific bad thing happened.')

        try:

            queue.put(dict(template=dict(body=body)))
            asyncio.sleep(delay)

        finally:
            logger.info("Stopping process message")

    logger = logging.getLogger()

    topic = args.get("topic")
    host = args.get("host")
    port = args.get("port")
    cafile = args.get("cafile")
    certfile = args.get("certfile")
    keyfile = args.get("keyfile")
    password = args.get("password")
    check_hostname = args.get("check_hostname", True)
    verify_mode = args.get("verify_mode", "CERT_REQUIRED")
    group_id = args.get("group_id", None)
    offset = args.get("offset", "latest")
    encoding = args.get("encoding", "utf-8")
    security_protocol = args.get("security_protocol", "PLAINTEXT")

    if offset not in ("latest", "earliest"):
        msg = f"Invalid offset option: {offset}"
        raise ValueError(msg)

    verify_modes = {
        "CERT_NONE": CERT_NONE,
        "CERT_OPTIONAL": CERT_OPTIONAL,
        "CERT_REQUIRED": CERT_REQUIRED,
    }
    try:
        verify_mode = verify_modes[verify_mode]
    except KeyError as exc:
        msg = f"Invalid verify_mode option: {verify_mode}"
        raise ValueError(msg) from exc

    ssl_context = None
    if cafile or security_protocol.endswith("SSL"):
        security_protocol = security_protocol.replace("PLAINTEXT", "SSL")
        # ssl_context = create_ssl_context(
        #     cafile=cafile,
        #     certfile=certfile,
        #     keyfile=keyfile,
        #     password=password,
        # )
        # ssl_context.check_hostname = check_hostname
        # ssl_context.verify_mode = verify_mode

    delay = args.get("delay", 0)

    # Create RabbitMQ Connection
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.basic_consume(queue='eda',
                        auto_ack=True,
                        on_message_callback=callback)



if __name__ == "__main__":

    class MockQueue:
        async def put(self, event):
            print(event)

    mock_arguments = dict()
    asyncio.run(main(MockQueue(), mock_arguments))