""" 
Voir cours-python dans LangagePython.zip,rechercher PYTHONPATH pour ajouter 
export PYTHONPATH=$PYTHONPATH:/home/mizael/Dev/Python/Anglais

test: be,have,do,get,stop,lie,try,read,lose,sleep,release,play

"""

import tkinter  
from tkinter import messagebox as msg
from include import Conjugaison as Conj
from src import Query as Q


def quit_app():
    reponse = msg.askyesno("Avertissement","Voulez-vous vraiment quitter ?")
    if reponse:
        app.quit()

def set_window(screen_x,screen_y):
    window_x = 542
    window_y = 540
    pos_x = (screen_x // 2) - (window_x // 2) #(largeur écran // 2) - (largeur fenêtre // 2)
    pos_y = (screen_y // 2) - (window_y // 2) #(hauteur écran // 2) - (hauteur fenêtre // 2) 
    geo = "{}x{}+{}+{}".format(window_x,window_y,pos_x,pos_y)
    return geo

def get_form(verb): 
    if Default_form.get() == "Affirmative":
        return Conj.Affirmative(verb)
    elif Default_form.get() == "Negative":
        return Conj.Negative(verb)
    elif Default_form.get() == "Interrogative":
        return Conj.Interrogative(verb)
    else:
        return Conj.InterroNegative(verb)       
        
def get_tence(verb):
    my_verb = get_form(verb)
    if Default_tence.get() == "present simple":
        return my_verb.present_simple()
    elif Default_tence.get() == "present continuous":
        return my_verb.present_progressive()
    elif Default_tence.get() == "present perfect":
        return my_verb.present_perfect()
    if Default_tence.get() == "past simple":
        return my_verb.past_simple()
    elif Default_tence.get() == "past continuous":
        return my_verb.past_progressive()
    elif Default_tence.get() == "past perfect":
        return my_verb.past_perfect()
    elif Default_tence.get() == "present conditionnal":
        return my_verb.present_conditional()
    elif Default_tence.get() == "past conditionnal":
        return my_verb.past_conditional()
    else:
        return my_verb.future()

def get_verb():
    return str(var_entry.get())

def set_labelframe(parent,variable):
    return tkinter.LabelFrame(parent,text=variable,font=("Consolas",10,"bold"),fg="#FA0",bg="#222",borderwidth=0)

def set_listbox(verb):
    var_combined = "\t" + str(Default_form.get()) + "\n\t" + str(Default_tence.get())
    my_labelframe = set_labelframe(My_canvas,var_combined)
    my_listbox = tkinter.Listbox(my_labelframe,width=30,bg="#222",fg="#FFF",borderwidth=0)
    for i in range(len(verb)):
        my_listbox.insert(i,verb[i])
    my_listbox.grid(padx=2,pady=10) 
    my_labelframe.pack(side="left",padx=10,pady=10) 
    
def delete_conjugate():
    if len(My_canvas.winfo_children()) < 2:
        return 
    else:
        widget = My_canvas.winfo_children()
        widget[0].destroy()

    
def conjugate(*args):
    if get_verb() == "":
        msg.showinfo("Infos","Veuillez entrer un verbe !")
    elif Q.is_verb(get_verb()) == False:
        msg.showerror("Erreur de saisie","Ce verbe n'existe pas")
    elif Default_form.get() == "Form"and Default_tence.get() == "Tence":
        msg.showwarning("Attention","Veuillez choisir la forme et le temps du verbe à conjuguer!")
    elif Default_form.get() == "Form":
        msg.showwarning("Attention","Veuillez choisir la forme du verbe à conjuguer!")
    elif Default_tence.get() == "Tence":
        msg.showwarning("Attention","Veuillez choisir le temps du verbe à conjuguer!")
    else:
        delete_conjugate()
        set_listbox(get_tence(get_verb()))
          
def delete_translate():
    widget = My_frame.winfo_children()
    if len(widget) > 6:
        widget[len(widget) - 1].destroy()

def get_traduction():
    if Q.is_in("regularverbs",get_verb()) != None:
        return Q.is_in("regularverbs",get_verb())
    return Q.is_in("irregularverbs",get_verb())

def translate(*args):
    if get_verb() == "":
        msg.showinfo("Infos","Veuillez entrer un verbe !")
    elif Q.is_verb(get_verb()) == False:
        msg.showerror("Erreur de saisie","Ce verbe n'existe pas")
    else:
        delete_translate()
        my_labelframe = set_labelframe(My_frame," Traduction ")
        var_combined = str(var_entry.get()) + ":" + " " + get_traduction()
        my_label = tkinter.Label(my_labelframe,text=var_combined,bg="#222",fg="#FFF")
        my_label.grid(padx=10,pady=10)
        my_labelframe.grid(row=4,columnspan=2,column=2,pady=5)
    



app = tkinter.Tk()
app.title("English Apps")
app.geometry(set_window(int(app.winfo_screenwidth()),int(app.winfo_screenheight())))
app.resizable(width=False,height=False)
app["background"] = "#777"

My_frame = tkinter.LabelFrame(app,borderwidth=3,relief="sunken",text="Menu",font=("Consolas",20,"bold"))
My_frame["bg"] = "#555"
My_frame["fg"] = "#0AF"
My_frame.pack(fill="both",padx=5,ipadx="1c")

Text_label = tkinter.Label(My_frame,text=" To ")
Text_label.grid(row=1,columnspan=2,column=2)

var_entry = tkinter.StringVar()
Entry_verb = tkinter.Entry(My_frame,textvariable=var_entry,relief="solid")
Entry_verb.grid(row=2,columnspan=2,column=2)


Conjugate_button = tkinter.Button(My_frame,text="Conjuguer !",activebackground="#0AF",bg="#444",fg="#FFF",command=conjugate)
Conjugate_button["borderwidth"] = 2
Conjugate_button.grid(row=3,pady=10,column=2)

Translate_button = tkinter.Button(My_frame,text="Traduire !",activebackground="#0AF",bg="#444",fg="#FFF",command=translate)
Translate_button["borderwidth"] = 2
Translate_button.grid(row=3,column=3)

Default_form = tkinter.StringVar()
Default_form.set("Form")
Item_form = ["Affirmative",
            "Negative",
            "Interrogative",
            "Interro-negative"]
Form = tkinter.OptionMenu(My_frame,Default_form,*Item_form)
Form["width"] = 15
Form["textvariable"] = Default_form
Form["bg"] = "#444"
Form["fg"] = "#FA0"
Form["activebackground"] = "#FA0"
Form["menu"]["activebackground"] = "#FA0"
Form["menu"]["background"] ="#444"
Form["borderwidth"] = 0
Form.grid(row=1,column=1,rowspan=2)

Default_tence = tkinter.StringVar()
Default_tence.set("Tence")
Item_tence = ["present simple",
            "present continuous",
            "present perfect",
            "past simple",
            "past continuous",
            "past perfect",
            "present conditionnal",
            "past conditionnal",
            "futur"]
Tence = tkinter.OptionMenu(My_frame,Default_tence,*Item_tence)
Tence["width"] = 15
Tence["textvariable"] = Default_tence
Tence["bg"] = "#444"
Tence["fg"] = "#FA0"
Tence["activebackground"] = "#FA0"
Tence["menu"]["activebackground"] ="#FA0"
Tence["menu"]["background"] ="#444"
Tence["borderwidth"] = 0
Tence.grid(row=1,column=4,rowspan=2)

Quit_button = tkinter.Button(app,text="Quitter",fg="#0AF",bg="#444",command=quit_app,font=("Helvetica",12,"bold"),width=10,height=2)
Quit_button["borderwidth"] = 0
Quit_button.pack(side="bottom",pady=5)

My_canvas = tkinter.Canvas(app,bg="#AAA",relief="groove",borderwidth=0)
My_canvas["bg"] = "#555"
My_canvas.pack(fill="both",padx=5,pady=5,expand=True)


app.mainloop()
