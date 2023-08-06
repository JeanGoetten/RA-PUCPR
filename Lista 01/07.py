# ler horário fornecido pelo usuário (h:m:s) e calcular
# minutos transcorridos desde o início do dia
# segundos transcorridos desde o início do dia

from datetime import datetime

f = "%H%M%S"
system_time = datetime.now()

try:
    user_time = (datetime.strptime(input('Insira o horário (HHMMSS): '), f)
                 .replace(year=system_time.year, month=system_time.month, day=system_time.day)
                 .replace(microsecond=0))

    system_time_start_day = system_time.replace(hour=0, minute=0, second=0, microsecond=0)

    user_timestamp = datetime.timestamp(user_time)
    system_timestamp_start_day = datetime.timestamp(system_time_start_day)

    dif_timestamp = user_timestamp - system_timestamp_start_day


    # print(user_time)
    # print(system_time_start_day)
    #
    # print(f"{dif_timestamp/3600: .0f} horas desde o início do dia")

    print(f"{dif_timestamp/60: .0f} minutos desde o início do dia")
    print(f"{dif_timestamp: .0f} segundos desde o início do dia")

except:
    print("Insira o horário no formato recomendado")