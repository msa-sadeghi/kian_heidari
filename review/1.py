# c = 0
# while c < 3:
#     user = input("enter the username: ")
#     passw = input("enter the password: ")
#     if user == "kian" and passw == "123":
#         print("welcome", user)
#         break
#     else:
#         c+=1
#         print("user or pass is not correct")
# if c == 3:
#     print("you locked!!!")    


import tkinter as tk
def login():
    if user.get() == "kian" and passw.get() == "123":
        r.set(f"welcome {user.get()}")
    else:
        exit()      
root = tk.Tk()
user = tk.StringVar()
passw = tk.StringVar()
r = tk.StringVar()
first_frame = tk.Frame(root)
first_frame.pack()
user_label = tk.Label(first_frame, text="username")
user_label.pack(side="left")
user_text_box = tk.Entry(first_frame, textvariable=user)
user_text_box.pack(side="left")
second_frame = tk.Frame(root)
second_frame.pack()
pass_label = tk.Label(second_frame, text="password")
pass_label.pack(side="left")
pass_text_box = tk.Entry(second_frame, textvariable=passw)
pass_text_box.pack(side="left")
submit_btn = tk.Button(root, text="login", command=login)
submit_btn.pack()
result = tk.Label(root, textvariable=r)
result.pack()
root.mainloop()