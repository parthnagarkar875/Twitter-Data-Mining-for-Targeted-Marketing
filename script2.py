from proxyscrape import create_collector

collector = create_collector('hello122', 'socks4')

# Retrieve any http proxy
proxy = collector.get_proxy()
print(proxy)