first_var = 20
second_var = 50

print("before---")
print('first_var- ', first_var, 'second_var- ', second_var)
first_var = second_var + first_var
second_var = first_var - second_var
first_var = first_var - second_var

print("After---")
print('first_var- ', first_var, 'second_var- ', second_var)