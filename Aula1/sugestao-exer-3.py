import customtkinter as gui


def calcular_bhaskara():
    try:
        # Pega os valores dos coeficientes digitados nas caixas de texto
        a = float(caixa_a.get())
        b = float(caixa_b.get())
        c = float(caixa_c.get())
        
        # A regra principal: o coeficiente 'a' não pode ser zero
        if a == 0:
            rotulo_resultado.configure(text="O valor de 'a' não pode ser 0.\n(Não é uma equação do 2º grau)")
            return
            
        # 1º Passo: Calcular o Delta (b² - 4ac)
        delta = (b ** 2) - (4 * a * c)
        
        # 2º Passo: Analisar o Delta e calcular as raíces
        if delta < 0:
            rotulo_resultado.configure(
                text=f"Delta = {delta:.2f}\nNão existem raízes reais (Delta menor que 0)."
            )
        elif delta == 0:
            x = -b / (2 * a)
            rotulo_resultado.configure(
                text=f"Delta = {delta:.0f}\nPossui uma única raiz real:\nx = {x:.2f}"
            )
        else:
            raiz_delta = delta ** 0.5  # Raiz quadrada - delta elevado a 0.5
            x1 = (-b + raiz_delta) / (2 * a)
            x2 = (-b - raiz_delta) / (2 * a)
            
            rotulo_resultado.configure(
                text=f"Delta = {delta:.2f}\nPossui duas raízes reais:\nx₁ = {x1:.2f}\nx₂ = {x2:.2f}"
            )
            
    except ValueError:
        # Mensagem caso o usuário digite letras ou deixe algum campo vazio
        rotulo_resultado.configure(text="Por favor, digite números válidos em todos os campos!")


# 0. Configuração do tema (opções: dark, light e system)
gui.set_appearance_mode("light")

# 1. Criação da janela principal
janela = gui.CTk()
janela.title("Calculadora de Bhaskara")
janela.geometry("380x450")

# 2. Título do aplicativo
titulo = gui.CTkLabel(janela, text="Equação do 2º Grau", font=("Arial", 20, "bold"))
titulo.pack(pady=20)

# 3. Rótulo e Caixa para o coeficiente 'a'
rotulo_a = gui.CTkLabel(janela, text="Digite o valor de 'a':")
rotulo_a.pack(pady=2)
caixa_a = gui.CTkEntry(janela, placeholder_text="Ex: 1")
caixa_a.pack(pady=5)

# 4. Rótulo e Caixa para o coeficiente 'b'
rotulo_b = gui.CTkLabel(janela, text="Digite o valor de 'b':")
rotulo_b.pack(pady=2)
caixa_b = gui.CTkEntry(janela, placeholder_text="Ex: -5")
caixa_b.pack(pady=5)

# 5. Rótulo e Caixa para o coeficiente 'c'
rotulo_c = gui.CTkLabel(janela, text="Digite o valor de 'c':")
rotulo_c.pack(pady=2)
caixa_c = gui.CTkEntry(janela, placeholder_text="Ex: 6")
caixa_c.pack(pady=5)

# 6. Botão para acionar o cálculo
botao = gui.CTkButton(janela, text="Calcular Raízes", command=calcular_bhaskara)
botao.pack(pady=20)

# 7. Rótulo que vai exibir os resultados na tela
rotulo_resultado = gui.CTkLabel(janela, text="", font=("Arial", 14, "bold"), justify="center")
rotulo_resultado.pack(pady=10)

# Inicia o loop da janela
janela.mainloop()