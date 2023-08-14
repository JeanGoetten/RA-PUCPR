# Os fabricantes de discos rígidos usam potências de dez (definidas no Sistema Internacional) para
# expressar a capacidade dos discos. Assim quando é anunciado um disco rígido com 500 GB (ou 500 Gbytes,
# em grafia correta), o disco tem aproximadamente 500 bilhões de bytes (500 x 109 ); que correspondem,
# entretanto, a aproximadamente 465,6 GiB (465,6 gibibytes = 465 x 230 ). Para maiores informações sobre esta
# ambiguidade ler o artigo da Wikipédia sobre “Prefixo binário”.
# Elabore um algoritmo que leia a capacidade de um disco rígido (em notação comercial) e mostre quantos
# gibibytes de fato ele tem.

print("============== Capacidade real de um dispositivo de armazenamento digital ==============")

capacidade_anunciada = float(input("Insira a capacidade anunciada do dispositivo (GB): "))

def conversor(capacidade_anunciada):
    dif = (capacidade_anunciada * 7.4)/100
    capacidade_real = capacidade_anunciada - dif
    return capacidade_real


def conversor2(capacidade_anunciada):
    capacidade_real = capacidade_anunciada/1.073741824
    return capacidade_real

print(f"Cpacidade real ~= {conversor2(capacidade_anunciada): .2f} gibibytes")