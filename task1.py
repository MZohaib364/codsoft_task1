#TASK 1
#TO DO LIST APPLICATION


import tkinter as tk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        # Task Entry
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task Button
        add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_task_button.grid(row=0, column=1, padx=10, pady=10)

        # To-Do List
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
        self.listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Remove Task Button
        remove_task_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        remove_task_button.grid(row=2, column=0, padx=10, pady=10)

        # Message Label
        self.message_label = tk.Label(root, text="")
        self.message_label.grid(row=2, column=1, padx=10, pady=10)

        # Quit Button
        quit_button = tk.Button(root, text="Quit", command=root.destroy)
        quit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.message_label.config(text=f"Task '{task}' added to your to-do list.", fg="green")
        else:
            self.message_label.config(text="Task cannot be empty!", fg="red")

    def remove_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            removed_task = self.tasks.pop(task_index)
            self.listbox.delete(task_index)
            self.message_label.config(text=f"Task '{removed_task}' removed from your to-do list.", fg="green")
        else:
            self.message_label.config(text="Please select a task to remove.", fg="red")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
