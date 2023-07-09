import re

ip_address = "192.04.030.020".split(".")

result = ".".join([re.sub(r"^0", "", num) for num in ip_address])
print(result)
