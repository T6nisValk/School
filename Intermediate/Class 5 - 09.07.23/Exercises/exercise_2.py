import re
ip_address = "192.04.030.020".split(".")

pattern = r"^0"
result = ".".join([re.sub(pattern, "", num) for num in ip_address])
print(result)
