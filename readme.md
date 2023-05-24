# Python ATAK Server - TLS Connection

This Python script allows you to listen for Cursor-on-Target (COT) messages from a ATAK COT server using a TLS connection. It establishes a secure connection to the server, receives incoming messages, and prints them to the console. It can also be used to send messages to the server.

### Update:
24.05.23 - Added a feature which sends a COT every 1 minute to the server, creating a BOT user. This can be useful for interfacing with other future functions.

## Prerequisites

Before using this script, ensure that you have the following:

- Python 3.x installed on your system.
- The necessary dependencies installed. You can install them using pip:

pip install colorama


## Usage

1. Clone the repository or download the script file to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Modify the script to configure the server and client settings:

   - Set the server IP and port in the `server_ip` and `server_port` variables at the top of the script.
   - Provide the path to your client certificate (`certfile`) and key (`keyfile`) in the `receive_messages` function.
   - Set the password for your client certificate in the `cert_password` variable.
   - If required, update the `cafile` variable with the path to the server's self-signed certificate.

4. Run the script:

python connect.py


   The script will establish a TLS connection to the COT server and start listening for incoming messages.

5. You will see the script output on the console. Incoming messages will be printed in different colors to differentiate them.

6. To stop the script, press `Ctrl + C`.

## Troubleshooting

- **SSL Certificate Errors**: If you encounter SSL certificate errors, ensure that you have the correct client certificate and key, and that the server's certificate is valid and trusted. You may need to update the `certfile`, `keyfile`, and `cafile` variables in the script accordingly.

## License

This script is licensed under the [MIT License](LICENSE).

## Acknowledgements

This script utilizes the following Python packages:

- [colorama](https://pypi.org/project/colorama/): for colored console output.
- [ssl](https://docs.python.org/3/library/ssl.html): for establishing TLS connections.


