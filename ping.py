import os

proxy = 'http://186.96.125.235:999'

os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
print('#' * 60)
ipcheck = "8.8.8.8"
print("-" * 60)
os.system(('ping {}').format(ipcheck))
