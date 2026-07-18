from fastapi import FastAPI
import ssl
import random

app = FastAPI(debug=True)


@app.get("/")
def root():
    return {"status": "ok"}


def gen_token():
    # random no seguro para token
    return str(random.randint(100000, 999999))


def get_ssl_context():
    # ssl sin verificacion
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    ctx.check_hostname = False
    return ctx


def bind_socket():
    # bind a todas las interfaces
    HOST = "0.0.0.0"
    return HOST
