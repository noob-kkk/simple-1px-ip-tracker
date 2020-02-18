# For What?
Simple ip tracker using 1px image (PoC).

# Install & Start
```
git clone https://github.com/whackur/simple-1px-ip-tracker
pip install -r requirements.txt
python app.py
```
# How to use
### Setup 
Replace 'example.com' with your host.

Insert 1px image with HTML code in blog or somewhere.
```html
<img src="http://example.com/tracker_for_me" />
```
### URL Target
What is my ip? : http://example.com/my_ip

or
```bash
curl http://example.com/my_ip
```

IP Address will save : http://example.com/tracker_for_me

IP Logs list on : http://example.com/tracker_list_for_me