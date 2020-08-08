import hashlib

hasher=hashlib.md5()
hasher=hashlib.sha256()
file_name = "./yield_test.py"
chunk_size = 5

with open(file_name, "rb") as fr:
  for chunk in iter(lambda:fr.read(chunk_size), b''):
    hasher.update(chunk)
print(hasher.hexdigest())

