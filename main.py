from tkinter import *
root = Tk()
root['bg'] = 'light blue'
root.geometry('600x300')
root.resizable(0, 0)
root.title("MMW Website Blocker")
Label(root, text='WEBSITE BLOCKER', bg='yellow',font='arial 20 bold').pack()
Label(root,fg='green', bg='light blue', text='To remove a website go to /etc/hosts and edit the file', font='Gothic 18 bold').pack(side='bottom')
host_path ='/etc/hosts'
ip_address = '127.0.0.1'

Label(root, bg='light blue', text ='Enter Website :' , font ='arial 18 bold').place(x=5 ,y=60)
Websites = Text(root,font = 'arial 12',height='1', width = '40', wrap = WORD, padx=5, pady=5)
Websites.place(x= 150,y = 60)

def Blocker():
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))

    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                Label(root, text = 'Already Blocked' , font = 'arial 12 bold').place(x=200,y=200)
                pass
            else:
                host_file.write(ip_address + " " + website + '\n')
                Label(root, text = "Blocked", font = 'arial 12 bold').place(x=230,y =200)
    

block = Button(root, text='Block', font='Modern 12 bold', pady=5, command=Blocker, width=4, fg='red')

block.place(x=260, y=150)
root.mainloop()
