import concurrent.futures
import threading
import time

CUSTOMERS_AMOUNT = 1000
WORKERS_AMOUNT = 10

class Customer:

  def __init__(self, customer_id, customer_first_name, customer_last_name, customer_email):
    self.customer_id = customer_id
    self.customer_first_name = customer_first_name
    self.customer_last_name = customer_last_name
    self.customer_email = customer_email

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
    # 1 single threaded solution

    print("--- 1. Single Thread Solution ---")
    start_time = time.time()

    for customer in customers:
      send_email(customer)

    print(f"Single thread finished in: {time.time() - start_time:.2f} seconds\n")


    print(f"--- 2. Thread-Per-Customer Solution ({CUSTOMERS_AMOUNT} Threads) ---")
    start_time = time.time()
    workers = []

    # Create and start a thread for each customer
    for customer in customers:
      # worker = EmailSenderWorker(customer)
      worker = threading.Thread(target=send_email, args=(customer,))
      workers.append(worker)
      worker.start()

    # Wait for all threads to complete
    for worker in workers:
      worker.join()

    print(f"{CUSTOMERS_AMOUNT} threads finished in: {time.time() - start_time:.2f} seconds\n")


    print(f"--- 3. Thread Pool Solution (Pool of {WORKERS_AMOUNT}) ---")
    start_time = time.time()

    # Use a thread pool with a max limit of WORKERS_AMOUNT workers
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS_AMOUNT) as executor:
      executor.map(send_email, customers)

    print(f"Thread pool finished in: {time.time() - start_time:.2f} seconds\n")
