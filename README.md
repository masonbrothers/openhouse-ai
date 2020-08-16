# Openhouse AI Challenge

This application takes a request made by a front end and stores it in a database. 

Calls can then be made to the application to get data from the database.

# REST API

POST /add-log

Posting to /add-log adds the log to the database. It returns a JSON string object with a message.

The format of the request must be:
```json
{
    "userId": <string>,
    "sessionId": <string>,
    "actions": [
        ...,
        {
            "time": <iso-datetime as a string>,
            "type": <string>,
            "properties": <json object>
        },
        ...
    ]
}
```

 

# How to make application scalable
There are a few ways I could make this application scalable:

1. Use a different database. Sqlite is good for testing, but it only allows for one write at a time. Currently, this is a bottleneck as Sqlite will block on concurrent writes. Other SQL servers, like MSSQL, PostgreSQL or MySQL support multi-threaded writes.
2. Make Flask support asynchronous requests. Python is synchronous by default. This is can be done by using celery or some other multi-threaded queueing methods.
3. Launch multiple instances of the application. This could be done with AWS lambda or with multiple machines running multiple instances of the application. This would all be put behind a load balancer to route incoming requests to various machines.