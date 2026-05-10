bind = "0.0.0.0:8000"

workers = 4

worker_class = "sync"

threads = 2

timeout = 120

keepalive = 5

max_requests = 1000

max_requests_jitter = 50

reload = True

accesslog = "-"

errorlog = "-"

loglevel = "info"

capture_output = True

enable_stdio_inheritance = True

proc_name = "ludo_multiplayer"

def when_ready(server):
    server.log.info("Gunicorn Server Ready")

def on_starting(server):
    server.log.info("Starting Ludo Server")

def worker_int(worker):
    worker.log.info("Worker Interrupted")

def pre_fork(server, worker):
    server.log.info("Preparing Worker")

def post_fork(server, worker):
    server.log.info("Worker Started")

def worker_abort(worker):
    worker.log.info("Worker Abort")
