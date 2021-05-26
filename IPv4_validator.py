def ip_validator(ip):
	'''Verifys the validity of IPv4 addresses'''
    ip = ip.split('.')
    return all(n.isdigit() for n in ip) and all(0 <= int(n) <= 255 for n in ip) \
           and len(ip) == 4


print(
	'Valid ip' if ip_validator(input('Input a ip: ')) else 'Not valid ip'
)