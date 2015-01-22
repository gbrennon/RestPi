RestPi
======

Minimalist REST API built with Flask!

Start the server with

```
sudo python RestPi.py
```

Check if the server is online:

```
<raspberry_ip>:5000/
```

Set a pin 5 as Input:

```
<raspberry_ip>:5000/setInput?pin=5
```

Read pin 5 value:

```
<raspberry_ip>:5000/readPin?pin=5
```

Set pin 6 to Output and set the state(1 = on, 0 = off):


```
<raspberry_ip>:5000/setOutput?pin=6
<raspberry_ip>:5000/writePin?pin=6&state=1
```
