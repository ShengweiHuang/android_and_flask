# Android java connect to flask server example

## Requirement
Server side:
```
python 3
flask
```
## How to run
### Server side:
add ```server_flask.py``` to your server
```
python3 server_flask.py
```
### Client side:<br>
add ```urlConnection.java``` into your project, and add these code to where you want to execute
```
urlConnect uc = new urlConnect(targetURL);
uc.start();
while (uc.getLockStatus()) {}
String result = uc.getResult();
```
targetURL means your server IP and port and url input parameters, here's an example
```
http://35.185.187.199:8000/android?input=123
```
