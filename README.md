## Redixx

Minimal redis clone built in Python for the sake of learning

To run the server:

    python server.py
  
To connect:

    telnet localhost 9000

    # sample input/output
    SET foo 2
    OK
    GET foo
    2
    DEL foo
    OK
    RPUSH numbers 2
    OK
    RPUSH numbers 4
    OK
    RPUSH numbers 6
    OK
    LPOP numbers
    2
    RPOP numbers
    6
  
  
