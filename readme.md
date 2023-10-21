# SIMPLE-1PX-IP-TRACKER
- Simple ip tracker using 1px image (PoC).
- But it works well !!

# Install & Start
## Running with Python
```shell
git clone https://github.com/whackur/simple-1px-ip-tracker
pip install -r requirements.txt
```
## Running with pm2 & venv
```shell
pm2 start app.py --interpreter ..../simple-1px-ip-tracker/.venv/bin/python
```


# Usage
## Setup 
- Replace 'example.com' with your host.
- Insert 1px image with HTML code in blog or somewhere.
```html
<img src="http://example.com/tracker_for_me" />
```

## Replace ip_addr variable
- Nginx Options.
- SET proxy_pass 
```
    location / {
        proxy_redirect off;
        proxy_pass http://localhost:8080;
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-Host $http_host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
```

## Replace Port in app.py
```python
app.run(host="0.0.0.0", port=1005)
```

## URL Target
- What is my ip? : http://example.com/my_ip

or
```bash
curl http://example.com/my_ip
```

- IP Address will save : http://example.com/tracker_for_me
- IP Logs list on : http://example.com/tracker_list_for_me

# Reference
- IP Database : https://github.com/maxmind/GeoIP2-python
- My Youtube Link : https://youtu.be/xMJBdjhxAwk
