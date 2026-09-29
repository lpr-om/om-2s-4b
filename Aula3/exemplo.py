import customtkinter as gui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Configurações da Janela
app = gui.CTk()
app.title("Construindo gráficos")
app.geometry("800x600")
app.configure(fg_color="#ffffff")

# Criação do Gráfico no Matplotlib (Largura: 7, Altura: 3 polegadas)
fig, ax = plt.subplots(figsize=(7, 3))
canvas = FigureCanvasTkAgg(fig, master=app)
canvas.draw()
canvas.get_tk_widget().pack(padx=20, pady=20)
ax.set_title("Gráfico de Notas")

# Função para fechar TUDO corretamente ao clicar no "X"
def ao_fechar():
    plt.close("all")  # Libera a memória do Matplotlib
    app.destroy()  # Encerra a janela do CustomTkinter

# Função para limpar o gráfico
def limpar_grafico():
    entrada_eixo_x.delete(0, gui.END)  # Limpa a entrada do eixo X
    entrada_eixo_y.delete(0, gui.END)  # Limpa a entrada do eixo Y
    ax.clear()  # Limpa o gráfico atual
    canvas.draw()  # Atualiza o canvas para refletir a limpeza

# Função para desenhar o gráfico
def desenhar_grafico():
    EIXO_X = entrada_eixo_x.get().split()
    EIXO_Y = [float(x) for x in entrada_eixo_y.get().split()]
    ax.clear()  # Limpa o gráfico atual antes de desenhar um novo
    ax.bar(EIXO_X, EIXO_Y)  # Desenha o gráfico de barras verticais
    ax.set_title("Gráfico de Notas")
    canvas.draw()

# caixa de texto para as categorias do eixo X
entrada_eixo_x = gui.CTkEntry(app, width=400, placeholder_text="Digite quatro disciplinas")
entrada_eixo_x.pack(pady=10)

# caixa de texto para os valores do eixo Y
entrada_eixo_y = gui.CTkEntry(app, width=400, placeholder_text="Digite as notas correspondentes")
entrada_eixo_y.pack(pady=10)

# Botão para desenhar o gráfico
botao = gui.CTkButton(app, text="Desenhar Gráfico", command=desenhar_grafico)
botao.pack(pady=10)
# Botão para limpar o gráfico
botao_limpar = gui.CTkButton(app, text="Limpar Gráfico", command = limpar_grafico)
botao_limpar.pack(pady=10)

app.protocol("WM_DELETE_WINDOW", ao_fechar)
app.mainloop()
