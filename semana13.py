# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 36},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 23}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 9},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 21}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 24}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 21}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 37}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 10},
            {"day": "Domingo", "temp": 26}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 36},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 34}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 30}
        ]
    ]
]
# para la tarea de esta semana usamos como base la tarea de la anterior semana
# a el proceso de for de la semana anterior le agrgamos una funcion
def funcion_calcular_promedio(temperaturas):
    funcion_calcular_promedio = {}
    ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]
    for ciudad_idx, ciudad in enumerate(temperaturas):
        for semana_idx, semana in enumerate(ciudad):
            suma_temperaturas = sum([dia["temp"] for dia in semana])
            promedio = suma_temperaturas / len(semana)
            print(f"promedio de temperaturas {ciudades[ciudad_idx]},semanas{semana_idx + 1}, promedio{promedio:.2f}°C")
# luego usamos return en la misma funcion
    return funcion_calcular_promedio
#  para finlizar llamamos a la función para calcular promedio
calcular_promedio = funcion_calcular_promedio(temperaturas)
