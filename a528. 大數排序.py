while True:
  try:
    n = int(input())
    data = []          
    for i in range(n):
      data.append(int(input()))  
    data.sort()      
    for i in data:
      print(i)
  except:
    break
