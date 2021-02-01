from spython.main import Client

Client.build('/.alpine.def',image='alpine.sif',build_folder='./')
Client.run('./alpine.sif')

