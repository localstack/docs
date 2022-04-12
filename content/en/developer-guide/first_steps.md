### Running Localstack

Once you have cloned the localstack repository, and setup the environment, with dependencies installed,
You should be able to create the python virtualenv with

  ```bash
  virtualenv -p 3.8 venv 
  source venv/bin/activate 

  ```
 it will create the virtualenv with the python version 3.8, and load it.
 
 Then, to install all the libraries into the containers, run 
  ```bash
  make install-dev 
  ```
  
  Finally, you should able to run 
  ```bash
  make start 
  ```
  You will see localstack running, and the url to http://localhost:4566/ shows `{"status": "running"}`
  
  If you are looking for running directly the Python repo
 
   ```bash
   localhost/bin$ python3 localstack start --host 
  ```

### Debugging Local changes

```
   python3 -m pdb localstack start --host
   python3 -m pdb bin/localstack start --host  

```
