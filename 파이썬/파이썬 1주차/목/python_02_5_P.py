todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]

to_do ,d_day = input(), int(input()) 
to_do_tuple = to_do, d_day #('Soccer Contest', 10)

todo.append(to_do_tuple) #[('Python Homework', 3), ('Assay', 4), ('Vacation', 100), ('Soccer Contest', 10)]
print(todo)

