# count a list recursively
lista = ["b",1,2,3,"c"]
def list_sum_recursive(input_list, acc):
   if input_list == []:
         return acc
   else:
         count = acc + 1
         tail = input_list[1:]
         return list_sum_recursive(tail, count)

print(list_sum_recursive(lista,0))

