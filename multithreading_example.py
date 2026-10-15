import threading
import time

from overrides import overrides


class MyThread(threading.Thread):

    def __init__(self, jid):
        super().__init__()
        self.jid = jid

    @overrides
    def run(self):
        try:
            time.sleep(5)
            print(f'{self.jid} has finished. ident: {threading.current_thread().ident}')
        except Exception as e:
            print(f'Exception was caught with message {e}')


if __name__ == "__main__":
    workers = []
    for i in range(5):
        worker = MyThread(i+1)
        print(f'thread {i+1} is alive!')
        workers.append(worker)

    print()

    for i, worker in enumerate(workers):
        print(f'thread {i+1} is starting!')
        worker.start()

    for worker in workers:
        worker.join()

    print('Main thread is dying')