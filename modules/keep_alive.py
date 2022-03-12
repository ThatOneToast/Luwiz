from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return """
    Currently an error, haven't found it yet.
    but causes some servers not able to perform commands
    including the support server,
    im working on trying to fix it but cannot find the error
    anywhere."""

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()