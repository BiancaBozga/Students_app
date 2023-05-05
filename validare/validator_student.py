from erori.validation_error import ValidationError


class ValidatorStudent:
    def __init__(self):
        pass
    def valideaza_student(self,student):
        """
        Valideaza daca id-ul intreg al studentului este >0, daca numele este diferit de sirul vid si daca grupa este>0
        :param student: student de tipul Student,unic identificabil prin id intreg,nume de tip string si grupa de tip integer
        :return: none sau eroare daca exista
        """
        erori=""
        if student.get_id_student()<0:
            erori+="id invalid!\n"
        if student.get_nume_student()=="":
            erori+="nume invalid!\n"
        if student.get_grupa_student()<0:
            erori+="grupa invalida!\n"
        if len(erori)>0:
            raise ValidationError(erori)

