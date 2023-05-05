from business.service_studenti import ServiceStudenti
from domain.student import Student
from infrastructura.repo_studenti import RepoStudenti


class Teste:
    def __init__(self,repo_studenti,repo_laboratoare,repo_note,service_laboratoare,service_studenti,service_note):
        self.__repo_studenti=repo_studenti
        self.__repo_note=repo_note
        self.__repo_laboratoare = repo_laboratoare
        self.__service_studenti=service_studenti
    def __ruleaza_teste_domain(self):
        """
        Testeaza functiile din domeniu
        :return:-
        """
        id_student=123
        nume="Anca"
        grupa=211
        student=Student(id_student,nume,grupa)
        assert(student.get_id_student()==id_student)
        assert(student.get_nume_student()==nume)
        assert(student.get_grupa_student()==grupa)
        nume_nou="Andreea"
        student.set_nume_student(nume_nou)
        assert (student.get_nume_student() == nume_nou)
        grupa_noua=512
        student.set_grupa_student(grupa_noua)
        assert (student.get_grupa_student() == grupa_noua)

    def __ruleaza_teste_repository(self):
        """
            Testeaza functiile din repository
            :return:-
        """
        studenti=[]
        id_student = 123
        nume = "Anca"
        grupa = 211
        student = Student(id_student, nume, grupa)
        studenti = self.__repo_studenti.get_all()
        assert(self.__repo_studenti.numar_studenti()==0)
        self.__repo_studenti.adauga_student(student)
        studenti=self.__repo_studenti.get_all()
        assert(self.__repo_studenti.numar_studenti()==1)
        assert(studenti[0]==student)

        id_student = 178
        nume = "Ana"
        grupa = 213
        student = Student(id_student, nume, grupa)
        self.__repo_studenti.adauga_student(student)
        studenti = self.__repo_studenti.get_all()
        assert (self.__repo_studenti.numar_studenti() == 2)
        assert (studenti[1] == student)

        self.__repo_studenti.sterge_student_dupa_id(123)
        studenti = self.__repo_studenti.get_all()
        assert (self.__repo_studenti.numar_studenti() == 1)
        assert (studenti[0] == student)

        student_cautat=self.__repo_studenti.cauta_student_dupa_id(178)
        assert(student_cautat==student)
        nume_modificat="Miruna"
        grupa_modificata=512
        student_modificat=Student(id_student,nume_modificat,grupa_modificata)
        self.__repo_studenti.modifica_student(student_modificat)
        studenti = self.__repo_studenti.get_all()
        assert(studenti[0]==student_modificat)
    def __ruleaza_teste_service(self):
        """
            Testeaza functiile din service
            :return:-
        """
        self.__repo_studenti.golire_lista_repo()
        studenti=[]
        id_student = 125
        nume = "Anca"
        grupa = 211
        student = Student(id_student, nume, grupa)
        studenti=self.__service_studenti.get_all_service()
        assert (self.__service_studenti.numar_studenti_service() == 0)
        self.__service_studenti.adauga_student(id_student,nume,grupa)
        studenti = self.__service_studenti.get_all_service()
        assert (self.__service_studenti.numar_studenti_service() == 1)
        self.__service_studenti.sterge_student_dupa_id_service(id_student)
        assert (self.__service_studenti.numar_studenti_service() == 0)
        assert(studenti==[])
       # self.__service_studenti.modifica_student_dupa_id_service(id_student)
        self.__repo_studenti.golire_lista_repo()
    def ruleaza_toate_testele(self):
        self.__ruleaza_teste_domain()
        print("teste domain rulate cu succes!")
        self.__ruleaza_teste_repository()
        print("teste repository rulate cu succes!")
        self.__ruleaza_teste_service()
        print("teste service rulate cu succes!")


