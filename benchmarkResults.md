### GET

Server Software:        Werkzeug/1.0.1
Server Hostname:        127.0.0.1
Server Port:            3000

Document Path:          /titles
Document Length:        2596979 bytes

- Concurrency Level:      10
- Time taken for tests:   10.095 seconds
- Complete requests:      161
Failed requests:        0
Total transferred:      418143103 bytes
HTML transferred:       418113619 bytes
- Requests per second:    15.95 [#/sec] (mean)
- Time per request:       627.023 [ms] (mean)
Time per request:       62.702 [ms] (mean, across all concurrent requests)
Transfer rate:          40449.76 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0       3
Processing:   141  583 184.0    587    1090
Waiting:      128  536 175.4    522    1035
Total:        141  584 184.0    587    1091

Percentage of the requests served within a certain time (ms)
  50%    587
  66%    667
  75%    714
  80%    730
  90%    805
  95%    878
  98%    976
  99%   1048
 100%   1091 (longest request)

 ## POST
- Concurrency Level:      10
- Time taken for tests:   10.000 seconds
- Complete requests:      6451
Failed requests:        0
Total transferred:      1251494 bytes
Total body sent:        1640840
HTML transferred:       109667 bytes
- Requests per second:    645.07 [#/sec] (mean)
- Time per request:       15.502 [ms] (mean)
Time per request:       1.550 [ms] (mean, across all concurrent requests)
Transfer rate:          122.21 [Kbytes/sec] received
                        160.23 kb/s sent
                        282.44 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.6      0      16
Processing:     2   15   9.5     13      84
Waiting:        0   15   9.4     13      84
Total:          3   15   9.4     13      86

Percentage of the requests served within a certain time (ms)
  50%     13
  66%     16
  75%     18
  80%     20
  90%     26
  95%     34
  98%     45
  99%     52
 100%     86 (longest request)

 ## PUT

- Concurrency Level:      10
- Time taken for tests:   10.013 seconds
- Complete requests:      1126
Failed requests:        0
Total transferred:      261232 bytes
Total body sent:        259915
HTML transferred:       61930 bytes
- Requests per second:    112.45 [#/sec] (mean)
- Time per request:       88.929 [ms] (mean)
Time per request:       8.893 [ms] (mean, across all concurrent requests)
Transfer rate:          25.48 [Kbytes/sec] received
                        25.35 kb/s sent
                        50.82 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       1
Processing:    27   88  50.8     77     373
Waiting:       27   87  50.7     77     373
Total:         27   88  50.8     77     373

Percentage of the requests served within a certain time (ms)
  50%     77
  66%     94
  75%    112
  80%    124
  90%    156
  95%    189
  98%    233
  99%    267
 100%    373 (longest request)