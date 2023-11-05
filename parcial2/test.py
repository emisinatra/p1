#aca voy a hacer los casos de prueba
#importo
from main import is_mutant

# defino los casos de prueba
test_cases = [
    ['ATGCGA', 'CAGTGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG'],  # caso de prueba mutante
    ['ATGCGA', 'CAGTGC', 'TTATTT', 'AGACGG', 'GCGTCA', 'TCACTG'],  # caso de prueba no mutante
]

# y aca los pruebo
for i, dna in enumerate(test_cases):
    print(f"Caso de prueba {i+1}:")
    print("\n".join(dna))
    if is_mutant(dna):
        print("La secuencia de ADN es mutante.")
    else:
        print("La secuencia de ADN no es mutante.")
    print()
