import platform
import getpass
import shutil
import logging
import os


logging.basicConfig(
    filename="log/assist_desenvolvimento.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%y-%m-%d %H:%M:%S"
)


def exibir_menu():
    print("\n===================== ASSISTENTE DE IMPLANTAÇÃO - T.I. =====================\n")
    print(
    "1. Verificar Ambiente \n"
    "2. Listar Aplicativos \n"
    "3. Iniciar Instalação \n"
    "4. Consultar Logs \n"
    "0. Sair \n"
    "\n ============================================================================ \n")


def verificar_ambiente(): 
    maquina = platform.uname()
    total, usado, livre = shutil.disk_usage("C:\\")

    total_gb = total / (1024**3)
    usado_gb = usado / (1024**3)
    livre_gb = livre / (1024**3)
    pouco_espaco = livre_gb<5

    print("Verificando ambiente...\n")
    print("\n========================= DIAGNÓSTICO DO AMBIENTE ===========================\n")
    logging.info("Iniciando diagnóstico do ambiente.")
    print(f"Sistema Operacional: {platform.system()}")
    print(f"Processador: {maquina.processor}")
    print(f"Versão do Python: {platform.python_version()}")
    print(f"Nome da máquina: {maquina.node}")
    print(f"Usuário atual: {getpass.getuser()}")
    print(f"Espaço total: {total_gb:.2f}GB")
    print(f"Espaço usado: {usado_gb:.2f}GB")
    print(f"Espaço livre: {livre_gb:.2f}GB")
    if pouco_espaco:
        print("\nALERTA: pouco espaço livre em disco. Verifique os requisitos antes de instalar aplicativos.")
        logging.warning("Pouco espaço livre em disco.")
    else:
        print("\nEspaço livre para instalar. ")
        logging.info("Espaço livre acima do limite de alerta.")
    print("\n=============================================================================\n")

def listar_apps(): 
    print("Listando aplicativos...")

def iniciar_instalacao(): 
    print("Iniciando instalação...")

def consultar_logs(): 
    print("Consultando logs...")

while True:

    exibir_menu()
    resp = input("Escolha uma opção: ")


    if resp == "1":
        verificar_ambiente()
    elif resp == "2":
        listar_apps()
    elif resp == "3":
        iniciar_instalacao()
    elif resp == "4":
        consultar_logs()
    elif resp == "0":
        print("Fim do programa.\n")
        break
    else:
        print("Opção inválida.")
    input("\nPressione ENTER para continuar...")
   
print("\nPrograma encerrado.")
print("\n ============================================================================ \n")
