import tkinter as tk

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(App,self).__init__()

        self.title("Button")
        self.geometry('300x185')
        
        self.bt = tk.Button(self,text="LOAD")
        self.bt.pack()

        self.la = tk.Label(self)
        self.la.pack()

        self.bt["command"] = self.button_handle
        
    def button_handle(self):
        self.la.config(text = "hello world")

if __name__=="__main__":
    app = App()
    app.mainloop()