import json
data = {
    "name":"zq",
    "age":3,
    "company":"zhongtong"
}
print(type(data))
data1 = json.dumps(data)
print(type(data1))
print(data1)
data2=json.loads(data1)
print(type(data2))