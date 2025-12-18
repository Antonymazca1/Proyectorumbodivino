from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import json
import os
from config import HOST, PORT, ADMIN_PASSWORD, DATA_FILE

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = os.path.join(BASE_DIR, "templates")
STATIC = os.path.join(BASE_DIR, "static")

def load_messages():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_message(data):
    messages = load_messages()
    messages.append(data)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        # Archivos estáticos
        if path.startswith("/static/"):
            file_path = os.path.join(BASE_DIR, path.lstrip("/"))
            if os.path.isfile(file_path):
                self.send_response(200)
                self.send_header("Content-Type", self.get_type(file_path))
                self.end_headers()
                self.wfile.write(open(file_path, "rb").read())
            else:
                self.send_error(404)
            return

        # Rutas
        if path == "/" or path == "/index":
            return self.render("index.html")
        if path == "/about":
            return self.render("about.html")
        if path == "/messages":
            return self.render("messages.html")
        if path == "/resources":
            return self.render("resources.html")
        if path == "/contact":
            return self.render("contact.html")
        if path == "/login":
            return self.render("login.html")
        if path == "/admin":
            if not self.is_logged():
                return self.redirect("/login")
            return self.render_admin()

        self.send_error(404)

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8")
        data = parse_qs(body)

        if self.path == "/contact":
            msg = {
                "name": data.get("name", [""])[0],
                "email": data.get("email", [""])[0],
                "subject": data.get("subject", [""])[0],
                "content": data.get("content", [""])[0],
            }
            save_message(msg)
            return self.render("thanks.html")

        if self.path == "/login":
            password = data.get("password", [""])[0]
            if password == ADMIN_PASSWORD:
                self.send_response(302)
                self.send_header("Location", "/admin")
                self.send_header("Set-Cookie", "session=ok")
                self.end_headers()
                return
            return self.render("login.html")

        self.send_error(404)

    def render(self, file):
        path = os.path.join(TEMPLATES, file)
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(open(path, "rb").read())

    def render_admin(self):
        messages = load_messages()
        rows = ""
        for m in messages:
            rows += f"<tr><td>{m['name']}</td><td>{m['email']}</td><td>{m['subject']}</td><td>{m['content']}</td></tr>"

        html = open(os.path.join(TEMPLATES, "admin.html"), encoding="utf-8").read()
        html = html.replace("{{rows}}", rows)

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def redirect(self, to):
        self.send_response(302)
        self.send_header("Location", to)
        self.end_headers()

    def is_logged(self):
        cookie = self.headers.get("Cookie", "")
        return "session=ok" in cookie

    def get_type(self, path):
        if path.endswith(".css"): return "text/css"
        if path.endswith(".js"): return "application/javascript"
        return "text/html"

def main():
    server = HTTPServer((HOST, PORT), Handler)
    print(f"Servidor activo en http://{HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    main()
