Aqui está um exemplo de README para o seu código:

# Desempenho Acadêmico

Este é um programa simples em Python que permite a um aluno inserir notas em diferentes matérias e verificar seu desempenho acadêmico.

## Funcionalidades

- Escolher matérias (Matemática, Português, Ciências, Ed. Física, Inglês).
- Inserir notas para cada matéria.
- Calcular a média e determinar a situação do aluno (Aprovado, Aprovado na final, Reprovado).
- Salvar o histórico de desempenho.

## Uso

1. Instale o Python em sua máquina, se ainda não tiver.
2. Clone este repositório.
3. Execute o script `desempenho_academico.py`.

## Exemplo de Uso

```python
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
aluno.salvar_historico()
```

## Observações

- Certifique-se de escolher uma matéria antes de inserir as notas.
- A situação do aluno é determinada pelas seguintes faixas de média: 
  - Média < 5: Reprovado
  - 5 <= Média < 7: Aprovado na final
  - Média >= 7: Aprovado por média
