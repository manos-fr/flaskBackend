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
 <!-- Document Path:          /titles/999999489697
Document Length:        55 bytes

Concurrency Level:      10
Time taken for tests:   10.000 seconds
Complete requests:      5201
Failed requests:        0
Total transferred:      1206632 bytes
Total body sent:        1193090
HTML transferred:       286055 bytes
Requests per second:    520.10 [#/sec] (mean)
Time per request:       19.227 [ms] (mean)
Time per request:       1.923 [ms] (mean, across all concurrent requests)
Transfer rate:          117.84 [Kbytes/sec] received
                        116.51 kb/s sent
                        234.35 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       5
Processing:     5   19   8.7     17      81
Waiting:        5   19   8.6     17      81
Total:          5   19   8.6     17      82

Percentage of the requests served within a certain time (ms)
  50%     17
  66%     19
  75%     20
  80%     22
  90%     27
  95%     36
  98%     49
  99%     58
 100%     82 (longest request) -->

 Document Path:          /titles/999999489697
Document Length:        55 bytes

Concurrency Level:      10
Time taken for tests:   10.001 seconds
- Complete requests:      8030
Failed requests:        0
Total transferred:      1862960 bytes
Total body sent:        1840931
HTML transferred:       441650 bytes
- Requests per second:    802.93 [#/sec] (mean)
- Time per request:       12.454 [ms] (mean)
Time per request:       1.245 [ms] (mean, across all concurrent requests)
Transfer rate:          181.91 [Kbytes/sec] received
                        179.76 kb/s sent
                        361.68 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.4      0      17
Processing:     2   12   5.1     11      61
Waiting:        2   12   5.1     11      61
Total:          4   12   5.1     11      61

Percentage of the requests served within a certain time (ms)
  50%     11
  66%     11
  75%     12
  80%     13
  90%     17
  95%     22
  98%     28
  99%     34
 100%     61 (longest request)