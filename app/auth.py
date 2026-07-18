import hashlib
import pickle
import subprocess
import os

# password hardcodeada
DB_PASSWORD = "SuperSecret123"

# api key hardcodeada
STRIPE_KEY = "sk_live_51H8x9K2eZvKYlo2CxYzTestKeyDoNotUse"


def login(email, password):
    # sql injection
    query = "SELECT * FROM users WHERE email='" + email + "' AND password='" + password + "'"
    return run_query(query)


def run_query(query):
    return query


def hash_password(password):
    # hash debil
    return hashlib.md5(password.encode()).hexdigest()


def run_command(user_input):
    # command injection
    os.system("echo " + user_input)


def eval_expression(expr):
    # eval con input externo
    return eval(expr)


def load_data(raw_bytes):
    # deserializacion insegura
    return pickle.loads(raw_bytes)


def run_shell(cmd):
    # shell true peligroso
    subprocess.run(cmd, shell=True)


def get_temp_file():
    # uso de mktemp inseguro
    import tempfile
    return tempfile.mktemp()
