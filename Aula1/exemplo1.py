# Importa a biblioteca customtkinter e chama de "gui"
import customtkinter as gui

# Função chamada quando o botão for clicado
def verificar_senha():
    senha = caixa_texto.get()  # pega a senha que foi digitada
    tamanho_senha = len(senha)  # calcula o tamanho da senha
    if tamanho_senha < 8:
        rotulo.configure(text=f"Senha fraca! - {tamanho_senha} caracteres")  # atualiza o rótulo...
    else:
        rotulo.configure(text=f"Senha forte! - {tamanho_senha} caracteres")  # atualiza o rótulo...

# Configuração do tema (opções: dark, light e system)
gui.set_appearance_mode("light")

# Cria a janela principal
janela = gui.CTk()
janela.title("Verificador de senha - V1.0")
janela.geometry("350x180")

# Campo de entrada de texto
caixa_texto = gui.CTkEntry(
    janela,
    placeholder_text="Digite a senha a ser verificada...",
    width=200,
    show="*"
)
caixa_texto.pack(pady=10)

# Botão que executa a função
botao = gui.CTkButton(
    janela,
    text="Verificar senha",
    command=verificar_senha
)
botao.pack(pady=10)

rotulo = gui.CTkLabel(janela, 
    text="Resultado da verificação.",
    font=("Arial", 16), text_color="black"
)
rotulo.pack(pady=10)

# Mantém a janela aberta
janela.mainloop()
