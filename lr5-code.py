def check_order(array):
  for i in range(len(array) - 1):
    if ord(array[i]) > ord(array[i + 1]):
      return False
  return True
def main():
  arrays = []
  for i in range(5):
    print(f"Введите элементы массива {i+1}:")
    array = input().split()
    arrays.append(array)

  for i in range(5):
    if check_order(arrays[i]):
      print(f"Массив {i+1} - да")
    else:
      print(f"Массив {i+1} - нет")
if __name__ == "__main__":
  main()