class Student:
    def __init__(self,id_student,nume,grupa):
        self.__id_student=id_student
        self.__nume=nume
        self.__grupa=grupa
    def get_id_student(self):
        """

        :return:id-ul intreg al studentului
        """
        return self.__id_student
    def get_nume_student(self):
        """

        :return:numele string al studentului
        """
        return self.__nume
    def set_nume_student(self,nume):
        """
        Seteaza numele studentului la numele nou numen de tip string
        :param nume:string
        :return: -
        """
        self.__nume=nume
    def get_grupa_student(self):
        """

        :return:grupa de tip intreg a studentului
        """
        return self.__grupa
    def set_grupa_student(self,grupa):
        """
        seteaza grupa studentului la noua grupa
        :param grupa: integer
        :return:
        """
        self.__grupa=grupa
    def __equ__(self,other):
        """
        Verifica daca doi concurenti au aceleasi id-uri
        :param other:Student,class
        :return:
        """
        return self.__id_student==other.__id_student
    def __str__(self):
        """

        :return:id-ul studentului, numele si grupa
        """
        return f"{self.__id_student} {self.__nume} {self.__grupa}"


