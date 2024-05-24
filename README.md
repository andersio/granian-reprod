
### Starlette/FastAPI/Granian combinations

```
granian = { version = "1.3.2", extras = ["reload"] }
fastapi = "0.111.0"
starlette = "0.37.2"
```

### Without BaseHTTPMiddleware

#### c=20

```
make run use_http_middleware=no
make reproduce c=20 n=200
```

```
Concurrency Level:      20
Time taken for tests:   48.946 seconds
Complete requests:      200
Failed requests:        0
Total transferred:      200022600 bytes
HTML transferred:       200000000 bytes
Requests per second:    4.09 [#/sec] (mean)
Time per request:       4894.614 [ms] (mean)
Time per request:       244.731 [ms] (mean, across all concurrent requests)
Transfer rate:          3990.81 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    2   0.3      2       3
Processing: 46928 46929   0.6  46929   46932
Waiting:        1   21   8.5     21      33
Total:      46930 46931   0.4  46931   46932
```

#### c=50
```
make run use_http_middleware=no
make reproduce c=50 n=500
```


```
Concurrency Level:      50
Time taken for tests:   184.479 seconds
Complete requests:      500
Failed requests:        0
Total transferred:      500056500 bytes
HTML transferred:       500000000 bytes
Requests per second:    2.71 [#/sec] (mean)
Time per request:       18447.922 [ms] (mean)
Time per request:       368.958 [ms] (mean, across all concurrent requests)
Transfer rate:          2647.11 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0       2
Processing: 15363 18442 2126.5  18622   22059
Waiting:        5   13   3.1     13      23
Total:      15364 18442 2126.4  18622   22060
```


### With BaseHTTPMiddleware


#### c=20
```
make run use_http_middleware=yes
make reproduce c=20 n=200
```

```
Concurrency Level:      20
Time taken for tests:   98.745 seconds
Complete requests:      200
Failed requests:        0
Total transferred:      200022600 bytes
HTML transferred:       200000000 bytes
Requests per second:    2.03 [#/sec] (mean)
Time per request:       9874.461 [ms] (mean)
Time per request:       493.723 [ms] (mean, across all concurrent requests)
Transfer rate:          1978.18 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       1
Processing:  8198 9869 1328.1  10135   12206
Waiting:        4    9   2.9      9      24
Total:       8199 9869 1328.1  10136   12207
```

#### c=50
```
make run use_http_middleware=yes
make reproduce c=50 n=500
```

```
Concurrency Level:      50
Time taken for tests:   384.401 seconds
Complete requests:      500
Failed requests:        0
Total transferred:      500056500 bytes
HTML transferred:       500000000 bytes
Requests per second:    1.30 [#/sec] (mean)
Time per request:       38440.139 [ms] (mean)
Time per request:       768.803 [ms] (mean, across all concurrent requests)
Transfer rate:          1270.38 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.4      0       2
Processing: 35431 38433 1934.8  38352   41227
Waiting:        6   36  12.0     36      83
Total:      35432 38434 1934.7  38353   41227
```
