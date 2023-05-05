from erori.validation_error import ValidationError
from erori.repo_error import RepoError
class UI():
    def __init__(self,service_studenti,service_laboratoare,service_note):
        self.__service_studenti=service_studenti
        self.__service_note=service_note
        self.__service_laboratoare=service_laboratoare
        self.__comenzi={
            "adauga_student":self.__ui_adauga_student,
            "print_studenti":self.__ui_print_studenti,
            "sterge_student":self.__ui_sterge_student_dupa_id,
            "modifica_student":self.__ui_modifica_student_dupa_id,
            "cauta_student":self.__ui_cauta_student,
            "help":self.__printeaza_meniu

        }
    def __printeaza_meniu(self):
        for key in self.__comenzi:
            print(key)
    def __ui_cauta_student(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        id_student=int(self.__params[0])
        student_cautat=self.__service_studenti.cauta_student_dupa_id_service(id_student)
        print(f"Studentul cautat este {student_cautat}!")
    def __ui_modifica_student_dupa_id(self):
        if len(self.__params) != 3:
            print("numar parametrii invalid!")
            return
        id_student = int(self.__params[0])
        nume = self.__params[1]
        grupa = int(self.__params[2])
        self.__service_studenti.modifica_student_dupa_id_service(id_student,nume,grupa)
        print("student modificat cu succes!")

    def __ui_print_studenti(self):
        if len(self.__params)!=0:
            print("numar parametrii invalid!")
            return
        studenti=self.__service_studenti.get_all_service()
        if len(studenti)==0:
            print("nu exista studenti in aplicatie!")
            return
        for student in studenti:
            print(student)



    def __ui_adauga_student(self):
         if len(self.__params)!=3:
             print("numar parametrii invalid!")
             return
         id_student=int(self.__params[0])
         nume=self.__params[1]
         grupa=int(self.__params[2])
         self.__service_studenti.adauga_student(id_student,nume,grupa)
         print("student adaugat cu succes!")

    def __ui_sterge_student_dupa_id(self):
        if len(self.__params)!=1:
            print("numar parametrii invalid!")
            return
        id_sters=int(self.__params[0])
        self.__service_studenti.sterge_student_dupa_id_service(id_sters)
        print("student sters cu succes!")

    def run(self):
        while True:
            comanda=input(">>>")
            comanda=comanda.strip()
            if comanda=="":
                continue
            if comanda=="exit":
                return
            parti=comanda.split()
            nume_comanda=parti[0]
            self.__params=parti[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError:
                    print("eroare UI:tip numeric invalid!")
                except ValidationError as ve:
                    print(f"Validation Error:{ve}")
                except RepoError as re:
                    print(f"Repo Error:{re}")
            else:
                print("comanda invalida!")



