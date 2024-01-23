print("============== Conjugador Verbal ==============")

pessoas = ['Eu', 'Tu', 'Ele', 'Nós', 'Vós', 'Eles'];

conjuga_ar_presente_ind = ['o', 'as', 'a', 'amos', 'ais', 'am'];
conjuga_er_presente_ind = ['o', 'es', 'e', 'emos', 'eis', 'em'];
conjuga_ir_presente_ind = ['o', 'es', 'e', 'imos', 'is', 'em'];

conjuga_ar_preterito_per = ['ei', 'aste', 'ou', 'amos', 'astes', 'aram'];
conjuga_er_preterito_per = ['i', 'este', 'eu', 'emos', 'estes', 'eram'];
conjuga_ir_preterito_per = ['i', 'iste', 'iu', 'imos', 'istes', 'iram'];

conjuga_ar_futuro_presen = ['arei', 'arás', 'ará', 'aremos', 'areis', 'arão'];
conjuga_er_futuro_presen = ['erei', 'erás', 'erá', 'eremos', 'ereis', 'erão'];
conjuga_ir_futuro_presen = ['irei', 'irás', 'irá', 'iremos', 'ireis', 'irão'];

verbo = input("Digite o verbo: ")
termina = verbo[-2:]
#print(termina)
if termina == 'ar':
    print("Presente do indicativo")
    print()
    for i in range(6):
        print(pessoas[i] + ' ' + verbo[:-2] + conjuga_ar_presente_ind[i])
    print()
    print("Pretérito perfeito")
    print()
    for i in range(6):
        print(pessoas[i] + ' ' + verbo[:-2] + conjuga_ar_preterito_per[i])
    print()
    print("Futuro do presente")
    print()
    for i in range(6):
        print(pessoas[i] + ' ' + verbo[:-2] + conjuga_ar_futuro_presen[i])
elif termina == 'er':
    print("Presente do indicativo")
    print()
    for i in range(6):
        print(pessoas[i] + ' ' + verbo[:-2] + conjuga_er_presente_ind[i])
    print()
    print("Pretérito perfeito")
    print()
    for i in range(6):
        print(pessoas[i] + ' ' + verbo[:-2] + conjuga_er_preterito_per[i])
    print()
    print("Futuro do presente")
    print()
    for i in range(6):
        print(pessoas[i] + ' ' + verbo[:-2] + conjuga_er_futuro_presen[i])
elif termina == 'ir':
    print("Presente do indicativo")
    print()
    for i in range(6):
        print(pessoas[i] + ' ' + verbo[:-2] + conjuga_ir_presente_ind[i])
    print()
    print("Pretérito perfeito")
    print()
    for i in range(6):
        print(pessoas[i] + ' ' + verbo[:-2] + conjuga_ir_preterito_per[i])
    print()
    print("Futuro do presente")
    print()
    for i in range(6):
        print(pessoas[i] + ' ' + verbo[:-2] + conjuga_ir_futuro_presen[i])