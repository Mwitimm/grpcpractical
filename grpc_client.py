"""
import grpc 
import get_config_pb2
import get_config_pb2_grpc 

def run():
    #Instantiate stub on the client 
    connect = grpc.insecure_channel("localhost:8080")
    stub =  get_config_pb2_grpc.get_configStub(channel=connect)
    #Call the login info method
    response = stub.Login_info(get_config_pb2.Request(host="192.168.10.1",
    username="Martin",
    password="Javascript3c#"))
    print(response.message)
    
    
    
run()
""" 

import grpc
import time
import get_config_pb2
import get_config_pb2_grpc

def run():
    # Instantiate stub on the client
    channel = grpc.insecure_channel("localhost:8080")
    stub = get_config_pb2_grpc.get_configStub(channel=channel)

    # Define request parameters
    request = get_config_pb2.Request(
        host="192.168.10.1",
        username="Martin",
        password="Javascript3c#"
    )

    # Number of times to run the request per second
    requests_per_second = 5
    interval = 1 / requests_per_second

    try:
        while True:
            # Call the login info method
            response = stub.Login_info(request)
            print(response.message)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Client stopped.")

if __name__ == "__main__":
    run()

    