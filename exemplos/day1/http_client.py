import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9000))
cmd = "GET http://localhost/index.html HTTP/1.0\r\n\r\n".encode()
client.send(cmd)

while True:
    data = client.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")

client.close()


############################


# import httpx

# result = httpx.get("http://example.com/index.html")
# print(result.status_code)
# print(result.headers)
# print(result.content)
