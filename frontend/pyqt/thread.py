# ----------------------------------------------------------------------------
#
# Copyright 2018 EMVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ----------------------------------------------------------------------------


# Standard library imports

# Related third party imports
from PyQt5.QtCore import QMutexLocker, QThread

# Local application/library specific imports
from core.thread_ import ThreadBase


class PyQtThread(ThreadBase):
    def __init__(self, mutex=None, worker=None):
        #
        super().__init__(mutex=mutex, worker=worker)

        #
        self._thread = PyQtThreadImpl(
            mutex=mutex, parent=self, worker=worker
        )

    def _start(self):
        self._thread.start()

    def stop(self):
        self._thread.stop()

    def run(self):
        self._thread.run()

    def join(self):
        self._thread.join()

    def wait(self):
        self._thread.wait()

    def acquire(self):
        return self._thread.acquire()

    def release(self):
        self._thread.release()

    @property
    def worker(self):
        return self._thread.worker

    @worker.setter
    def worker(self, obj):
        self._thread.worker = obj


class PyQtThreadImpl(QThread):
    def __init__(self, mutex=None, parent=None, worker=None):
        #
        super().__init__()

        #
        self._worker = worker
        self._mutex = mutex
        self._parent = parent

    def stop(self):
        with QMutexLocker(self._mutex):
            self._parent.is_running = False

    def run(self):
        while self._parent.is_running:
            if self._worker:
                self._worker()

    def join(self):
        while self._parent.is_running:
            pass

    def acquire(self):
        return QMutexLocker(self._mutex)

    def release(self):
        pass

    @property
    def worker(self):
        return self._worker

    @worker.setter
    def worker(self, obj):
        self._worker = obj
