

from validare.validator_student import ValidatorStudent
from validare.validator_laborator import ValidatorLaborator
from validare.validator_nota import ValidatorNota
from infrastructura.repo_note import RepoNote
from infrastructura.repo_studenti import RepoStudenti
from infrastructura.repo_laboratoare import RepoLaboratoare
from business.service_note import ServiceNote
from business.service_studenti import ServiceStudenti
from business.service_laboratoare import ServiceLaboratoare
from prezentare.consola import UI
from testare.teste import Teste

if __name__ == '__main__':
  validator_student=ValidatorStudent()
  validator_laborator=ValidatorLaborator()
  validator_nota = ValidatorNota()
  repo_note=RepoNote()
  repo_laboratoare=RepoLaboratoare()
  repo_studenti=RepoStudenti()
  service_studenti=ServiceStudenti(validator_student,repo_studenti)
  service_note=ServiceNote(validator_nota,repo_note)
  service_laboratoare=ServiceLaboratoare(validator_laborator,repo_laboratoare)
  consola=UI(service_studenti,service_laboratoare,service_note)
  teste = Teste(repo_studenti,repo_laboratoare,repo_note,service_laboratoare,service_studenti,service_note)
  teste.ruleaza_toate_testele()
  consola.run()

