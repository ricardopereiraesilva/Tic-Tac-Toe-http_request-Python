from tkinter import *
import actor_api

class ActorPlayer:
	def __init__(self):
		self.mainWindow = Tk()
		self.mainWindow.title("Jogo da velha")
		self.mainWindow.iconbitmap("images/icon.ico")
		self.mainWindow.geometry("400x470")
		self.mainWindow.resizable(False, False)
		self.mainWindow["bg"]="gray"

		self.mainFrame = Frame(self.mainWindow, padx=44, pady=40, bg="gray")
		self.messageFrame = Frame(self.mainWindow, padx=4, pady=4, bg="gray")

		self.empty = PhotoImage(file="images/empty.gif")		#pyimage1
		self.white = PhotoImage(file="images/white.gif")		#pyimage2
		self.red = PhotoImage(file="images/red.gif")			#pyimage3

		self.boardView=[]
		for y in range(3):
			viewTier = []
			for x in range(3):
				aLabel = Label(self.mainFrame, bd=2, relief="solid", image=self.empty)
				aLabel.grid(row=x , column=y)
				aLabel.bind("<Button-1>", lambda event, linha=y+1, coluna=x+1: self.click(event, linha, coluna))
				viewTier.append(aLabel)
			self.boardView.append(viewTier)

		self.labelMessage = Label(self.messageFrame, bg="gray", text='Clique em qualquer posição para iniciar', font="arial 14")
		self.labelMessage.grid(row=0, column=0, columnspan=3)
		self.mainFrame.grid(row=0 , column=0)
		self.messageFrame.grid(row=1 , column=0) 

		self.myBoard = actor_api.ActorAPI()

		self.mainWindow.mainloop()


	def click(self, event, linha, coluna):
		self.myBoard.click(linha, coluna)
		newState = self.myBoard.getState()
		self.labelMessage['text']=newState.getMessage()
		for x in range(3):
			for y in range(3):
				label = self.boardView[x][y]
				value = newState.getValue(x+1, y+1)
				if value==0:
					label['imag'] = self.empty
				elif value==1:
					label['imag'] = self.red
				elif value==2:
					label['imag'] = self.white 