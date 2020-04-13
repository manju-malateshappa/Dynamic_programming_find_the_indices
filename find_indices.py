
# create the dynamic programming tables
def create_dynamic_programming_tables(n):
  #intialise 3 tables with MINIMUM_VALUE 
  table1 = [MINIMUM_VALUE] * (n+1)
  table2 = [MINIMUM_VALUE] * n
  table3= [MINIMUM_VALUE] * (n - 1)

  #create the dp tables
  for i in range(n - 1, -1, -1): 
    table1[i] = max(table1[i + 1], arr[i]) 
  for i in range(n - 2, -1, -1):
    table2[i]=max(table2[i + 1],table1[i + 1] - arr[i])
  for i in range(n - 3, -1, -1): 
    table3[i] = max(table3[i + 1],table2[i + 1] + arr[i])

  return table1, table2, table3

# finds the index value
def find_the_idex(table, start_position, end_position):
  for i in range(start_position, end_position):
    if table[i]!=table[i+1]:
      return i

# # finds the indices i<j<k such that A[i] - A[j] + A[k] is maximized
def findIndicesOfMaximumVales(n):
  if n < 3:
    print("The array should have atleast 3 items")
    return "Data is not enough"
  else:
    # We create 3 Dynamic programming tables
    table1, table2, table3 = create_dynamic_programming_tables(n)
    ith_index = find_the_idex(table3, 0, len(table3))
    jth_index = find_the_idex(table2, ith_index + 1, len(table2))
    kth_index = find_the_idex(table1, jth_index + 1, len(table1))
    return ith_index, jth_index, kth_index

  
# entry point for the driver
if __name__ == "__main__": 
  
    #arr = [4, 8, 9, 2, 20]
    arr = [2,8,2,6,4,1,9,3,10]
    #arr = []
    length_of_array = len(arr)
    print(length_of_array)
    if length_of_array > 3:
    # To reprsent minus infinite 
      MINIMUM_VALUE = -100000000

      i,j,k = findIndicesOfMaximumVales(length_of_array)
    
      print("index_values", i,j,k)
      print(" a[i] ", arr[i])
      print(" a[j] ", arr[j])
      print(" a[k] ", arr[k])
      result = arr[i] -arr[j] + arr[k]
      print("maximum value is = ",result)
    else :
      print("The array should have atleast 3 items.. cannot proceed....")

