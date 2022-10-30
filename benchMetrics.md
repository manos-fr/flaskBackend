## GET

### This is ApacheBench, Version 2.3 <$Revision: 1901567 $>

Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)

- Finished 801 requests

Server Software: Werkzeug/1.0.1
Server Hostname: 127.0.0.1
Server Port: 3000

Document Path: /titles

- Document Length: 2599732 bytes

- Concurrency Level: 10
- Time taken for tests: 10.009 seconds
- Complete requests: 801
- Failed requests: 780
- (Connect: 0, Receive: 0, Length: 780, Exceptions: 0)
- Non-2xx responses: 781
- Total transferred: 77856937 bytes
- HTML transferred: 77702361 bytes
- Requests per second: 80.03 [#/sec] (mean)
- Time per request: 124.952 [ms] (mean)
- Time per request: 12.495 [ms] (mean, across all concurrent requests)
- Transfer rate: 7596.66 [Kbytes/sec] received
-
- Connection Times (ms)
- min mean[+/-sd] median max
- Connect: 0 0 0.1 0 1
- Processing: 40 106 86.0 79 1617
- Waiting: 37 104 85.9 77 1613
- Total: 40 106 86.0 79 1617

Percentage of the requests served within a certain time (ms)
50% 79
66% 88
75% 108
80% 138
90% 150
95% 221
98% 377
99% 451
100% 1617 (longest request)

Table rows: 8578

## POST

### This is ApacheBench, Version 2.3 <$Revision: 1901567 $>

Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Finished 3068 requests

Server Software: Werkzeug/1.0.1
Server Hostname: 127.0.0.1
Server Port: 3000

Document Path: /titles
Document Length: 17 bytes

Concurrency Level: 10
Time taken for tests: 10.001 seconds
Complete requests: 3068
Failed requests: 1000
(Connect: 0, Receive: 0, Length: 1000, Exceptions: 0)
Non-2xx responses: 1000
Total transferred: 30194369 bytes
Total body sent: 781558
HTML transferred: 29633265 bytes
Requests per second: 306.76 [#/sec] (mean)
Time per request: 32.599 [ms] (mean)
Time per request: 3.260 [ms] (mean, across all concurrent requests)
Transfer rate: 2948.31 [Kbytes/sec] received
76.31 kb/s sent
3024.62 kb/s total

Connection Times (ms)
min mean[+/-sd] median max
Connect: 0 0 0.1 0 3
Processing: 1 32 40.5 7 317
Waiting: 1 31 40.0 7 317
Total: 1 32 40.5 8 318

Percentage of the requests served within a certain time (ms)
50% 8
66% 21
75% 73
80% 78
90% 88
95% 95
98% 106
99% 119
100% 318 (longest request)

Table rows: 8477

## PUT

### This is ApacheBench, Version 2.3 <$Revision: 1901567 $>

Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 5000 requests
Completed 10000 requests
Finished 12938 requests

Server Software: Werkzeug/1.0.1
Server Hostname: 127.0.0.1
Server Port: 3000

Document Path: /titles/tt12966696
Document Length: 53 bytes

Concurrency Level: 10
Time taken for tests: 10.000 seconds
Complete requests: 12938
Failed requests: 0
Total transferred: 2988909 bytes
Total body sent: 2938969
HTML transferred: 685767 bytes
Requests per second: 1293.76 [#/sec] (mean)
Time per request: 7.729 [ms] (mean)
Time per request: 0.773 [ms] (mean, across all concurrent requests)
Transfer rate: 291.88 [Kbytes/sec] received
287.00 kb/s sent
578.88 kb/s total

Connection Times (ms)
min mean[+/-sd] median max
Connect: 0 0 0.3 0 18
Processing: 0 7 27.3 5 1757
Waiting: 0 6 27.2 5 1755
Total: 1 7 27.3 5 1757

Percentage of the requests served within a certain time (ms)
50% 5
66% 6
75% 7
80% 7
90% 9
95% 11
98% 14
99% 20
100% 1757 (longest request)

Table rows: 8477
