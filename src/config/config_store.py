from threading import RLock
from copy import deepcopy

class ConfigStore:
    def __init__(self, initial_config):
        self._lock = RLock()
        self._config = deepcopy(initial_config)

    def get_snapshot(self):
        with self._lock:
            return deepcopy(self._config)

    def set(self, new_config):
        with self._lock:
            self._config = deepcopy(new_config)