import grpc
import threading
import get_config_pb2
import get_config_pb2_grpc

# Number of concurrent clients (threads) to simulate
NUM_CLIENTS = 50

# Request parameters
REQUEST_PARAMS = {
    "host": "192.168.10.1",
    "username": "Martin",
    "password": "Javascript3c#"
}

def attack():
    # Create an insecure channel to the gRPC server
    channel = grpc.insecure_channel("localhost:8080")
    stub = get_config_pb2_grpc.get_configStub(channel=channel)

    # Create a request object
    request = get_config_pb2.Request(**REQUEST_PARAMS)

    try:
        # Make continuous requests
        while True:
            response = stub.Login_info(request)
            # Print or log the response if needed
    except Exception as e:
        print(f"Error: {e}")

def simulate_attack():
    threads = []

    # Start multiple threads to simulate concurrent clients
    for _ in range(NUM_CLIENTS):
        thread = threading.Thread(target=attack)
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    simulate_attack()
