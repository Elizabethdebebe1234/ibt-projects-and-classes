from collections import deque

# Create an empty queue
bank_queue = deque()

# Enqueue (add) five customers
bank_queue.append("Almaz")
bank_queue.append("Dawit")
bank_queue.append("Sara")
bank_queue.append("Abel")
bank_queue.append("Hana")

print("Customers in queue:")
print(bank_queue)

print("\nServing customers:")

# Serve customers in FIFO order
while bank_queue:
    customer = bank_queue.popleft()
    print(f"{customer} has been served.")

print("\nQueue after serving everyone:")
print(bank_queue)
