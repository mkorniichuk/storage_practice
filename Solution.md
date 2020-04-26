## Possible solution:

```
$ docker run --rm -v $(pwd)/main:/src -v db:/db -d -p 80:5000  --name main mkorniichuk/flask

$ docker run --rm -v $(pwd)/support:/src -v db:/db:ro -d -p 81:5000 --name support mkorniichuk/flask

======================================================

$ docker stop main
$ docker stop support

$ docker network create --internal net1

$ docker run --rm -v $(pwd)/main:/src -v db:/db -d --name main --network net1 mkorniichuk/flask

$ docker run --rm -v $(pwd)/support:/src -v db:/db:ro -d --name support --network net1 mkorniichuk/flask

$ docker run -it -p 80:80 -v $(pwd)/nginx.config:/etc/nginx/conf.d/default.conf --network int --name rev_proxy -d nginx

$ docker network connect bridge rev_proxy
```