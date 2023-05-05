from erori.repo_error import RepoError


class RepoStudenti:
    def __init__(self):
       self.__studenti=[]

    def adauga_student(self,student):
        """
        adauga studentul student la lista studentilor
        :param student: Student
        :return: -
        """
        for _student in self.__studenti:
            if _student.get_id_student()==student.get_id_student():
                raise RepoError("student existent!")
        self.__studenti.append(student)
    def sterge_student_dupa_id(self,id_student):
        """
        Sterge studentul cu id-ul id_student
        :param id_student: integer
        :return: -
        """
        ok=0
        contor=0
        for _student in self.__studenti:
            contor+=1
            if _student.get_id_student() ==id_student:
                ok=1
                numar_student_in_lista=contor
        if ok==0:
             raise RepoError("student inexistent!")
        del self.__studenti[numar_student_in_lista-1]
    def cauta_student_dupa_id(self,id_student):
        """
        Cauta studentul cu id-ul id_student,iar daca nu il gaseste semnaleaza erori
        :param id_student: integer
        :return: studnetul cautat sau semnaleaza erori
        """
        ok = 0
        contor=0
        for _student in self.__studenti:
            contor+=1
            if _student.get_id_student() == id_student:
                ok = 1
                numar_student_in_lista=contor
        if ok == 0:
            raise RepoError("student inexistent!")
        return self.__studenti[numar_student_in_lista-1]
    def modifica_student(self,student):
        """
        Modifica studentul cu id-ul studentului student, inlocuindu-l cu student
        :param student: Student,class
        :return: -
        """
        ok = 0
        contor=0
        for _student in self.__studenti:
            contor+=1
            if _student.get_id_student() == student.get_id_student():
                ok = 1
                numar_student_in_litsa=contor
        if ok == 0:
            raise RepoError("student inexistent!")
        self.__studenti[numar_student_in_litsa-1]=student

    def get_all(self):
        """

        :return:lista de studenti unic identificabili prin id
        """
        return self.__studenti
    def numar_studenti(self):
        """

        :return:numarul de studenti din lista de studenti
        """
        return len(self.__studenti)
    def golire_lista_repo(self):
        """
        Reface lista de studenti, pentru a nu ramane studenti adaugati in functia de testare
        :return:-
        """
        self.__studenti=[]

