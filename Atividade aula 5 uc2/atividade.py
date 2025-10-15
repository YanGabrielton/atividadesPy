import kagglehub
from kagglehub import KaggleDatasetAdapter

# Nome do arquivo dentro do dataset
file_path = "student_exam_scores.csv"

# Carrega o dataset direto do Kaggle
dataf = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "saadaliyaseen/analyzing-student-academic-trends",
    file_path,
)

# Agrupando: média das notas por horas estudadas e horas dormidas
media_horas_estudadas_dormidas = dataf.groupby(['hours_studied', 'sleep_hours'])['exam_score'].mean()

# Agrupando: média das notas em função das horas estudadas
notas_por_horas = dataf.groupby('hours_studied')['exam_score'].mean()

# Exibe os resultados

print("\nMédia das notas por horas estudadas e dormidas:\n", media_horas_estudadas_dormidas)
print("\nMédia das notas por horas estudadas:\n", notas_por_horas)



#agora vou fazer da media de aprovados que estudaram pouco 

aprovados_estudandoPouco = dataf[(dataf['hours_studied'] <= 4) & (dataf['exam_score'] >= 20)]
print("\n Aprovados:\n ",aprovados_estudandoPouco)