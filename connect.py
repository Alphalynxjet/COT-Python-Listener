import ssl
import socket
from colorama import init, Fore, Style
import time
from datetime import datetime, timedelta

# Initialize colorama
init()

# Server information
server_ip = '127.0.0.1'  # Update with the server's hostname if applicable
server_port = 8089

# Client certificate and key
certfile = '/root/example.pem'
keyfile = '/root/example.key'
cert_password = 'atakatak'
cafile = '/root/server.pem'

cot_xml_template = '''<?xml version="1.0" encoding="UTF-8"?>
<event version="2.0" uid="BOT" type="a-f-G-U-C-I" how="h-e" time="{time}" start="{time}" stale="{stale}">
    <point lat="0" lon="0" hae="9999999.0" ce="9999999.0" le="9999999.0"/>
    <detail>
        <contact callsign="BOT" endpoint="*:-1:stcp"/>
        <__group name="Yellow" role="RTO"/>
        <status battery="100"/>
        <takv device="Server" platform="Python" os="Ubuntu" version="1"/>
        <track speed="0.0" course="0.0"/>
        <uid Droid="BOT"/>
    </detail>
</event>'''

def set_stale_time():
    current_time = datetime.utcnow()
    stale_time = current_time + timedelta(minutes=5)
    return stale_time.strftime('%Y-%m-%dT%H:%M:%SZ')

def send_cot_message(sock):
    try:
        cot_xml = cot_xml_template.format(time=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
                                          stale=set_stale_time())
        sock.sendall(cot_xml.encode())
        print(Fore.YELLOW + 'Sent CoT message:' + Style.RESET_ALL, cot_xml)

    except socket.error as e:
        print(Fore.RED + 'Socket error:' + Style.RESET_ALL, e)
    except Exception as e:
        print(Fore.RED + 'Error:' + Style.RESET_ALL, e)

def receive_messages():
    try:
        # Create a TLS context
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

        # Load client certificate and key
        context.load_cert_chain(certfile, keyfile, cert_password)

        # Load the server's self-signed certificate into the custom CA store
        context.load_verify_locations(cafile=cafile)

        # Disable hostname verification
        context.check_hostname = False

        # Establish a TLS connection to the server
        with socket.create_connection((server_ip, server_port)) as sock:
            # Wrap the socket with the TLS context
            with context.wrap_socket(sock) as ssock:
                print(Fore.GREEN + 'Connected to the server.' + Style.RESET_ALL)

                # Send the CoT message every 1 minute
                while True:
                    send_cot_message(ssock)
                    time.sleep(60)

                print(Fore.GREEN + 'Connection closed.' + Style.RESET_ALL)

    except ssl.SSLError as e:
        print(Fore.RED + 'SSL error:' + Style.RESET_ALL, e)
    except socket.error as e:
        print(Fore.RED + 'Socket error:' + Style.RESET_ALL, e)
    except Exception as e:
        print(Fore.RED + 'Error:' + Style.RESET_ALL, e)

if __name__ == '__main__':
    receive_messages()
