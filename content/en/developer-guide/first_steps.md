### Running Localstack

Once you have cloned the LocalStack repository, and setup the environment, with the OS System dependencies installed,
you should be able to create the Python virtualenv.

We recommend create the virtualenv inside `.venv`, 
which is automatically created whith the Make utility available in the root of the repository.

Create the virtualenv with

{{< command >}}
make venv
{{< / command >}}

 The command above will create the Python virtualenv with the dependencies.
 Then, to build and install all the Python dependencies and third-party libraries into the venv, excecute 
  
{{< command >}}
make install 
{{< / command >}}

Finally, you should able to run Localstack with 
{{< command >}}
make start
{{< / command >}}

You will see LocalStack running, and the url to http://localhost:4566/ shows `{"status": "running"}`

If you are looking for running LocalStack directly with Python, execute
 
{{< command >}}
localhost/bin$ python3 localstack start --host
{{< / command >}}

### Debugging Local changes

{{< command >}}
python3 -m pdb localstack start --host
python3 -m pdb bin/localstack start --host  
{{< / command >}}

Also, consider the debugging flags at
https://docs.localstack.cloud/localstack/configuration/#debugging

{{< command >}}
  DEVELOP=1 SERVICES=s3,ec2, DEBUG=1  make start
{{< / command >}}

### Initialize Services

{{< command >}}
SERVICES=s3 DEBUG=1  make start
{{< / command >}}
