import re

log1 = """15:30:45 [error] 1234#1234: *56789 connect() failed (111: Connection refused) while connecting to upstream, client: 192.168.1.100, server: example.com, request: “GET /api/data HTTP/1.1”, upstream: “http://127.0.0.1:8000/api/data”, host: “/"example.com”, referrer: “https://example.com"""
log2 = """2024/07/11 16:15:20 [error] 1234#1234: *67890 open() “/usr/share/nginx/html/not_found.html” failed (2: No such file or directory), client: 192.168.1.101, server: example.com, request: “GET /nonexistent-page HTTP/1.1”, host: “example.com”,
referrer: “https://example.com/”"""

pattern = r"(\d+\:\d+\:\d+) (\[\w*\]) (\d+\#\d+\:) (\*\d+)"
data = re.search(pattern, log1)
time = data.group(1)
typeerror = data.group(2)
siblingport = data.group(3)
id = data.group(4)

parse_data = {
    "time" : time,
    "typeerror" : typeerror,
    "siblingport" : siblingport,
    "id" : id
}

print (parse_data)