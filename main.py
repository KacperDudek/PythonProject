"""
All important imports, which are needed for running program properly
"""
import csv
import os
import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox


class GUI(Frame):
    """
    Creating class, which is base of GUI
    """

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        """
        Defining method where everything will be implemented
        :return:
        """

        fileExist = os.path.isfile('People.csv')
        header = ['NAME:', 'SURNAME:', 'AGE:']
        addon = []

        def clearAction():
            """
            Implementing button action which clears all text boxes.
            """
            area1.delete(0, 'end')
            area2.delete(0, 'end')
            area3.delete(0, 'end')

        def quitAction():
            """
            Implementing button action which disposes a program.
            """
            quit()

        def helpAction():
            """
            Implementing button action which displays message window with describes all buttons
            """
            tkinter.messagebox.showinfo('Help', 'Add button: Adds person from text areas\n'
                                                'Clear button: Clears entry boxes\n'
                                                'Quit button: Aborts program\n'
                                                'Show info button: Displays file. Enables after adding person. '
                                                'Disables after clicking')

        def addAction():
            """
            Implementing button action which allows us to create and add person
            from text boxes to a .csv file
            :return:
            """
            displayBtn['state'] = NORMAL

            class Data:
                """
                Implementing bridge design pattern.
                It will display headers preceding information from text boxes
                in messagebox to avoid any mistakes.
                """

                @staticmethod
                def takeName():
                    """
                    Header preceding information from first text box
                    :return:
                    """
                    return 'Name: '

                @staticmethod
                def takeSurname():
                    """
                    Header preceding information from second text box
                    :return:
                    """
                    return 'Surname: '

                @staticmethod
                def takeAge():
                    """
                    Header preceding information from third text box
                    :return:
                    """
                    return 'Age: '

            class Check:
                """
                Impossible to implement bridge pattern without this constructor in this way
                """

                def __init__(self, bridgePerson):
                    self.bridgePerson = bridgePerson

            class Product:
                """
                Similarly to bridge, builder could not be implemented without this
                """

                def __init__(self, buildPerson):
                    self.buildPerson = buildPerson

            class infoA(Check):
                """
                Creating class for output for user
                """

                def __init__(self, bridgePerson, objName, objSurname, objAge):
                    super().__init__(bridgePerson)

                    self.objName = objName
                    self.objSurname = objSurname
                    self.objAge = objAge

                def displayName(self):
                    """
                    Function which allows us to see header preceding
                    first information from text box in messagebox
                    """
                    self.bridgePerson.takeName(self.objName)

                def displaySurname(self):
                    """
                    Function which allows us to see header preceding
                    second information from text box in messagebox
                    """

                    self.bridgePerson.takeSurname(self.objSurname)

                def displayAge(self):
                    """
                    Function which allows us to see header preceding
                    third information from text box in messagebox
                    """
                    self.bridgePerson.takeAge(self.objAge)

            class infoB(Product):
                """
                Creating class which will allow us to build person
                and add it to .csv file by addAction
                """

                def __init__(self, buildPerson, bName, bSurname, bAge):
                    super().__init__(buildPerson)

                    self.bName = bName
                    self.bSurname = bSurname
                    self.bAge = bAge

                def buildName(self):
                    """
                    Function which builds name
                    :return:
                    """
                    self.bName = area1
                    return self.bName

                def buildSurname(self):
                    """
                    Function which builds surname
                    :return:
                    """
                    self.bSurname = area2
                    return self.bSurname

                def buildAge(self):
                    """
                    Function which builds age
                    :return:
                    """
                    self.bAge = area3
                    return self.bAge

            data = Data()

            personInformation = infoA(Data, area1, area2, area3)
            infoBuild = infoB(Data, area1, area2, area3)

            addon.append(infoBuild.buildName().get())
            addon.append(infoBuild.buildSurname().get())
            addon.append(infoBuild.buildAge().get())

            personInformation.displayName = data.takeName()
            personInformation.displaySurname = data.takeSurname()
            personInformation.displayAge = data.takeAge()

            answer = tkinter.messagebox.askyesno('Confirmation', 'Do you really want to add this person?\n' +

                                                 str(personInformation.displayName) + str(area1.get()) + '\n' +
                                                 str(personInformation.displaySurname) + str(area2.get()) + '\n' +
                                                 str(personInformation.displayAge) + str(area3.get()))

            if answer is True:
                with open('People.csv', 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    if not fileExist:
                        writer.writerow(header)

                    writer.writerow(addon)
                    csvfile.close()
                    addon.clear()
                    area1.delete(0, 'end')
                    area2.delete(0, 'end')
                    area3.delete(0, 'end')

            else:
                addon.clear()

        def displayAction():
            """
            Implementing button action which displays written .csv file with informations
            :return:
            """

            class Singleton(object):
                """
                Creating Singleton
                """
                _instance = None

                def __init__(self):
                    raise RuntimeError('Call instance() instead')

                @classmethod
                def instance(cls):
                    """
                    Creating function which is instance of singleton
                    :return:
                    """
                    if cls._instance is None:
                        print('Creating new instance')
                        cls._instance = cls.__new__(cls)

                    return cls._instance

            s1 = Singleton.instance()
            s2 = Singleton.instance()


            """
            Implementing window after reading file
            """
            if s1 == s2:

                displayBtn['state'] = DISABLED
                window = tkinter.Toplevel()
                window.geometry('350x720')
                window.title('Student informations')

                scr = tkinter.Scrollbar(master=window)
                txt = tkinter.Text(master=window, height=50, width=50)
                scr.pack(side=tkinter.RIGHT, fill=tkinter.Y)
                txt.pack(side=tkinter.LEFT, fill=tkinter.Y)
                scr.config(command=txt.yview)
                txt.config(yscrollcommand=scr.set)

                with open('People.csv', 'r', newline='') as csvfile:
                    reader = csv.reader(csvfile, quotechar='|')
                    for row in reader:
                        txt.insert(tkinter.INSERT, '\t\t|'.join(row).strip() + '\n')

            else:
                tkinter.messagebox.showerror('Already open', 'This database has been already opened')


        """
        Implementing core window. 
        """
        self.master.title('Add student')
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3)
        self.rowconfigure(5, pad=5)

        lbl = Label(self, text='Student:')
        lbl.grid(sticky='w', pady=4, padx=5)

        lbl = Label(self, text='Name:')
        lbl.grid(sticky='w', pady=4, padx=5)

        area1 = Entry(self)
        area1.grid(row=2, column=0, columnspan=2, rowspan=1, padx=5, sticky='new')

        lbl = Label(self, text='Surname:')
        lbl.grid(sticky='nw', pady=4, padx=5)

        area2 = Entry(self)
        area2.grid(row=3, column=0, columnspan=2, rowspan=1, padx=5, sticky='new', pady=26)

        lbl = Label(self, text='Age:')
        lbl.grid(row=3, sticky='nw', pady=65, padx=5)

        area3 = Entry(self)
        area3.grid(row=3, column=0, columnspan=2, rowspan=1, padx=5, sticky='new', pady=85)

        separator = Separator(self, orient=VERTICAL)
        separator.grid(column=3, row=0, rowspan=8, sticky='ns')

        addBtn = Button(self, text='Add', command=addAction)

        addBtn.grid(row=1, column=4, pady=4, padx=5)

        clearBtn = Button(self, text='Clear', command=clearAction)
        clearBtn.grid(row=2, column=4, pady=4, padx=5)

        helpBtn = Button(self, text='Help', command=helpAction)
        helpBtn.grid(row=4, column=0, padx=5)

        quitBtn = Button(self, text='Quit', command=quitAction)
        quitBtn.grid(row=4, column=4, padx=5)

        displayBtn = Button(self, text='Show info', command=displayAction)
        displayBtn['state'] = DISABLED
        displayBtn.grid(row=3, column=4, padx=5)


def main():
    """
    Creating main function which will display whole window
    and will have all implemented before methods
    """
    root = Tk()
    root.geometry('350x310+300+300')
    root = GUI()
    root.mainloop()


if __name__ == '__main__':
    main()
