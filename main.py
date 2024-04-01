from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from calc.matrix_operations import *

class page(Frame):
    pass

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Linear Algebra ToolKit") 
        self.geometry("1000x800")
        self.config(bg='#202020')
        self.run_operation = None
        self.operations = {
            "t":  {"v": "Transpose", "is": False, "need_square": False, "function": transpose},
            "d":  {"v": "Determinant", "is": False, "need_square": True, "function": determinant},
            "i":  {"v": "Inverse", "is": False, "need_square": True, "function": inverse},
            "r":  {"v": "REF", "is": False, "need_square": False, "function": row_echelon},
            "rr": {"v": "RREF", "is": False, "need_square": False, "function": reduced_row_echelon},
            "rk": {"v": "Rank", "is": False, "need_square": False, "function": rank},
            "e":  {"v": "Eigenvalue", "is": False, "need_square": True, "function": eigenvalues},
            "lu": {"v": "LU Decomposition", "is": False, "need_square": False, "function": lu_demonpisition},
            "p":  {"v": "AX=b", "is": False, "need_square": False, "function": solve_problem}   
        }
        self.main_page()
    
    def check_operation(self, operation):
        self.operations[operation]["is"] = True
        return

    def main_page(self):
        title_label = Label(self, text="Operations", 
                    font=("Helvetica", 15, "bold"), width=60, height=1,
                    bg="light grey", fg="black")
        title_label.place(relx=0.5, rely=0.043, anchor=CENTER)
        #tranpose option
        self.transpose_button = Button(self, text="Tranpose", width=25, height=3, 
                                       command=lambda: (self.check_operation("t"), self.matrix_setup()),
                                       font=("Helvetica", 12, "bold"),
                                       bg="grey", fg="black")
        self.transpose_button.place(relx=0.5, rely=0.13, anchor=CENTER)
        #determinent option
        self.determinant_button = Button(self, text="Determinant", width=25, height=3, 
                                         command=lambda: (self.check_operation("d"), self.matrix_setup()), 
                                         font=("Helvetica", 12, "bold"),
                                         bg="grey", fg="black")
        self.determinant_button.place(relx=0.5, rely=0.23, anchor=CENTER)
        #inverse option
        self.inverse_button = Button(self, text="Inverse", 
                                     command=lambda: (self.check_operation("i"), self.matrix_setup()), 
                                     width=25, height=3, 
                                     font=("Helvetica", 12, "bold"),
                                     bg="grey", fg="black")
        self.inverse_button.place(relx=0.5, rely=0.33, anchor=CENTER)
        #ref option
        self.ref_button = Button(self, text="Row Echelon", 
                                 command=lambda: (self.check_operation("r"), self.matrix_setup()), 
                                 width=25, height=3, 
                                 font=("Helvetica", 12, "bold"),
                                 bg="grey", fg="black")
        self.ref_button.place(relx=0.5, rely=0.43, anchor=CENTER)
        #rref option
        self.rref_button = Button(self, text="Reduced Row Echelon", 
                                  command=lambda: (self.check_operation("rr"), self.matrix_setup()), 
                                  width=25, height=3, 
                                  font=("Helvetica", 12, "bold"),
                                  bg="grey", fg="black")
        self.rref_button.place(relx=0.5, rely=0.53, anchor=CENTER)
        #rank option
        self.rank_button = Button(self, text="Rank", 
                                  command=lambda: (self.check_operation("rk"), self.matrix_setup()),
                                  width=25, height=3, 
                                  font=("Helvetica", 12, "bold"),
                                  bg="grey", fg="black")
        self.rank_button.place(relx=0.5, rely=0.63, anchor=CENTER)
        #eigen
        self.rank_button = Button(self, text="Eigenvalue", 
                                  command=lambda: (self.check_operation("e"), self.matrix_setup()),
                                  width=25, height=3, 
                                  font=("Helvetica", 12, "bold"),
                                  bg="grey", fg="black")
        self.rank_button.place(relx=0.5, rely=0.73, anchor=CENTER)
        #lu option
        self.lu_button = Button(self, text="LU Decompisition", 
                                command=lambda: (self.check_operation("lu"), self.matrix_setup()),
                                width=25, height=3, 
                                font=("Helvetica", 12, "bold"),
                                bg="grey", fg="black")
        self.lu_button.place(relx=0.5, rely=0.83, anchor=CENTER)
        #AX=b option
        self.problem_button = Button(self, text="AX = b", 
                                     command=lambda: (self.check_operation("p"), self.matrix_setup()),
                                     width=25, height=3, 
                                     font=("Helvetica", 12, "bold"),
                                     bg="grey", fg="black")
        self.problem_button.place(relx=0.5, rely=0.93, anchor=CENTER)

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
        
    def back_option(self):
        self.back_button = Button(self, text="Menu",
                                  command=lambda: (self.back_button.destroy(), 
                                  setattr(self, "run_operation", None), 
                                  self.clear_screen(), self.main_page()),
                                  width=4, height=1,
                                  font=("Helvetica", 10, "bold"),
                                  bg="black", fg="white")
        self.back_button.place(relx=1, rely=0, anchor=NE)
        

    def matrix_setup(self):
        self.clear_screen()
        self.back_option()
        #title
        title_label = Label(self, text="Enter the size of row and column of the matrix!", 
                            font=("Helvetica", 20, "bold"), width=55, height=2,
                            bg="light grey", fg="black")
        title_label.place(relx=0.5, rely=0.25, anchor=CENTER)
        #row
        row_label = Label(self, text="Number of Rows:", font=("Helvetica", 14, "bold"),
                          width=20, height=1, bg="light grey", fg="black")
        row_label .place(relx=0.35, rely=0.4, anchor=CENTER)
        self.entry_m = Entry(self, width=18, font=("Helvetica", 14, "bold"),
                             bg="grey", fg="black", highlightbackground="black", highlightcolor="grey")
        self.entry_m.place(relx=0.65, rely=0.4, anchor=CENTER)
        #col
        col_label = Label(self, text="Number of Columns:", font=("Helvetica", 14, "bold"),
                          width=20, height=1, bg="light grey", fg="black")
        col_label.place(relx=0.35, rely=0.5, anchor=CENTER)
        self.entry_n = Entry(self, width=18, font=("Helvetica", 14, "bold"),
                             bg="grey", fg="black", highlightbackground="black", highlightcolor="grey")
        self.entry_n.place(relx=0.65, rely=0.5, anchor=CENTER)
        #submit 
        submit_button = Button(self, text="Submit", command=self.create_matrix,
                               font=("Helvetica", 14, "bold"),
                               width=25, height=2, bg="grey", fg="black")
        submit_button.place(relx=0.5, rely=0.7, anchor=CENTER)

    def create_matrix(self):
        #check for integer
        try:
            row = int(self.entry_m.get())
            col = int(self.entry_n.get())
        except ValueError:
            messagebox.showerror("ERROR!", "Please Enter an Integer!", parent=self)
            return
        #not to create an 0 matrix
        if (row == 0) and (col == 0):
            messagebox.showerror("ERROR!", "Please Enter a Valid Input!", parent=self)
            return
        #checks which operaiton to run
        for operation, value in self.operations.items():
            if value["is"]:
                self.run_operation = value
                value["is"] = False
                break
        #check if square is needed
        if self.run_operation["need_square"]:
            if (row != col):
                messagebox.showerror("ERROR!", "Number of Rows and Columns Needs To Be The Same!", parent=self)
                return
        #create a "new page"
        self.clear_screen()
        matrix_frame = Frame(self, bg="#202020")
        matrix_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.back_option()

        title_label = Label(matrix_frame, text=self.run_operation["v"], 
                    font=("Helvetica", 18, "bold"), width=60, height=1,
                    bg="light grey", fg="black")
        title_label.place(relx=0.5, rely=0.023, anchor=CENTER)

        self.prob_con = 0
        ver = 0.4 - col/35
        if ver < 0:
            ver = 0
        extra_entry = []
        if self.run_operation["v"] == "AX=b":
            if col >= 6:
                self.prob_con = 0.1

            label_a = Label(matrix_frame, text="A", width=5*(row), height=1,
                            font=("Helvetica", 12, "bold"), 
                            bg="light grey", fg="black", anchor="center")
            label_a.place(relx=(0.51-self.prob_con)-row/30, rely=0.35-col/35)
            label_b = Label(matrix_frame, text="B", width=4, height=1,
                            font=("Helvetica", 12, "bold"), 
                            bg="light grey", fg="black", anchor="center")
            label_b.place(relx=0.885, rely=0.35-col/35)

            for i in range(row):
                entry = Entry(matrix_frame, width=5, font=("Helvetica", 12, "bold"),
                              bg="grey", fg="black", highlightcolor="grey")
                entry.place(relx=0.88, rely=ver)
                extra_entry.append(entry)
                ver = ver+0.05
        
        ver = 0.4 - col/35
        if ver < 0:
            ver = 0
        entry_matrix = []
        for i in range(row):
            hor = (0.5-self.prob_con) - row/30
            if hor < 0:
                hor = 0
            row_entries = []
            for j in range(col):
                entry = Entry(matrix_frame, width=5, font=("Helvetica", 12, "bold"),
                             bg="grey", fg="black", highlightcolor="grey")
                entry.place(relx=hor, rely=ver)
                row_entries.append(entry)
                hor = hor+0.07
            entry_matrix.append(row_entries)
            ver = ver+0.05 

        self.submit_button = Button(self, text="Submit", font=("Helvetica", 14, "bold"), 
                                    command=lambda:(self.collect_matrix(entry_matrix, extra_entry), 
                                    self.print_result()), width=20, height=2, bg="grey", fg="black")
        self.submit_button.place(relx=0.5, rely=0.8, anchor=CENTER)
    
    def collect_matrix(self, entry, extra_entry):
        #collect/checks each element with a number
        matrix_values = []
        for row_elements in entry:
            row_values = []
            for element in row_elements:
                value = element.get()
                if not value:
                    value = 0
                try:
                    row_values.append(float(value))
                except ValueError:
                    messagebox.showerror("ERROR!", "Please Enter a number", parent=self)
                    return
            matrix_values.append(row_values)
        self.matrix = Matrix(matrix_values)

        if len(extra_entry) != 0:
            self.b_vector = []
            for element in extra_entry:
                value = element.get()
                if not value:
                    value = 0
                try:
                    self.b_vector.append(float(value))
                except ValueError:
                    messagebox.showerror("ERROR!", "Please Enter a number", parent=self)
                    return

    def print_result(self):
        self.clear_screen()
        #top section
        question_frame = Frame(self, bd=2, relief="solid", bg="#202020")
        question_frame.place(relx=0, rely=0, relwidth=1, relheight=0.5)
        question_label = Label(question_frame, font=("Helvetica", 14, "bold"), 
                               text="INPUT (" + self.run_operation["v"] + "): ",
                               width=77, height=1, bg="light grey", 
                               fg="black", anchor="w")
        question_label.place(relx=0.5, rely=0.03, anchor=CENTER)
        self.back_option()
        #buttom section
        answer_frame = Frame(self, bd=2, relief="solid", bg="#202020")
        answer_frame.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)        
        answer_label = Label(answer_frame, text="ANSWER: ", 
                             font=("Helvetica", 14, "bold"), 
                             width=77, height=1, bg="light grey", 
                             fg="black", anchor="w")
        answer_label.place(relx=0.5, rely=0.03, anchor="center")

        if self.run_operation["v"] == "AX=b":
            hori = (0.5-self.prob_con) - self.matrix.col/30
            label_a = Label(question_frame, text="A", width=5*(self.matrix.row), height=1,
                            font=("Helvetica", 12, "bold"), 
                            bg="grey", fg="black", anchor="center")
            label_a.place(relx=(0.51-self.prob_con)-self.matrix.row/30, rely=0.21-self.matrix.col/35)
            label_b = Label(question_frame, text="B", width=4, height=1,
                            font=("Helvetica", 12, "bold"), 
                            bg="grey", fg="black", anchor="center")
            label_b.place(relx=0.893, rely=0.21-self.matrix.col/35)
            self.display_matrix(question_frame, self.matrix, hori)
            y = 0.3 - self.matrix.row/35
            if y < 0.07:
                y = 0.07
            for i in range(len(self.b_vector)):
                label = Label(question_frame, text=str(round(self.b_vector[i], 3)), 
                              width=6, height=2, bd=5, relief="solid",
                              font=("Helvetica", 10, "bold"))
                label.place(relx=0.885, rely=y)
                y = y+0.123

            result = self.run_operation["function"](self.matrix, self.b_vector)
            hori = 0.5 - result.col/30
            self.display_matrix(answer_frame, result, hori)
            return


        hori = 0.5 - self.matrix.col/30
        self.display_matrix(question_frame, self.matrix, hori)

        if self.run_operation["v"] == "LU Decomposition":
            lower, upper = self.run_operation["function"](self.matrix)
            if lower == -9:
                messagebox.showerror("ERROR!", "Enter a Valid Matrix!", parent=self)
                self.matrix_setup()
                return

            hori = 0.25 - lower.col/30
            self.display_matrix(answer_frame, lower, hori)
            hori = 0.7 - upper.col/30
            self.display_matrix(answer_frame, upper, hori)
            return

        result = self.run_operation["function"](self.matrix)
        hori = 0.5 - result.col/30
        self.display_matrix(answer_frame, result, hori)

    
    def display_matrix(self, frame, matrix, x):
        if x < 0:
            x = 0
        for j in range(matrix.col):
            y = 0.3 - matrix.row/35
            if y < 0.07:
                y = 0.07
            for i in range(matrix.row):
                label = Label(frame, text=str(round(matrix.elements[i][j], 3)), 
                              width=6, height=2, bd=5, relief="solid",
                              font=("Helvetica", 10, "bold"))
                label.place(relx=x, rely=y)
                y = y+0.123
            x = x+0.07

if __name__ == "__main__":
    app = App()
    app.mainloop()