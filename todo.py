todo = {}

def list_todos():
    if not todo:
        
        print("There is no todd")
        
        return
    else:
        for key,value in todo.items():
            print(f"{key}. {value}")
            

def add_todo():
    
    key = input("Enter todo number: ").strip()
    
    value = input("Enter new todo: ").strip()
    
    if key and value:
        todo[key] = value
        
        print("Todo item added.")
        
    else:
        print("Empty todo was not added.")

def update_todo():
    
    list_todos()
    
    if not todo:
        return
    
    key = input("Enter todo number to update: ").strip()
    
    if key in todo:
        new_text = input("Enter new to do textt: ").strip()
        if new_text:
            todo[key] = new_text
            print("Todo updated.")
        else:
            print("Update not successful")
    else:
        print("there is no to do number.")
        

def delete_todo():
    
    list_todos()
    
    if not todo:
        return
    
    key = input("Enter todo number to delete: ").strip()
    
    if key in todo:
        removed = todo.pop(key)
        print(f"Removed todo: {removed}")
    else:
        print("Invalid todo number.")
        

def main():
    
    while True:
        print("\nTodo List ")
        
        print("1. List todos")
        print("2. Add todo")
        print("3. Update todo")
        print("4. Delete todo")
        print("5. Exit")
        print("\n")
        
        choice = input("Choose option: ").strip()
        
        if choice == "1":
            list_todos()
            
            
        elif choice == "2":
            add_todo()
            
            
        elif choice == "3":
            update_todo()
            
            
        elif choice == "4":
            delete_todo()
            
            
        elif choice == "5":
            print("Exit.")
            break
        
        else:
            print("Invalid optiion")
            
            
if __name__ == "__main__":
    main()  
        

