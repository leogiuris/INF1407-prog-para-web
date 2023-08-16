import importado as t

print(t.func(), __name__)

dic = {}

dic.get("a",lambda:print("AAAA"))()