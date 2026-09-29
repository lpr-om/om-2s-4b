import customtkinter as gui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests
from datetime import datetime

# Configurações da Janela
app = gui.CTk()
app.title("Previsão Semanal - São Paulo")
app.geometry("800x600")
app.configure(fg_color="#2b2b2b")

# Criação do Gráfico no Matplotlib
plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(7, 4), dpi=100)
fig.patch.set_facecolor('#2b2b2b')
ax.set_facecolor("#2b2b2b")
canvas = FigureCanvasTkAgg(fig, master=app)
canvas.get_tk_widget().pack(fill=gui.BOTH, expand=True, padx=20, pady=10)

def ao_fechar():
    plt.close("all")
    app.destroy()

def buscar_previsao_semanal():
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        # 1. PARÂMETROS PARA 7 DIAS E DADOS DIÁRIOS
        params = {
            "latitude": -23.5505,
            "longitude": -46.6333,
            "daily": ["temperature_2m_max", "temperature_2m_min"],
            "forecast_days": 7,
            "timezone": "America/Sao_Paulo"
        }
        
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        
        # 2. EXTRAÇÃO DOS DADOS DIÁRIOS
        EIXO_X = data["daily"]["time"]
        temp_max = data["daily"]["temperature_2m_max"]
        temp_min = data["daily"]["temperature_2m_min"]
        
        # Formata datas para "DD/MM"
        dias = [datetime.fromisoformat(d).strftime("%d/%m") for d in EIXO_X]
        return dias, temp_max, temp_min
    
    except Exception as e:
        print(f"Erro ao buscar previsão: {e}")
        return None, None, None

def plotar_grafico():
    dias, temp_max, temp_min = buscar_previsao_semanal()
    
    if dias and temp_max and temp_min:
        ax.clear()
        
        # 3. PLOTAGEM DAS DUAS LINHAS (MÁXIMA E MÍNIMA)
        ax.plot(dias, temp_max, marker='o', color='#ef4444', linewidth=2, label='Máxima (°C)')
        ax.plot(dias, temp_min, marker='o', color='#3b82f6', linewidth=2, label='Mínima (°C)')
        
        # Adiciona valores numéricos acima dos pontos de máxima e abaixo das mínimas
        for i in range(len(dias)):
            ax.text(i, temp_max[i] + 0.8, f"{temp_max[i]}°", color='#ef4444', fontsize=8, ha='center', fontweight='bold')
            ax.text(i, temp_min[i] - 1.5, f"{temp_min[i]}°", color='#3b82f6', fontsize=8, ha='center', fontweight='bold')
        
        # Destaque para o dia de "Hoje" (índice 0)
        ax.axvline(x=0, color='#f59e0b', linestyle='--', linewidth=1.5, alpha=0.7)
        ax.text(0, max(temp_max) + 3, "Hoje", color='#f59e0b', fontweight='bold', fontsize=9, ha='center')

        # Ajustes Visuais e Legenda
        ax.set_ylabel("Temperatura (°C)", color="white")
        ax.set_title("Previsão do Tempo para os Próximos 7 Dias - São Paulo", fontsize=12, color="white")
        ax.tick_params(axis='x', colors="white")
        ax.tick_params(axis='y', colors="white")
        ax.grid(True, linestyle="--", alpha=0.3)
        
        # Configuração da legenda compatível com o modo escuro
        ax.legend(loc='upper right', facecolor='#2b2b2b', edgecolor='white', labelcolor='white')
        
        # Ajusta limites de Y para os valores numéricos não saírem da tela
        ax.set_ylim(min(temp_min) - 4, max(temp_max) + 5)
        fig.tight_layout()
        
        canvas.draw()

plotar_grafico()  # Chama a função para desenhar o gráfico ao iniciar o programa
app.protocol("WM_DELETE_WINDOW", ao_fechar)
app.mainloop()