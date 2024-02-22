def megabytes_to_bytes(megabytes):
  bytes = megabytes * 1000000
  return bytes

def main():
  b = megabytes_to_bytes(10) 
  print(b)
  b = megabytes_to_bytes(64)
  print(b)
main()
