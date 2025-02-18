from http.server import BaseHTTPRequestHandler, HTTPServer


hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """Класс для обработки входящих запросов от пользователей"""

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            with open("contacts.html", "r", encoding="utf-8") as file:
                page_content = file.read()

            self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    # Проверка работоспособности сервера
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Начало работы сервера http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Работа сервера остановлена.")
