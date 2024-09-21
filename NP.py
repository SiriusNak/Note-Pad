import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button

class NakNotePad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title('Nak\'s Note Pad')
        #Text
        self.text_area : Text = Text(self.root, wrap= 'word')
        self.text_area.pack(expand= True, fill= 'both')
        #Frame
        self.button_frame : Frame = Frame(self.root)
        self.button_frame.pack()
        #Save Button
        self.save_button : Button = Button(self.button_frame, text= 'Save',command= self.save_file)
        self.save_button.pack(side= tk.LEFT)
         #Load Button
        self.load_button : Button = Button(self.button_frame, text= 'Load',command= self.load_file)
        self.load_button.pack(side= tk.LEFT)
        #Update Exisiting File Button
        self.update_existing_file_button : Button = Button(self.button_frame, text= 'Update Note', command= self.update_existing_file)
        self.update_existing_file_button.pack(side= tk.LEFT)

    def save_file(self) -> None:                              
           file_path : str =filedialog.asksaveasfilename(defaultextension= '.txt', filetypes= [('Text File', "*.txt")])
           with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
           print(f'The file was saved to: {file_path}')
    
    def load_file(self) -> None:                              
           file_path : str = filedialog.askopenfilename(defaultextension= '.txt', filetypes= [('Text File', '*.txt')])
           with open(file_path, 'r') as file:
                content: str = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.INSERT, content)
           print(f'The file loaded from: {file_path}')

    def update_existing_file(self) -> None:
         file_path : str = filedialog.askopenfilename(defaultextension= '.txt', filetypes= [('Text File', '*.txt')])
         if file_path:
            try:
              with open(file_path, 'a') as file:
                file.write(self.text_area.get(1.0,tk.END))
              print(f'The note has been updated in: {file_path}')
            except Exception as e:
              print(f'Error updating file: {e}')
         else: print('No existing file to update.')
        
    def run(self) -> None:
        self.root.mainloop()

def main() -> None:
    root : Tk = tk.Tk()
    app : NakNotePad = NakNotePad(root= root)
    app.run()

if __name__ == '__main__':
    main()
   