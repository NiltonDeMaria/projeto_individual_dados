candidatosLista = [[5, 10, 8, 8], [10, 7, 7, 8], [8, 5, 4, 9], [2, 2, 2, 1], [10, 10, 8, 9]]

def buscaCandidatos(e, t, p, s):
    
    tamanhoLista = len(candidatosLista)
    b = 0

    for n in range(tamanhoLista):
        if (candidatosLista[n][0] >= e and
            candidatosLista[n][1] >= t and
            candidatosLista[n][2] >= p and
            candidatosLista[n][3] >= s):

            candidato = n + 1
            print(f"   Candidato {candidato} atende o critério.")
            b += 1
    if b == 0:
        print("   Nenhuma candidato atente ao critério.")

