import customtkinter as gui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests
from datetime import datetime

# Configurações da Janela
app = gui.CTk()
app.title("Umidade Relativa do Ar - São Paulo")
app.geometry("800x600")
app.configure(fg_color="#2b2b2b")  # Cor de fundo preta

# Criação do Gráfico no Matplotlib (Largura: 7, Altura: 4 polegadas)
plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(7, 4), dpi=100)
fig.patch.set_facecolor('#2b2b2b')
ax.set_facecolor("#2b2b2b")
canvas = FigureCanvasTkAgg(fig, master=app)
canvas.get_tk_widget().pack(fill=gui.BOTH, expand=True, padx=20, pady=10)

# Função para fechar TUDO corretamente ao clicar no "X"
def ao_fechar():
    plt.close("all")  # Libera a memória do Matplotlib
    app.destroy()  # Encerra a janela do CustomTkinter

def buscar_previsao_tempo():
    try:
        # Coordenadas de São Paulo (Lat: -23.55, Lon: -46.63)
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": -23.5505,
            "longitude": -46.6333,
            "hourly": "relative_humidity_2m",  # 1. PARAMETRO ALTERADO
            "forecast_days": 1,
            "timezone": "America/Sao_Paulo"
        }
        
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        
        # Extrai horas e umidade das próximas 24h
        EIXO_X = data["hourly"]["time"]
        EIXO_Y = data["hourly"]["relative_humidity_2m"]  # 2. CHAVE ALTERADA
        
        # Formata o texto de hora para "HH:MM"
        horas = [datetime.fromisoformat(h).strftime("%H:%M") for h in EIXO_X]
     
        return horas, EIXO_Y
    
    except Exception as e:
        print(f"Erro ao buscar previsão: {e}")
        return None, None

def plotar_grafico():
    horas, umidade = buscar_previsao_tempo()
    
    if horas and umidade:
        ax.clear()
        # Plota a linha de umidade com tom azul (#3b82f6)
        ax.plot(horas, umidade, marker='o', color='#3b82f6', linewidth=2)
        
        # 3. ROTULOS E ESCALA AJUSTADOS
        ax.set_ylabel("Umidade Relativa (%)", color="white")
        ax.set_ylim(0, 100)  # Fixa a escala percentual de 0 a 100%
        ax.set_title("Umidade Relativa do Ar - São Paulo", fontsize=12, color="white")
        
        ax.tick_params(axis='x', rotation=45, labelsize=8, colors="white")
        ax.tick_params(axis='y', colors="white")
        ax.grid(True, linestyle="--", alpha=0.3)
        fig.tight_layout()
        
        canvas.draw()

plotar_grafico()  # Chama a função para desenhar o gráfico ao iniciar o programa
app.protocol("WM_DELETE_WINDOW", ao_fechar)
app.mainloop()