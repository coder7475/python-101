import threading

def print_numbers():
    for i in range(10):
        print(i)

thread = threading.Thread(target=print_numbers)  # Create a Thread object with target function
thread.start()  # Start the thread, begins executing print_numbers in parallel
thread.join()   # Wait for the thread to finish before continuing
