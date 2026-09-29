import customtkinter as gui

def calcular_imc():
    try:
        # Pega os valores digitados e converte para números decimais (float)
        peso = float(caixa_peso.get())
        altura = float(caixa_altura.get())
        
        # Fórmula do IMC: peso dividido pela altura ao quadrado
        imc = peso / (altura ** 2)
        
        # Classificação simples em 3 níveis
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc <= 24.9:
            classificacao = "Peso normal"
        else:
            classificacao = "Acima do peso"
            
        # Atualiza o texto na tela mostrando o resultado (com 1 casa decimal)
        rotulo_resultado.configure(
            text=f"IMC: {imc:.1f}\nClassificação: {classificacao}"
        )
    except ValueError:
        # Se o usuário digitar letras ou deixar vazio, exibe um aviso
        rotulo_resultado.configure(text="Por favor, digite números válidos!")

# 1. Configuração do tema (opções: dark, light e system)
gui.set_appearance_mode("light")

# 2. Criação da janela principal
janela = gui.CTk()
janela.title("Calculadora de IMC")
janela.geometry("350x400")

# 3. Título do aplicativo
titulo = gui.CTkLabel(janela, text="Calculadora de IMC", font=("Arial", 20, "bold"))
titulo.pack(pady=20)

# 4. Campo para o Peso
rotulo_peso = gui.CTkLabel(janela, text="Digite seu peso (kg):")
rotulo_peso.pack(pady=5)
caixa_peso = gui.CTkEntry(janela, placeholder_text="Ex: 60.5")
caixa_peso.pack(pady=5)

# 5. Campo para a Altura
rotulo_altura = gui.CTkLabel(janela, text="Digite sua altura (m):")
rotulo_altura.pack(pady=5)
caixa_altura = gui.CTkEntry(janela, placeholder_text="Ex: 1.75")
caixa_altura.pack(pady=5)

# 6. Botão para acionar o cálculo
botao = gui.CTkButton(janela, text="Calcular", command=calcular_imc)
botao.pack(pady=20)

# 7. Texto que vai exibir o resultado na tela
rotulo_resultado = gui.CTkLabel(janela, text="", font=("Arial", 14, "bold"))
rotulo_resultado.pack(pady=10)

# Inicia o loop da janela para mantê-la aberta
janela.mainloop()