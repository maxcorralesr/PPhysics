import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.widgets import Slider

# Constantes
GRAVEDAD = 9.81  # Aceleración debido a la gravedad (m/s^2)

def movimiento_proyectil(velocidad_inicial, angulo_lanzamiento, altura_inicial):
    angulo_lanzamiento_rad = math.radians(angulo_lanzamiento)
    
    tiempo_vuelo = (velocidad_inicial * math.sin(angulo_lanzamiento_rad) + math.sqrt((velocidad_inicial * math.sin(angulo_lanzamiento_rad))**2 + 2 * GRAVEDAD * altura_inicial)) / GRAVEDAD
    
    t = np.linspace(0, tiempo_vuelo, num=500)
    x = velocidad_inicial * np.cos(angulo_lanzamiento_rad) * t
    y = altura_inicial + velocidad_inicial * np.sin(angulo_lanzamiento_rad) * t - 0.5 * GRAVEDAD * t**2
    
    return x, y

# Configurar la figura y los ejes
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)
ax.set_xlabel("Distancia horizontal (m)")
ax.set_ylabel("Altura (m)")
ax.set_title("Movimiento de proyectiles")
ax.grid(True)
ax.set_xlim(0, 50)
ax.set_ylim(0, 25)

# Valores iniciales
velocidad_inicial = 10
angulo_lanzamiento = 45
altura_inicial = 0
x, y = movimiento_proyectil(velocidad_inicial, angulo_lanzamiento, altura_inicial)
line, = ax.plot(x, y, label="Trayectoria")
ax.legend()

# Agregar sliders
ax_velocidad = plt.axes([0.1, 0.15, 0.65, 0.03])
ax_angulo = plt.axes([0.1, 0.1, 0.65, 0.03])
ax_altura = plt.axes([0.1, 0.05, 0.65, 0.03])

slider_velocidad = Slider(ax_velocidad, "Velocidad (m/s)", 1, 50, valinit=velocidad_inicial)
slider_angulo = Slider(ax_angulo, "Ángulo (°)", 0, 90, valinit=angulo_lanzamiento)
slider_altura = Slider(ax_altura, "Altura (m)", 0, 50, valinit=altura_inicial)

def actualizar(val):
    v = slider_velocidad.val
    a = slider_angulo.val
    h = slider_altura.val
    x, y = movimiento_proyectil(v, a, h)
    line.set_xdata(x)
    line.set_ydata(y)
    ax.set_xlim(0, max(x) * 1.1)
    ax.set_ylim(0, max(y) * 1.1)
    fig.canvas.draw_idle()

slider_velocidad.on_changed(actualizar)
slider_angulo.on_changed(actualizar)
slider_altura.on_changed(actualizar)

plt.show()