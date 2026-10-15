import concurrent.futures
import queue
import threading
import time

from overrides import overrides

CUSTOMERS_AMOUNT = 10000
WORKERS_AMOUNT = 1000

class Customer:

  def __init__(self, customer_id, customer_first_name, customer_last_name, customer_email):
    self.customer_id = customer_id
    self.customer_first_name = customer_first_name
    self.customer_last_name = customer_last_name
    self.customer_email = customer_email

class EmailSenderWorker(threading.Thread):
    def __init__(self, task_queue):
        super().__init__()
        self.task_queue = task_queue

    @overrides
    def run(self):
        while True:
            customer = self.task_queue.get()

            if customer is None:
                self.task_queue.task_done()
                break

            send_email(customer)
            self.task_queue.task_done()

class CustomThreadPool:
    def __init__(self, num_of_workers):
        self.task_queue = queue.Queue()
        self.workers = []

        for _ in range(num_of_workers):
            worker = EmailSenderWorker(self.task_queue)
            self.workers.append(worker)
            worker.start()

    def submit(self, customer):
        self.task_queue.put(customer)

    def shutdown(self):
        self.task_queue.join()

        for _ in self.workers:
            self.task_queue.put(None)

        for worker in self.workers:
            worker.join()



def send_email(customer: Customer):
  # Simulate a network delay for sending an email
  time.sleep(0.02)
  # print(f"Hello {customer.customer_first_name} {customer.customer_last_name}")


# Generate CUSTOMERS_AMOUNT mock customers
customers = [
    Customer(
        i,
        f"First{i}",
        f"Last{i}",
        f"customer{i}@example.com",
    )
    for i in range(1, CUSTOMERS_AMOUNT + 1)
]

if __name__ == "__main__":
    start_time = time.time()

    # Use a thread pool with a max limit of WORKERS_AMOUNT workers
    pool = CustomThreadPool(num_of_workers=WORKERS_AMOUNT)

    for customer in customers:
        pool.submit(customer)

    pool.shutdown()

    print(f"Thread pool finished in: {time.time() - start_time:.2f} seconds\n")
