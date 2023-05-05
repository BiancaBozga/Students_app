from domain.student import Student
class ServiceStudenti:

    def __init__(self,validator_student,repo_studenti):
        self.__validator_student=validator_student
        self.__repo_studenti=repo_studenti

    def adauga_student(self,id_student,nume,grupa):
        """
        Adauga studnetul cu id_ul id_student, numele nume si grupa grupa
        :param id_student:integer
        :param nume: string
        :param grupa: integer
        :return: -
        """
        student=Student(id_student,nume,grupa)
        self.__validator_student.valideaza_student(student)
        self.__repo_studenti.adauga_student(student)
    def sterge_student_dupa_id_service(self,id_student):
        """
        Sterge studnetul cu id_ul id_student
        :param id_student: integer
        :return: -
        """
        self.__repo_studenti.sterge_student_dupa_id(id_student)
    def get_all_service(self):
        """

        :return:lista de studenti
        """
        return self.__repo_studenti.get_all()
    def modifica_student_dupa_id_service(self,id_student,nume,grupa):
        """
        Modifica studentul cu id_ul id_student si il transforma in noul student
        :param id_student:integer
        :param nume: string
        :param grupa: integer
        :return:
        """
        student = Student(id_student, nume, grupa)
        self.__repo_studenti.modifica_student(student)
    def cauta_student_dupa_id_service(self,id_student):
        """
        Cauta studentul cu id_student, iar daca nu il gaseste semnaleaza erori
        :param id_student: integer
        :return: studentul gasit,daca exista
        """
        return self.__repo_studenti.cauta_student_dupa_id(id_student)
    def numar_studenti_service(self):
        """
        :return:numarul studentilor din lista (integer)
        """
        return self.__repo_studenti.numar_studenti()