# KEEP TRACK OF TODOS USING A LIST
todo_list = []

# I need a way to add todos
def add_todo(todo):
    # we recieve a todo, which is a string
    todo_list.append(todo)

# print the empty todo list
print(todo_list)
add_todo("feed the cat")
# print todo_list again to make sure our todo got added
print(todo_list)

# I need to be able to delete todos
def delete_todo(index):
    # del todo_list[index]
    try:
        todo_list.pop(index)
    except IndexError:
        print("🔥Sorry, there is nothing to remove here!🔥")
delete_todo(0)
print(todo_list)
delete_todo(0)
print(todo_list)

# I need to print my todos

# Show user the main menu