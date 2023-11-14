class DesempenhoAcademico:

    def __init__(self, aluno):
        self.nomeAluno = aluno
        self.media = 0
        self.situacao = False
        self.materia = None
        self.array_materias =[[]*6, []*6, []*6, []*6, []]
        self.aprovado_ou_nao = 'Reprovado'

    def escolher_materia(self):
        print('''
        Matérias:
        1. Matemática
        2. Português
        3; Ciências
        4. Ed. Física
        5. Inglês
        ''')
        self.materia = input('Qual matéria? ')
        match self.materia.lower():
            case 'matemática':
                self.materia = 0
                return self.materia
            case 'português':
                self.materia = 1
                return self.materia
            case 'ciências':
                self.materia = 2
                return self.materia
            case 'ed. física':
                self.materia = 3
                return self.materia
            case 'inglês':
                self.materia = 4
                return self.materia
            case _:
                self.materia = None
                return self.materia, print('Matéria não encontrada, verifique os acentos.')

    def media_materia(self, nota1, nota2, nota3, nota4):
        if self.materia is None:
            return print('Escolha uma matéria primeiro')
        else:
            self.media = (nota1 + nota2 + nota3 + nota4) / 4
            if self.media < 5:
                self.aprovado_ou_nao = 'Reprovado'
            elif self.media < 7 and self.media >= 5:
                self.aprovado_ou_nao = 'Aprovado na final'
            elif self.media >= 7:
                self.aprovado_ou_nao = 'Aprovado pela média'
            self.array_materias[self.materia] = nota1, nota2, nota3, nota4, self.media, self.aprovado_ou_nao
            return self.array_materias

    def salvar_hitorico(self):
        if 5 <= self.media < 7:
            self.aprovado_ou_nao = 'Aprovado na final'
        elif self.media >= 7:
            self.aprovado_ou_nao = 'Aprovado por média'

        if self.array_materias is None:
            return print('Faça a média primeiro')
        else:
            if len(self.array_materias) == 5:
                print(f'''
                Aluno {self.nomeAluno}
                
                Matemática: 
                Nota 1: {self.array_materias[0][0]}
                Nota 2: {self.array_materias[0][1]}
                Nota 3: {self.array_materias[0][2]}
                Nota 4: {self.array_materias[0][3]}
                Média: {self.array_materias[0][4]}
                Aprovação: {self.array_materias[0][5]}
                
                Português: 
                Nota 1: {self.array_materias[1][0]}
                Nota 2: {self.array_materias[1][1]}
                Nota 3: {self.array_materias[1][2]}
                Nota 4: {self.array_materias[1][3]}
                Média: {self.array_materias[1][4]}
                Aprovação: {self.array_materias[1][5]}
                
                Ciências: 
                Nota 1: {self.array_materias[2][0]}
                Nota 2: {self.array_materias[2][1]}
                Nota 3: {self.array_materias[2][2]}
                Nota 4: {self.array_materias[2][3]}
                Média: {self.array_materias[2][4]}
                Aprovação: {self.array_materias[2][5]}
                
                Ed. Física: 
                Nota 1: {self.array_materias[3][0]}
                Nota 2: {self.array_materias[3][1]}
                Nota 3: {self.array_materias[3][2]}
                Nota 4: {self.array_materias[3][3]}
                Média: {self.array_materias[3][4]}
                Aprovação: {self.array_materias[3][5]}
                                
                Inglês: 
                Nota 1: {self.array_materias[4][0]}
                Nota 2: {self.array_materias[4][1]}
                Nota 3: {self.array_materias[4][2]}
                Nota 4: {self.array_materias[4][3]}
                Média: {self.array_materias[4][4]}
                Aprovação: {self.array_materias[4][5]}
                ''')


aluno = DesempenhoAcademico('Isac')
aluno.escolher_materia()
print(aluno.media_materia(10, 10, 10, 10))
aluno.escolher_materia()
print(aluno.media_materia(3, 3, 3, 3))
aluno.escolher_materia()
print(aluno.media_materia(5, 5, 5, 5))
aluno.escolher_materia()
print(aluno.media_materia(8, 8, 8, 8))
aluno.escolher_materia()
print(aluno.media_materia(2, 2, 2, 2))
aluno.salvar_hitorico()
