run: use_http_middleware=no
run: export USE_HTTP_MIDDLEWARE=$(use_http_middleware)
run:
	poetry run granian --interface asgi \
		--host 0.0.0.0 --port 8000 \
		--http auto --no-ws --loop uvloop \
		--log-level debug \
		main:app

reproduce: c=3
reproduce: n=15
reproduce: timeout=60
reproduce:
	ab -c $(c) -n $(n) -m POST -s $(timeout) http://127.0.0.1:8000/stream/pdf
