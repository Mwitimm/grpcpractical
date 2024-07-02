from concurrent import futures
import time
import grpc
import get_config_pb2
import get_config_pb2_grpc
import paramiko
import logging


logging.basicConfig(filename='server.log', filemode='a', level=logging.INFO, format='%(asctime)s - %(message)s')




class DisplayConfig(get_config_pb2_grpc.get_configServicer):
    #log in with paramiko
    def Login_info(self, request, context):
        logging.info(f"Received request from {context.peer()} at at {time.ctime()} with host={request.host}, username={request.username}")
        #print(f"Received request from {context.peer()} at {time.ctime()}  with host={request.host}, username={request.username} ")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=request.host,port=22,username=request.username,password=request.password,look_for_keys=False)
        cli =ssh.invoke_shell()
        cli.send("sys \n")
        time.sleep(0.5)
        cli.send("screen-length 0 temporary \n")
        time.sleep(0.5)
        cli.send("display ip interface brief \n")
        time.sleep(0.5)
        cli.send("dis ssh server session | no-more \n")
        cli.send("\n")
        time.sleep(0.5)
        cli.send("display cu   | no-more\n")
        time.sleep(0.5)
        data = cli.recv(999999).decode()
        ssh.close()
        #return cconfig info in the output
        return get_config_pb2.Reply(message=data)
    
    def serve(self):
        #create grpc service
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        #deploy grp server in the defined service
        
        get_config_pb2_grpc.add_get_configServicer_to_server(DisplayConfig(),server)
        #start the server
        
        server.add_insecure_port("localhost:8080")
        print("Staring server on localhost:8080 ....")
        server.start()
        print("Running........")
        _one_day_in_seconds = 60 * 60 * 24
        try:
            while True:
                time.sleep(_one_day_in_seconds)
        except KeyboardInterrupt:
            print("Stopping......")
            server.stop(True)
            
            
            
            
server_object = DisplayConfig()

server_object.serve()
        