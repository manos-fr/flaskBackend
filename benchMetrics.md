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
