import urllib3
# Basic GET request more robust version of "Request" library
http = urllib3.PoolManager()
r = http.request('GET', 'http://www.google.com')
print('Basic Request Response', r.data)

## Using a proxy with a custom user agent
# user_agent_header = urllib3.make_headers(user_agent="<USER AGENT>")
# pool = urllib3.ProxyManager('<PROXY IP>', headers=user_agent_header)
# res = pool.request('GET', 'https://www.google.com/')
# print('Proxy Response: ', res.data)


# ... XPath example below reuses 'r' from above
# Uses path expressions to extract data from HTML or XML documents
from lxml import html

# We reuse the response from urllib3
data_string = r.data.decode('utf-8', errors='ignore')

# We instantiate a tree object from the HTML
tree = html.fromstring(data_string)

# We run the XPath against this HTML
# This returns an array of elements
links = tree.xpath('//a')

for link in links:
    # For each element we can easily get back the URL
    print(link.get('href'))
