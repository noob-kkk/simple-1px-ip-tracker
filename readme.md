# SIMPLE-1PX-IP-TRACKER
- Simple ip tracker using 1px image (PoC).
- But it works well !!

# Install & Start
```shell
git clone https://github.com/whackur/simple-1px-ip-tracker
pip install -r requirements.txt
python app.py
```
# Usage
## Setup 
- Replace 'example.com' with your host.
- Insert 1px image with HTML code in blog or somewhere.
```html
<img src="http://example.com/tracker_for_me" />
```
## Replace ip_addr variable
- set your ip_addr
```python
    ip_addr = str(request.remote_addr)  # case of public ip
    ip_addr = str(request.environ['HTTP_X_REAL_IP'])  # case of reverse proxy
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
