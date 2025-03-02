from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()

    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    mailFrom = 'MAIL FROM:<alice@example.com>\r\n'
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()

    rcptTo = 'RCPT TO:<bob@example.com>\r\n'
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()

    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()

    clientSocket.send(msg.encode())

    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()

    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()

    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
