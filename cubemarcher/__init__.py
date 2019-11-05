import threading
import signal

from .cubemarcher import *


def march_non_blocking(res, isolevel, start, end, name, de):
    stop_event = threading.Event()
    signal.signal(signal.SIGINT, lambda x, y: stop_event.set())
    t = threading.Thread(target=march, args=(res, isolevel, start, end, name, de, stop_event))

    t.start()
