def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst

print(odd_indices([4, 3, 7, 10, 11, -2]))