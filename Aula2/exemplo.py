import customtkinter as gui

app = gui.CTk()
app.title("Verificador de vogais")
app.geometry("450x350")

# 1. Nossa lista de vogais, incluindo acentos
VOGAIS = ['a', 'e', 'i', 'o', 'u', 'á', 'à', 'â', 'ã', 'é', 'ê', 'í', 'ó', 'ô', 'õ', 'ú']


# 2. Função para analisar a frase digitada pelo usuário
def analisar_frase():
    texto_usuario = entrada_texto.get().lower() # A frase é transformada em minúsculas 
    total_vogais = 0
    for letra in texto_usuario: # LAÇO DE REPETIÇÃO - para cada letra do texto ...
        if letra in VOGAIS: # CONDICIONAIS: O contador de vogais
            total_vogais = total_vogais + 1

    # Mostrando o resultado na interface gráfica
    lbl_resultado.configure(text=f"Total de vogais: {total_vogais}")
    

# 3. Interface Gráfica Simples
gui.CTkLabel(app, text="Digite uma frase qualquer para ser analisada:", 
             font=("Arial", 14)).pack(pady=10)

entrada_texto = gui.CTkEntry(app, width=350, placeholder_text="Ex: Bom dia, como você está?")
entrada_texto.pack(pady=10)

btn_analisar = gui.CTkButton(app, text="Analisar Texto", command=analisar_frase)
btn_analisar.pack(pady=15)

lbl_resultado = gui.CTkLabel(app, text="Aguardando análise...", font=("Arial", 16, "bold"))
lbl_resultado.pack(pady=20)

app.mainloop()



