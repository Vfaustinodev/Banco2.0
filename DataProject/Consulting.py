import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import os
import sqlite3

class ConsultingDates:

    PATH_FILE_DIR = os.path.dirname(__file__)

    try:
        connect = sqlite3.connect(PATH_FILE_DIR+'/users_registed.db')
        cursor = connect.cursor()

    except:
        print('NÃO FOI FEITA A CONEXÃO COM O BANCO DE DADOS')
        exit()

    def __init__(self):
          self.body_of_program()
          self.tree_view_form()
          self.buttons()
          self.center(self.root)
          self.root.mainloop()

    def tree_view_form(self):

        columns = (
    'ID', 'NAME', 'CONTACT', 'USER',
    'PASS', 'AGE', 'COUNTRY', 'BIRTH',
    'CPF', 'EMAIL', 'HOUR_REGISTED', 'GENDER', 
    'DATE_REGISTED'
    )
        
         #vertical bar
        self.scroolbar_view_y = tb.Scrollbar(self.frame_tree_view, style='round')
        self.scroolbar_view_y.pack(side='right', fill=Y)

        #horizontal bar
        self.scroolbar_view_x = tb.Scrollbar(self.frame_tree_view, orient='horizontal', style='round')
        self.scroolbar_view_x.pack(side='bottom', fill='x')
        
        self.table_view= tb.Treeview(
                    self.frame_tree_view, columns=columns, 
                    show='headings', style='success.Treeview', 
                    xscrollcommand=self.scroolbar_view_x.set,
                    yscrollcommand=self.scroolbar_view_y.set
        )
        self.table_view.pack(padx=0, pady=0)     

        #COnfig scrollbar X and Y
        self.scroolbar_view_x.config(command=self.table_view.xview)
        self.scroolbar_view_y.config(command=self.table_view.yview)   

        self.table_view.heading('ID', text='ID')
        self.table_view.heading('NAME', text='NOME')
        self.table_view.heading('CONTACT', text='CONTATO')
        self.table_view.heading('USER', text='USUARIO')
        self.table_view.heading('PASS', text='SENHA')
        self.table_view.heading('AGE', text='IDADE')
        self.table_view.heading('COUNTRY', text='PAÍS')
        self.table_view.heading('BIRTH', text='NASCIMENTO')
        self.table_view.heading('CPF', text='CPF')
        self.table_view.heading('EMAIL', text='EMAIL')
        self.table_view.heading('HOUR_REGISTED', text='HORA REGISTRO')
        self.table_view.heading('GENDER', text='GÊNERO')
        self.table_view.heading('DATE_REGISTED', text='DATA REGISTRO')

        self.table_view.column('ID', anchor='center', width=30)
        self.table_view.column('NAME', anchor='center')
        self.table_view.column('CONTACT', anchor='center')
        self.table_view.column('USER', anchor='center')
        self.table_view.column('PASS', anchor='center')
        self.table_view.column('AGE', anchor='center')
        self.table_view.column('COUNTRY', anchor='center')
        self.table_view.column('BIRTH', anchor='center')
        self.table_view.column('CPF', anchor='center')
        self.table_view.column('EMAIL', anchor='center')
        self.table_view.column('HOUR_REGISTED', anchor='center')
        self.table_view.column('GENDER', anchor='center')
        self.table_view.column('DATE_REGISTED', anchor='center')
        self.table_view.pack(fill='both', expand=True)

        self.consulting_table()

    def body_of_program(self):

        self.root = tb.Window(themename="cyborg")

        self.root.title('Consulta de Dados')

        self.root.geometry('850x550')
        self.root.iconbitmap(self.PATH_FILE_DIR+'\icons\login.ico')
        self.root.eval('tk::PlaceWindow . center')

        self.frame_tree_view=tb.Frame(self.root, bootstyle='darkly')
        self.frame_tree_view.pack(padx=20, pady=120, fill=BOTH, expand=YES)

    def consulting_table(self):

        self.cursor.execute(f'''SELECT * FROM tb_users_registed''')
        self.results_dates = self.cursor.fetchall()

        for lines_get in self.results_dates:
            contact=[
            lines_get[0], lines_get[1], lines_get[2], lines_get[3],
            lines_get[4], lines_get[5], lines_get[6], lines_get[7],
            lines_get[8], lines_get[9], lines_get[10], lines_get[11],
            lines_get[12]
            ]

            self.table_view.insert('', END, values=contact)
    
        self.connect.commit()

    def center(self, win):
            win.update_idletasks()

            width = win.winfo_width()
            frm_width = win.winfo_rootx() - win.winfo_x()
            win_width = width + 2 * frm_width

            height = win.winfo_height()
            titlebar_height = win.winfo_rooty() - win.winfo_y()
            win_height = height + titlebar_height + frm_width

            x = win.winfo_screenwidth() // 2 - win_width // 2
            y = win.winfo_screenheight() // 2 - win_height // 2

            win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

            win.deiconify()

    def buttons(self):
         
        delete_button = tb.Button(self.root, command=self.remove_all, style='danger.TButton.Outline', text='DELETAR TODOS', cursor='hand2')
        delete_button.place(x=270, y=40)

        delete_one_button = tb.Button(self.root, command=self.remove_one, style='danger.TButton.Outline', text='DELETAR', cursor='hand2')
        delete_one_button.place(x=20, y=40)

        delete_many_button = tb.Button(self.root, command=self.remove_many, style='danger.TButton.Outline', text='DELETAR SELECIONADOS', cursor='hand2')
        delete_many_button.place(x=100, y=40)

        save_commit = tb.Button(self.root, command=self.commit_save, style='success.TButton.Outline', text='SALVAR TUDO', cursor='hand2')
        save_commit.place(x=728, y=40)

        restore_button = tb.Button(self.root, command=self.restore_tree, style='success.TButton.Outline', text='DESFAZER', cursor='hand2')
        restore_button.place(x=635, y=40)
    
    def remove_all(self):

        self.cursor.execute(f'''DELETE FROM tb_users_registed;''')

        for record in self.table_view.get_children():
            self.table_view.delete(record)
    
    def remove_one(self):

        selected = self.table_view.focus()
        details = self.table_view.item(selected)
        capture_id = details.get("values")[0]
        
        self.cursor.execute(f'''DELETE FROM tb_users_registed WHERE id_user={capture_id};''')

        x = self.table_view.selection()[0]
        self.table_view.delete(x)

    def remove_many(self):

        selected = self.table_view.selection()
        for items in selected:
            current_item = self.table_view.item(items)
            capturar_ids = current_item.get("values")[0]

            self.cursor.execute(f'''DELETE FROM tb_users_registed WHERE id_user={capturar_ids};''')

        x = self.table_view.selection()

        for record in x:
            self.table_view.delete(record)

    def commit_save(self):
        self.connect.commit()
            
    def restore_tree(self):

        for delete_dates in self.table_view.get_children():
            self.table_view.delete(delete_dates)
            
        for lines_get in self.results_dates:
            contact=[
            lines_get[0], lines_get[1], lines_get[2], lines_get[3],
            lines_get[4], lines_get[5], lines_get[6], lines_get[7],
            lines_get[8], lines_get[9], lines_get[10], lines_get[11],
            lines_get[12]
            ]

            self.table_view.insert('', END, values=contact)

if __name__ == '__main__':
      ConsultingDates()