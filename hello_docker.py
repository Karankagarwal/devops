import time

# Function to simulate a task
def perform_task():
    while True:
        print("Performing a task...")
        # Simulate task duration
        time.sleep(10)
        print('hello docker')

if __name__ == "__main__":
    print("Starting the application...")
    try:
        # Run your main function here
        perform_task()
    except KeyboardInterrupt:
        print("Shutting down the application...")
