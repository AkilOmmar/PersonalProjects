import RPi.GPIO as GPIO
import tkinter as tk
import time
import threading

class MyTkinterApp(threading.Thread):
       timeVal = 1
       ProgramExit = False
       
       def __init__(self):
              threading.Thread.__init__(self)
              self.start()

       def callback(self):
              print ('Thanks, see you later .....')
              self.ProgramExit = True
              self.master.quit()

       def run(self):
              self.master = tk.Tk()
              self.master.protocol("WM_DELETE_WINDOW", self.callback)
              self.master.title("Blinking led")
              self.master.configure(background="black")
              self.master.geometry('250x200')
              # myFont=tkFont.Font(family = 'Helvetica', size= 30, weight = 'bold')
              #c=tk.Canvas(master, width=250, height=200)
              #c.pack()

              w = tk.Scale(self.master, from_=1, to=5, tickinterval=1, showvalue=0, orient=tk.HORIZONTAL, label="Blinking Time for Led (seconds)", bg="black", fg="white", activebackground='blue', command=self.changetime)
              w.pack(side=tk.TOP, fill=tk.BOTH, pady=10, padx=10)

              #exitButton = Button(master, text="Exit", font=myFont, command=exitProgram, height=2, width=6)
              exitButton = tk.Button(self.master, text="Exit", command=self.callback, highlightcolor="white", height=3, width=6, bg="black", fg="white")
              exitButton.pack(pady=15)

              self.master.mainloop()

       def changetime(self,duty):
               self.timeVal=int(duty)
               print ('The value is:', self.timeVal)
              
       def get_timeVal(self):
               return self.timeVal

       def get_ProgramExitTrigger(self):
               return self.ProgramExit

Myapp = MyTkinterApp()

# GPIO Setup
PIN = 11
#timeVal = 1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

while Myapp.get_ProgramExitTrigger() == False:
       GPIO.output(PIN, True)
       time.sleep(int(Myapp.get_timeVal()))
       print ('LED OFF')
       GPIO.output(PIN, False)
       time.sleep(int(Myapp.get_timeVal()))
       print ('LED ON')

GPIO.cleanup()
