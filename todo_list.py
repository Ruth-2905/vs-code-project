import json

def save_to_file(todos, filename = "todo_list.txt"):
     # Save to todo_list.txt
    with open(filename, "w") as f:
        print("Saving to file todo_list.txt")
        json.dump(todos, f, indent=4)

def load_from_file(filename = "todo_list.txt"):
    try:
        with open(filename, "r") as f:
            print(f"Reading previous data from {filename}")
            todos = json.load(f)
            return todos
    except FileNotFoundError:
        return []   


def add_to_list(todo_list, item):
    todo_list.append(item)
    print(f"added {item} to list")

def remove_from_list(todo_list, index):
    item = todo_list.pop(index)
    print(f"removed {item} from list")
  
def view_todo_list(todo_list):
    if len(todo_list) <= 0:
        print("list is empty")
    for index, todo in enumerate(todo_list, start=1):
        print(f"{index}. {todo} ")
   
if __name__== "__main__":
    todo_list = load_from_file()
    while(True):
        print("")
        print("What would you like to do")
        user_action = input("Enter 'V' for view, 'A' for add, 'R' for remove: ")
        print("")

        if user_action.lower() == "v":
            view_todo_list(todo_list = todo_list)
        elif user_action.lower() == "r":
            index = input("Enter the item index: ")
            remove_from_list(todo_list = todo_list, index = int(index))
            save_to_file(todo_list)
        elif user_action.lower() == "a":
            item = input("Enter name of item: ")
            add_to_list(todo_list = todo_list, item = item)
            save_to_file(todo_list)
        else:
            print("invalid input")

        print("")
        terminate = input("Do you want to quit? [y or n]:  ")

        if terminate.lower() == "y":
            break
     
    


