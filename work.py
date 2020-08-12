#fabonacci sequense
num_of_terms = int(input(" How many terms? "))


first1, second2 = 0, 1
count = 0

# check if the number of terms is valid
if num_of_terms <= 0:
   print("Please enter a positive number")
elif num_of_terms == 1:
   print("Fibonacci sequence upto",num_of_terms,":")
   print(first1)
else:
   print("Fibonacci sequence:")
   while count < num_of_terms:
       print(first1)
       nth = first1 + second2
       # update values
       first1 = second2
       second2 = nth
       count += 1
