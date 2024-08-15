import tkinter as tk
from tkinter import ttk

def calcular_pagos(precio, tipo_cambio, plazo):
    """
    Calcula el pago mensual y el importe total para un sistema fotovoltaico
    basado en el precio, el tipo de cambio y el plazo.

    Args:
        precio (float): Precio del sistema fotovoltaico en dólares.
        tipo_cambio (float): Tipo de cambio (no utilizado en esta versión).
        plazo (int): Plazo en meses.

    Returns:
        tuple: Pago mensual y importe total.
    """
    # Comisiones y tasas
    comision = 3.6
    iva = 0.576
    sobretasa_dict = {3: 4.5, 6: 7.5, 9: 9.9, 12: 11.95}
    
    # Calculamos la tasa total para el plazo
    sobretasa = sobretasa_dict[plazo]
    iva_sobretasa = sobretasa * (iva / 100)
    total_tasa = comision + iva + sobretasa + iva_sobretasa
    total_rate_percentage = total_tasa / 100
    
    # Calculamos el importe total
    importe_total = precio * (1 + total_rate_percentage)
    
    # Calculamos el pago mensual
    pago_mensual = importe_total / plazo
    
    return pago_mensual, importe_total

def mostrar_resultados():
    try:
        precio = float(entry_precio.get())
        tipo_cambio = float(entry_tipo_cambio.get())
        plazo = int(combo_plazo.get())
        
        pago_mensual, importe_total = calcular_pagos(precio, tipo_cambio, plazo)
        
        label_resultado.config(text=f"Pago mensual: ${pago_mensual:.2f}\nImporte total: ${importe_total:.2f}")
    except ValueError:
        label_resultado.config(text="Por favor, ingrese valores válidos.")
    except KeyError:
        label_resultado.config(text="Por favor, seleccione un plazo válido.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Pagos de Sistema Fotovoltaico")

# Crear los widgets
label_precio = ttk.Label(root, text="Precio del sistema fotovoltaico ($):")
label_precio.grid(column=0, row=0, padx=10, pady=10)

entry_precio = ttk.Entry(root)
entry_precio.grid(column=1, row=0, padx=10, pady=10)

label_tipo_cambio = ttk.Label(root, text="Tipo de cambio:")
label_tipo_cambio.grid(column=0, row=1, padx=10, pady=10)

entry_tipo_cambio = ttk.Entry(root)
entry_tipo_cambio.grid(column=1, row=1, padx=10, pady=10)

label_plazo = ttk.Label(root, text="Plazo (meses):")
label_plazo.grid(column=0, row=2, padx=10, pady=10)

combo_plazo = ttk.Combobox(root, values=[3, 6, 9, 12])
combo_plazo.grid(column=1, row=2, padx=10, pady=10)
combo_plazo.current(0)

button_calcular = ttk.Button(root, text="Calcular", command=mostrar_resultados)
button_calcular.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

label_resultado = ttk.Label(root, text="")
label_resultado.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Iniciar el bucle principal
root.mainloop()
