import RPi.GPIO as GPIO
import tkinter as tk
import time

# GPIO Setup
PIN = 11
timeVal = 1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)
LedOn = False

master = tk.Tk()
master.title("Blinking led")
master.configure(background="black")
master.geometry('250x200')
# myFont=tkFont.Font(family = 'Helvetica', size= 30, weight = 'bold')

def changetime(duty):
        timeVal=int(duty)
        print ('The value is:', timeVal)
        while True:
              GPIO.output(PIN, True)
              time.sleep(timeVal)
              print ('LED OFF')
              GPIO.output(PIN, False)
              time.sleep(timeVal)
              print ('LED ON')

def exitProgram():
        print ('Thanks, see you later .....')
        GPIO.cleanup()
        master.quit()

#c=tk.Canvas(master, width=250, height=200)
#c.pack()

w = tk.Scale(master, from_=1, to=5, tickinterval=1, showvalue=0, orient=tk.HORIZONTAL, label="Blinking Time for Led (seconds)", bg="black", fg="white", activebackground='blue', command=changetime)
w.pack(side=tk.TOP, fill=tk.BOTH, pady=10, padx=10)

#exitButton = Button(master, text="Exit", font=myFont, command=exitProgram, height=2, width=6)
exitButton = tk.Button(master, text="Exit", command=exitProgram, highlightcolor="white", height=3, width=6, bg="black", fg="white")
exitButton.pack(pady=15)

master.mainloop()


