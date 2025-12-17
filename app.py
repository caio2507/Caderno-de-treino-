import datetime
import os 
DIRETORIO_BASE = os.path.dirname(os.path.abspath(__file__)) 


#Pede ao usuário o peso e as repetições para uma série específica."""
def coletar_dados_serie(numero_serie):

    print(f"\n   --- Série {numero_serie} ---")
    
    # Valida o Peso
    while True:
        try:
            peso = float(input("   Digite o PESO (em kg): "))
            if peso < 0:
                print("O peso não pode ser negativo. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o peso.")

    while True:
        try:
            repeticoes = int(input("   Digite as REPETIÇÕES: "))
            if repeticoes < 1:
                print("As repetições devem ser pelo menos 1. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para as repetições.")
            
    return {"peso": peso, "repeticoes": repeticoes}


#Pede o nome do exercício e o número de séries, e coleta os dados de cada série.
def coletar_dados_exercicio():
    
    nome_exercicio = input("\nQual EXERCÍCIO: ").strip().title()
    
    while True:
        try:
            num_series = int(input(f"Quantas SÉRIES de {nome_exercicio} você vai fazer: "))
            if num_series <= 0:
                print("O número de séries deve ser maior que zero. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    series_coletadas = []
    
    for i in range(1, num_series + 1):
        dados_serie = coletar_dados_serie(i)
        series_coletadas.append(dados_serie)
        
    return {
        "exercicio": nome_exercicio,
        "series": series_coletadas
    }


# Formata os dados do treino e salva em um arquivo TXT.
def salvar_treino(nome_treino, treino_data):
    
    data_hora = datetime.datetime.now().strftime("|%H:%M:%S | %d-%m-%y|")
    
    nome_arquivo = os.path.join(DIRETORIO_BASE, "historico_treino.txt")
    
    conteudo_arquivo = f"==== {nome_treino.upper()} REGISTRADO em {data_hora} ====\n"
    
    for exercicio_info in treino_data:
        conteudo_arquivo += f"\n- EXERCÍCIO: {exercicio_info['exercicio']} ({len(exercicio_info['series'])} Séries)\n"
        
        for i, serie in enumerate(exercicio_info['series']):
            peso = serie['peso']
            reps = serie['repeticoes']
            conteudo_arquivo += f"   Série {i + 1}: {peso:.1f} kg x {reps} repetições\n"
            
    conteudo_arquivo += "\n" + ("=" * 40) + "\n"
    
    with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
        arquivo.write(conteudo_arquivo)
        
    print(f"\n>>> ✅ Histórico do treino salvo em '{nome_arquivo}'! <<<")

def iniciar_caderno_treino():

    print("--- 🏋️ CADERNO DE TREINO VIRTUAL INICIADO 🏋️ ---")
    
    nome_treino = input("Qual Grupo muscular você vai treino: ").strip().title()
    
    treino_completo = []
    
    while True:
        
        dados_exercicio = coletar_dados_exercicio()
        treino_completo.append(dados_exercicio)
        
        continuar = input("\nDeseja adicionar outro exercício? (s/n): ").strip().lower()
        
        if continuar != 's':
            break

    if treino_completo:
        salvar_treino(nome_treino, treino_completo)
    else:
        print("Nenhum exercício registrado. Treino encerrado.")


# Mostra o histórico de treinos salvos.
def ver_historico():
    
    nome_arquivo = os.path.join(DIRETORIO_BASE, "historico_treino.txt")
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            
            if conteudo:
                print("\n" + "="*50)
                print("📋 HISTÓRICO DE TREINOS")
                print("="*50)
                print(conteudo)
            else:
                print("\n⚠️  Nenhum treino registrado ainda.")
                
    except FileNotFoundError:
        print("\n⚠️  Arquivo de histórico não encontrado. Faça seu primeiro treino!")


if __name__ == "__main__":
    while True:
        print("\n" + "="*50)
        print("   🏋️ CADERNO DE TREINO 🏋️    ")
        print("="*50)
        print("1. Registrar novo treino")
        print("2. Ver histórico")
        print("3. Sair")
        print("="*50)
        
        escolha = input("\nEscolha uma opção: ").strip()
        
        if escolha == "1":
            iniciar_caderno_treino()
        elif escolha == "2":
            ver_historico()
        elif escolha == "3":
            print("\n👋 Até a próxima! Bons treinos!")
            break 
        else:
            print("\n❌ Opção inválida. Tente novamente.")