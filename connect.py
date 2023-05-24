import ssl
import socket
from colorama import init, Fore, Style

# Initialize colorama
init()

# Server information
server_ip = '127.0.0.1'  # Update with the server's hostname if applicable
server_port = 8089

# Client certificate and key
certfile = '/root/example.pem'
keyfile = '/root/example.key'
cert_password = 'atakatak'
cafile = '/root/server.crt'

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

                # Receive and print incoming messages
                while True:
                    data = ssock.recv(1024)
                    if not data:
                        break
                    print(Fore.CYAN + 'Received:' + Style.RESET_ALL, data.decode())

                print(Fore.GREEN + 'Connection closed.' + Style.RESET_ALL)

    except ssl.SSLError as e:
        print(Fore.RED + 'SSL error:' + Style.RESET_ALL, e)
    except socket.error as e:
        print(Fore.RED + 'Socket error:' + Style.RESET_ALL, e)
    except Exception as e:
        print(Fore.RED + 'Error:' + Style.RESET_ALL, e)

if __name__ == '__main__':
    receive_messages()
