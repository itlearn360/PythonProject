from collections import deque

# Class to implement a simple queue for customer service
class CustomerServiceQueue:
    def __init__(self):
        self.queue = deque()

    # Enqueue operation to add a customer to the queue
    def enqueue(self, customer):
        self.queue.append(customer)
        print(f"Customer {customer} added to the queue.")

    # Dequeue operation to serve the first customer in the queue
    def dequeue(self):
        if not self.isEmpty():
            customer = self.queue.popleft()  # Remove from the front of the queue
            print(f"Customer {customer} has been served.")
        else:
            print("No customers in queue to serve.")

    # Peek operation to check who is next in line without removing them
    def peek(self):
        if not self.isEmpty():
            print(f"Next customer to be served: {self.queue[0]}")
        else:
            print("No customers in queue.")

    # Check if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

# Create a customer service queue
customer_service_queue = CustomerServiceQueue()

# Enqueue customers into the queue
customer_service_queue.enqueue("Alice")
customer_service_queue.enqueue("Bob")
customer_service_queue.enqueue("Charlie")

# Peek at the next customer to be served
customer_service_queue.peek()

# Dequeue customers as they are served
customer_service_queue.dequeue()
customer_service_queue.dequeue()

# Peek again to see who's next
customer_service_queue.peek()

# Dequeue the last customer
customer_service_queue.dequeue()

# Check if the queue is empty
if customer_service_queue.isEmpty():
    print("All customers have been served.")
