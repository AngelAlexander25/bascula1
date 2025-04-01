import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import time
import random
import datetime
import uuid
import io
import base64
from PIL import Image, ImageDraw, ImageFont

# Set the page configuration at the very beginning
st.set_page_config(
    page_title="EcoTrack: Gestión Inteligente de Residuos",
    page_icon="♻️",
    layout="wide"
)

class EcoTrackApp:
    def __init__(self):
        # Configuración de la página
        
        # Estilos mejorados
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Montserrat:wght@500;600;700&display=swap');
        
        body {
            font-family: 'Roboto', sans-serif;
        }

        .main-title {
            font-family: 'Montserrat', sans-serif;
            text-align: center;
            font-size: 2.5em;
            font-weight: 700;
            margin-bottom: 25px;
            color: #007b5e;
        }

        .main-container {
            background: #ffffff;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }

        .metric-card {
            background: #f9f9f9;
            border-radius: 10px;
            padding: 15px;
            text-align: left;
            border: 1px solid #ddd;
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 18px;
            font-weight: 500;
        }

        .metric-card img {
            width: 24px;
            height: 24px;
        }

        .registro-residuos h3 {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 1.8em;
            font-weight: 700;
            color: #333;
        }

        .registro-residuos h3 img {
            width: 28px;
            height: 28px;
        }

        .button-register {
            background-color: #007b5e;
            color: white;
            font-size: 16px;
            font-weight: 600;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            width: 100%;
            border: none;
            transition: 0.3s;
        }

        .button-register:hover {
            background-color: #005f46;
            cursor: pointer;
        }

        .terminal {
            background-color: #000;
            color: #00ff00;
            font-family: monospace;
            padding: 10px;
            border-radius: 5px;
            height: 200px;
            overflow-y: auto;
        }
        
        .employee-card {
            background: linear-gradient(135deg, #1e5799 0%, #207cca 100%);
            color: white;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .qr-container {
            display: flex;
            justify-content: center;
            margin: 15px 0;
        }
        
        .scan-animation {
            border: 2px solid #4CAF50;
            border-radius: 5px;
            padding: 5px;
            animation: scan 1.5s infinite;
        }
        
        @keyframes scan {
            0% { box-shadow: 0 0 0 0 rgba(76, 175, 80, 0.4); }
            70% { box-shadow: 0 0 0 10px rgba(76, 175, 80, 0); }
            100% { box-shadow: 0 0 0 0 rgba(76, 175, 80, 0); }
        }
        
        .scale-reading {
            font-size: 2.5em;
            font-weight: bold;
            text-align: center;
            margin: 15px 0;
            color: #333;
        }
        
        .blinking {
            animation: blink 1s infinite;
        }
        
        @keyframes blink {
            0% { opacity: 1; }
            50% { opacity: 0.3; }
            100% { opacity: 1; }
        }
        
        /* Estilos nuevos para mejorar la apariencia */
        .stButton > button {
            border-radius: 50px !important;
            font-weight: 500 !important;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1) !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 8px rgba(0,0,0,0.15) !important;
        }
        
        /* Estilos para tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: #f8f9fa;
            border-radius: 10px 10px 0 0;
            gap: 10px;
            padding-top: 10px;
            padding-bottom: 10px;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: #e8f5e9 !important;
            font-weight: bold;
        }
        
        h3 {
            font-family: 'Montserrat', sans-serif;
            margin-top: 30px;
        }
        
        h4 {
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            color: #007b5e;
        }005f46;
            cursor: pointer;
        }

        .terminal {
            background-color: #000;
            color: #00ff00;
            font-family: monospace;
            padding: 10px;
            border-radius: 5px;
            height: 200px;
            overflow-y: auto;
        }
        
        .employee-card {
            background: linear-gradient(135deg, #1e5799 0%, #207cca 100%);
            color: white;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .qr-container {
            display: flex;
            justify-content: center;
            margin: 15px 0;
        }
        
        .scan-animation {
            border: 2px solid #4CAF50;
            border-radius: 5px;
            padding: 5px;
            animation: scan 1.5s infinite;
        }
        
        @keyframes scan {
            0% { box-shadow: 0 0 0 0 rgba(76, 175, 80, 0.4); }
            70% { box-shadow: 0 0 0 10px rgba(76, 175, 80, 0); }
            100% { box-shadow: 0 0 0 0 rgba(76, 175, 80, 0); }
        }
        
        .scale-reading {
            font-size: 2.5em;
            font-weight: bold;
            text-align: center;
            margin: 15px 0;
            color: #333;
        }
        
        .blinking {
            animation: blink 1s infinite;
        }
        
        @keyframes blink {
            0% { opacity: 1; }
            50% { opacity: 0.3; }
            100% { opacity: 1; }
        }
        </style>
        """, unsafe_allow_html=True)
        
        self.inicializar_datos()
        self.inicializar_empleados()

    def inicializar_datos(self):
        if 'waste_data' not in st.session_state:
            np.random.seed(42)
            fechas = pd.date_range(start='2023-01-01', end='2024-03-25', freq='W')
            st.session_state.waste_data = pd.DataFrame({
                'Fecha': fechas,
                'Empleado': np.random.choice(['E001', 'E002', 'E003', 'E004', 'E005'], len(fechas)),
                'Orgánicos (kg)': np.random.uniform(3, 7, len(fechas)),
                'Inorgánicos (kg)': np.random.uniform(2, 6, len(fechas)),
                'Peligrosos (kg)': np.random.uniform(0.5, 2, len(fechas))
            })
            st.session_state.waste_data['Total (kg)'] = (
                st.session_state.waste_data['Orgánicos (kg)'] +
                st.session_state.waste_data['Inorgánicos (kg)'] +
                st.session_state.waste_data['Peligrosos (kg)']
            )
        
        # Estados para la simulación
        if 'terminal_logs' not in st.session_state:
            st.session_state.terminal_logs = []
        
        if 'qr_scanned' not in st.session_state:
            st.session_state.qr_scanned = False
            
        if 'current_employee' not in st.session_state:
            st.session_state.current_employee = None
            
        if 'scale_connected' not in st.session_state:
            st.session_state.scale_connected = False
            
        if 'current_weight' not in st.session_state:
            st.session_state.current_weight = 0.0
            
        if 'waste_type' not in st.session_state:
            st.session_state.waste_type = None

    def inicializar_empleados(self):
        if 'employees' not in st.session_state:
            st.session_state.employees = {
                'E001': {'nombre': 'Carlos Rodríguez', 'departamento': 'Administración'},
                'E002': {'nombre': 'María Gómez', 'departamento': 'Operaciones'},
                'E003': {'nombre': 'Juan López', 'departamento': 'Mantenimiento'},
                'E004': {'nombre': 'Ana Martínez', 'departamento': 'Recursos Humanos'},
                'E005': {'nombre': 'Pedro Sánchez', 'departamento': 'Logística'}
            }

    
    def generar_qr_simulado(self, employee_id):
        """Genera una imagen de código QR simulado más realista para un ID de empleado"""
        # Crear una imagen cuadrada blanca
        img_size = 200
        module_size = 8  # Tamaño de cada módulo (cuadrado) del QR
        img = Image.new('RGB', (img_size, img_size), color='white')
        draw = ImageDraw.Draw(img)
        
        # Calcular dimensiones
        modules_count = img_size // module_size
        
        # Semilla aleatoria basada en el ID del empleado
        import random
        seed = sum(ord(c) for c in employee_id)
        random.seed(seed)
        
        # Crear matriz de módulos
        qr_matrix = [[0 for _ in range(modules_count)] for _ in range(modules_count)]
        
        # Función para dibujar los cuadrados de posición
        def add_position_pattern(row, col):
            # Exterior 7x7
            for r in range(7):
                for c in range(7):
                    if (r == 0 or r == 6 or c == 0 or c == 6 or  # Borde exterior
                        (r >= 2 and r <= 4 and c >= 2 and c <= 4)):  # Cuadrado central
                        qr_matrix[row+r][col+c] = 1
                    else:
                        qr_matrix[row+r][col+c] = 0
        
        # Añadir patrones de posición (esquinas)
        add_position_pattern(0, 0)  # Superior izquierdo
        add_position_pattern(0, modules_count-7)  # Superior derecho
        add_position_pattern(modules_count-7, 0)  # Inferior izquierdo
        
        # Añadir patrón de alineación (para QR más grandes)
        alignment_pos = modules_count - 9
        if modules_count >= 25:  # Solo para QR más grandes
            for r in range(5):
                for c in range(5):
                    if (r == 0 or r == 4 or c == 0 or c == 4 or (r == 2 and c == 2)):
                        qr_matrix[alignment_pos+r][alignment_pos+c] = 1
                    else:
                        qr_matrix[alignment_pos+r][alignment_pos+c] = 0
        
        # Añadir patrones de sincronización
        for i in range(modules_count):
            # Horizontal
            if i % 2 == 0 and i >= 8 and i < modules_count - 8:
                qr_matrix[6][i] = 1
            # Vertical
            if i % 2 == 0 and i >= 8 and i < modules_count - 8:
                qr_matrix[i][6] = 1
        
        # Llenar datos (aleatoriamente pero basados en el ID)
        for r in range(modules_count):
            for c in range(modules_count):
                # Saltarse las áreas de los patrones de posición
                skip_positions = (
                    (r < 7 and c < 7) or  # Superior izquierdo
                    (r < 7 and c >= modules_count-7) or  # Superior derecho
                    (r >= modules_count-7 and c < 7)  # Inferior izquierdo
                )
                
                # Saltarse las líneas de sincronización
                skip_timing = (r == 6 or c == 6)
                
                # Llenar con datos aleatorios solo donde no hay patrones
                if not skip_positions and not skip_timing:
                    # Probabilidad variable según la posición para crear un patrón más realista
                    prob = 0.35
                    if (r + c) % 3 == 0:  # Crear algunos patrones
                        prob = 0.65
                    
                    # Mayor aleatoriedad cerca del centro
                    center_distance = ((r - modules_count/2)**2 + (c - modules_count/2)**2)**0.5
                    if center_distance < modules_count/4:
                        prob = 0.5
                    
                    if random.random() < prob:
                        qr_matrix[r][c] = 1
        
        # Dibujar la matriz en la imagen
        for r in range(modules_count):
            for c in range(modules_count):
                if qr_matrix[r][c] == 1:
                    draw.rectangle([
                        c * module_size, 
                        r * module_size, 
                        (c + 1) * module_size - 1, 
                        (r + 1) * module_size - 1
                    ], fill='black')
        
        # Convertir a bytes para mostrar en streamlit
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        return buf.getvalue()

    def agregar_log(self, mensaje):
        """Añade un mensaje al log del terminal"""
        timestamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        st.session_state.terminal_logs.append(f"[{timestamp}] {mensaje}")
        
    def simular_conexion_rj232(self):
        """Simula la conexión con una báscula a través de RJ232"""
        self.agregar_log("Iniciando conexión con báscula vía RJ232...")
        
        for i in range(3):
            self.agregar_log(f"Buscando dispositivos... ({i+1}/3)")
            time.sleep(0.5)
            
        self.agregar_log("Dispositivo encontrado: BÁSCULA MODELO TX-500")
        self.agregar_log("Estableciendo conexión...")
        time.sleep(0.7)
        self.agregar_log("Conexión establecida. ID: SCL-{0:08X}".format(random.randint(0, 0xFFFFFFFF)))
        
        st.session_state.scale_connected = True
        self.agregar_log("Báscula lista para recibir datos.")

    def simular_lectura_bascula(self, tipo_residuo):
        """Simula la lectura de peso desde la báscula"""
        if not st.session_state.scale_connected:
            self.agregar_log("ERROR: Báscula no conectada. Intente nuevamente.")
            return
            
        self.agregar_log(f"Iniciando pesaje de residuo tipo: {tipo_residuo}")
        self.agregar_log("Esperando colocación de bolsa...")
        
        # Generar un peso aleatorio según el tipo de residuo
        if tipo_residuo == "Orgánicos":
            peso = round(random.uniform(3.0, 7.0), 2)
        elif tipo_residuo == "Inorgánicos":
            peso = round(random.uniform(2.0, 6.0), 2)
        else:  # Peligrosos
            peso = round(random.uniform(0.5, 2.0), 2)
            
        time.sleep(1)
        
        # Simular fluctuaciones de peso
        for _ in range(3):
            peso_fluctuante = round(peso + random.uniform(-0.3, 0.3), 2)
            st.session_state.current_weight = peso_fluctuante
            time.sleep(0.5)
            
        # Peso final estabilizado
        st.session_state.current_weight = peso
        st.session_state.waste_type = tipo_residuo
        
        self.agregar_log(f"Peso estabilizado: {peso} kg")
        self.agregar_log("Lectura completada correctamente.")
        
        return peso

    def guardar_registro(self, employee_id, tipo_residuo, peso):
        """Guarda un nuevo registro de residuos en la base de datos"""
        fecha_actual = datetime.datetime.now().date()
        
        # Crear registro con valores cero para los tipos no seleccionados
        organicos = peso if tipo_residuo == "Orgánicos" else 0
        inorganicos = peso if tipo_residuo == "Inorgánicos" else 0
        peligrosos = peso if tipo_residuo == "Peligrosos" else 0
        
        nuevo_registro = pd.DataFrame({
            'Fecha': [fecha_actual],
            'Empleado': [employee_id],
            'Orgánicos (kg)': [organicos],
            'Inorgánicos (kg)': [inorganicos],
            'Peligrosos (kg)': [peligrosos],
            'Total (kg)': [peso]
        })
        
        st.session_state.waste_data = pd.concat([st.session_state.waste_data, nuevo_registro], ignore_index=True)
        self.agregar_log(f"Registro guardado: {tipo_residuo}, {peso} kg, Empleado: {employee_id}")
        
        # Resetear estados
        st.session_state.current_weight = 0.0
        st.session_state.waste_type = None

    def crear_grafico_dispersion_3d(self):
        df = st.session_state.waste_data
        fig = go.Figure()

        categorias = ['Orgánicos', 'Inorgánicos', 'Peligrosos']
        colores = ['green', 'blue', 'red']
        
        for i, categoria in enumerate(categorias):
            fig.add_trace(go.Scatter3d(
                x=df['Fecha'],
                y=np.full(len(df), categoria),  
                z=df[f'{categoria} (kg)'],
                mode='markers',
                marker=dict(size=5, color=colores[i], opacity=0.7),
                name=categoria
            ))

        fig.update_layout(
            title="🌍 Distribución de Bolsas de Residuos en 3D",
            scene=dict(
                xaxis_title="Fecha",
                yaxis_title="Tipo de Residuo",
                zaxis_title="Peso (kg)"
            )
        )
        return fig

    def crear_grafico_sankey(self):
        datos = st.session_state.waste_data
        objetivos = ['Orgánicos', 'Inorgánicos', 'Peligrosos']
        valores = [
            datos['Orgánicos (kg)'].sum(),
            datos['Inorgánicos (kg)'].sum(),
            datos['Peligrosos (kg)'].sum()
        ]

        fig = go.Figure(data=[go.Sankey(
            node=dict(label=["Generación"] + objetivos, color=["#6baed6", "#74c476", "#fd8d3c", "#fdae61"]),
            link=dict(source=[0, 0, 0], target=[1, 2, 3], value=valores)
        )])

        fig.update_layout(title="🔀 Flujo de Residuos (Sankey)")
        return fig

    def crear_grafico_radar(self):
        df = st.session_state.waste_data[['Orgánicos (kg)', 'Inorgánicos (kg)', 'Peligrosos (kg)']].sum()
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=df.values,
            theta=df.index,
            fill='toself',
            name="Distribución de Residuos"
        ))
        fig.update_layout(title="📊 Proporción de Tipos de Residuos", polar=dict(radialaxis=dict(visible=True)))
        return fig
        
    def crear_grafico_empleados(self):
        """Crea un gráfico de barras por empleado"""
        df = st.session_state.waste_data.groupby('Empleado')[['Orgánicos (kg)', 'Inorgánicos (kg)', 'Peligrosos (kg)']].sum().reset_index()
        
        # Añadir nombres de empleados
        df['Nombre'] = df['Empleado'].map(lambda x: st.session_state.employees.get(x, {}).get('nombre', 'Desconocido'))
        
        fig = px.bar(
            df, 
            x='Nombre', 
            y=['Orgánicos (kg)', 'Inorgánicos (kg)', 'Peligrosos (kg)'],
            title="Aportación de Residuos por Empleado",
            labels={'value': 'Kilogramos', 'variable': 'Tipo de Residuo'}
        )
        
        return fig

    def mostrar_graficos_avanzados(self):
        st.markdown("## 📊 Análisis y Reportes de Residuos")
        
        # Mostrar métricas en una fila de tarjetas
        st.markdown("<h3>📈 Métricas Generales</h3>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            total_organicos = st.session_state.waste_data['Orgánicos (kg)'].sum()
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); 
                 border-radius: 10px; padding: 20px; text-align: center;
                 box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <img src="https://cdn-icons-png.flaticon.com/512/3209/3209202.png" style="width: 40px; height: 40px; margin-bottom: 10px;">
                <h4 style="margin:0; color: #2e7d32;">Orgánicos</h4>
                <p style="font-size: 28px; font-weight: bold; margin: 10px 0; color: #1b5e20;">{total_organicos:.1f} kg</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            total_inorganicos = st.session_state.waste_data['Inorgánicos (kg)'].sum()
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); 
                 border-radius: 10px; padding: 20px; text-align: center;
                 box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <img src="https://cdn-icons-png.flaticon.com/512/1686/1686301.png" style="width: 40px; height: 40px; margin-bottom: 10px;">
                <h4 style="margin:0; color: #1565c0;">Inorgánicos</h4>
                <p style="font-size: 28px; font-weight: bold; margin: 10px 0; color: #0d47a1;">{total_inorganicos:.1f} kg</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            total_peligrosos = st.session_state.waste_data['Peligrosos (kg)'].sum()
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); 
                 border-radius: 10px; padding: 20px; text-align: center;
                 box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <img src="https://cdn-icons-png.flaticon.com/512/1250/1250624.png" style="width: 40px; height: 40px; margin-bottom: 10px;">
                <h4 style="margin:0; color: #e65100;">Peligrosos</h4>
                <p style="font-size: 28px; font-weight: bold; margin: 10px 0; color: #bf360c;">{total_peligrosos:.1f} kg</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Mostrar últimos registros
        st.markdown("""
        <h3 style="margin-top: 30px;">📋 Últimos Registros</h3>
        """, unsafe_allow_html=True)
        
        st.dataframe(
            st.session_state.waste_data.sort_values('Fecha', ascending=False).head(5), 
            use_container_width=True,
            hide_index=True
        )
        
        # Tabs para gráficos
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "Evolución Temporal", 
            "Distribución 3D", 
            "Flujo de Residuos", 
            "Proporción",
            "Por Empleado"
        ])

        with tab1:
            st.markdown("<h4 style='text-align: center;'>Evolución de Residuos en el Tiempo</h4>", unsafe_allow_html=True)
            fig_area = px.area(
                st.session_state.waste_data, x='Fecha', y=['Orgánicos (kg)', 'Inorgánicos (kg)', 'Peligrosos (kg)'],
                labels={'value': 'Kilogramos', 'variable': 'Tipo de Residuo'},
                color_discrete_map={
                    'Orgánicos (kg)': '#4CAF50', 
                    'Inorgánicos (kg)': '#2196F3', 
                    'Peligrosos (kg)': '#FF9800'
                }
            )
            fig_area.update_layout(
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
                margin=dict(l=20, r=20, t=40, b=20),
            )
            st.plotly_chart(fig_area, use_container_width=True)

        with tab2:
            st.markdown("<h4 style='text-align: center;'>Distribución de Residuos en 3D</h4>", unsafe_allow_html=True)
            st.plotly_chart(self.crear_grafico_dispersion_3d(), use_container_width=True)

        with tab3:
            st.markdown("<h4 style='text-align: center;'>Flujo de Generación de Residuos</h4>", unsafe_allow_html=True)
            st.plotly_chart(self.crear_grafico_sankey(), use_container_width=True)

        with tab4:
            st.markdown("<h4 style='text-align: center;'>Proporción de Tipos de Residuos</h4>", unsafe_allow_html=True)
            st.plotly_chart(self.crear_grafico_radar(), use_container_width=True)
            
        with tab5:
            st.markdown("<h4 style='text-align: center;'>Aportación por Empleado</h4>", unsafe_allow_html=True)
            st.plotly_chart(self.crear_grafico_empleados(), use_container_width=True)
            
        # Sección de generación de reportes
        st.markdown("""
        <h3 style="margin-top: 30px;">📑 Generación de Reportes</h3>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            <div style="background: #f8f9fa; border-radius: 10px; padding: 15px; height: 100%;">
                <h4 style="text-align: center; margin-bottom: 15px;">Reporte por Empleado</h4>
                <p>Genere un reporte detallado del aporte de residuos por empleado en un período específico.</p>
            </div>
            """, unsafe_allow_html=True)
            
            emp_reporte = st.selectbox(
                "Seleccionar empleado:",
                options=list(st.session_state.employees.keys()),
                format_func=lambda x: f"{x} - {st.session_state.employees[x]['nombre']}",
                key="emp_report_select"
            )
            
            if st.button("Generar Reporte de Empleado", key="gen_emp_report"):
                emp_data = st.session_state.employees[emp_reporte]
                emp_residuos = st.session_state.waste_data[st.session_state.waste_data['Empleado'] == emp_reporte]
                
                total_org = emp_residuos['Orgánicos (kg)'].sum()
                total_inorg = emp_residuos['Inorgánicos (kg)'].sum()
                total_pel = emp_residuos['Peligrosos (kg)'].sum()
                total_general = total_org + total_inorg + total_pel
                
                st.markdown(f"""
                <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 20px; margin-top: 15px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                        <h4 style="margin: 0; color: #007b5e;">REPORTE DE EMPLEADO</h4>
                        <span style="background: #e9ecef; padding: 5px 10px; border-radius: 30px; font-size: 12px;">
                            Generado: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}
                        </span>
                    </div>
                    
                    <div style="display: flex; align-items: center; margin-bottom: 15px;">
                        <div style="background: #6c757d; color: white; width: 40px; height: 40px; 
                                   border-radius: 50%; display: flex; align-items: center; justify-content: center;
                                   margin-right: 15px; font-weight: bold;">
                            {emp_reporte[1:]}
                        </div>
                        <div>
                            <h5 style="margin: 0; font-size: 18px;">{emp_data['nombre']}</h5>
                            <p style="margin: 0; color: #6c757d; font-size: 14px;">{emp_data['departamento']}</p>
                        </div>
                    </div>
                    
                    <div style="background: #f8f9fa; border-radius: 8px; padding: 15px; margin: 15px 0;">
                        <h5 style="margin-top: 0;">Resumen de Aportes</h5>
                        <p><strong>Total de Registros:</strong> {len(emp_residuos)}</p>
                        <p><strong>Total Aportado:</strong> {total_general:.2f} kg</p>
                        <div style="display: flex; margin-top: 10px;">
                            <div style="flex: 1; text-align: center; padding: 10px; background: rgba(76, 175, 80, 0.1); border-radius: 5px; margin-right: 5px;">
                                <p style="font-size: 12px; margin: 0; color: #2e7d32;">ORGÁNICOS</p>
                                <p style="font-size: 18px; font-weight: bold; margin: 5px 0; color: #2e7d32;">{total_org:.2f} kg</p>
                                <p style="font-size: 12px; margin: 0; color: #2e7d32;">{(total_org/total_general*100) if total_general > 0 else 0:.1f}%</p>
                            </div>
                            <div style="flex: 1; text-align: center; padding: 10px; background: rgba(33, 150, 243, 0.1); border-radius: 5px; margin-right: 5px;">
                                <p style="font-size: 12px; margin: 0; color: #1565c0;">INORGÁNICOS</p>
                                <p style="font-size: 18px; font-weight: bold; margin: 5px 0; color: #1565c0;">{total_inorg:.2f} kg</p>
                                <p style="font-size: 12px; margin: 0; color: #1565c0;">{(total_inorg/total_general*100) if total_general > 0 else 0:.1f}%</p>
                            </div>
                            <div style="flex: 1; text-align: center; padding: 10px; background: rgba(255, 152, 0, 0.1); border-radius: 5px;">
                                <p style="font-size: 12px; margin: 0; color: #e65100;">PELIGROSOS</p>
                                <p style="font-size: 18px; font-weight: bold; margin: 5px 0; color: #e65100;">{total_pel:.2f} kg</p>
                                <p style="font-size: 12px; margin: 0; color: #e65100;">{(total_pel/total_general*100) if total_general > 0 else 0:.1f}%</p>
                            </div>
                        </div>
                    </div>
                    
                    <p style="text-align: center; font-size: 12px; color: #6c757d; margin-top: 20px;">
                        ID Reporte: REP-{uuid.uuid4().hex[:6].upper()}
                    </p>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: #f8f9fa; border-radius: 10px; padding: 15px; height: 100%;">
                <h4 style="text-align: center; margin-bottom: 15px;">Reporte por Período</h4>
                <p>Genere un informe completo de todos los residuos generados en un período seleccionado.</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Selector de fechas
            fecha_inicio = st.date_input("Fecha inicio:", key="fecha_inicio")
            fecha_fin = st.date_input("Fecha fin:", key="fecha_fin")
            
            if st.button("Generar Reporte de Período", key="gen_period_report"):
                # Convertir las fechas de date a datetime para poder comparar con el dataframe
                fecha_inicio_dt = pd.Timestamp(fecha_inicio)
                fecha_fin_dt = pd.Timestamp(fecha_fin)
                
                # Filtrar datos por el período seleccionado
                periodo_data = st.session_state.waste_data[
                    (st.session_state.waste_data['Fecha'] >= fecha_inicio_dt) & 
                    (st.session_state.waste_data['Fecha'] <= fecha_fin_dt)
                ]
                
                # Calcular totales
                total_organicos = periodo_data['Orgánicos (kg)'].sum()
                total_inorganicos = periodo_data['Inorgánicos (kg)'].sum()
                total_peligrosos = periodo_data['Peligrosos (kg)'].sum()
                total_general = total_organicos + total_inorganicos + total_peligrosos
                
                # Calcular empleados más activos
                empleados_activos = periodo_data.groupby('Empleado')['Total (kg)'].sum().sort_values(ascending=False).head(3)
                
                st.markdown(f"""
                <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 20px; margin-top: 15px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                        <h4 style="margin: 0; color: #007b5e;">REPORTE DE PERÍODO</h4>
                        <span style="background: #e9ecef; padding: 5px 10px; border-radius: 30px; font-size: 12px;">
                            Generado: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}
                        </span>
                    </div>
                    
                    <div style="background: #f8f9fa; border-radius: 8px; padding: 15px; margin-bottom: 15px;">
                        <h5 style="margin-top: 0;">Período Analizado</h5>
                        <p><strong>Desde:</strong> {fecha_inicio.strftime("%d/%m/%Y")}</p>
                        <p><strong>Hasta:</strong> {fecha_fin.strftime("%d/%m/%Y")}</p>
                        <p><strong>Total de Registros:</strong> {len(periodo_data)}</p>
                    </div>
                    
                    <h5>Resumen de Residuos</h5>
                    <div style="height: 30px; background: #e9ecef; border-radius: 15px; margin: 15px 0; overflow: hidden; display: flex;">
                        <div style="width: {(total_organicos/total_general*100) if total_general > 0 else 0}%; height: 100%; background: #4CAF50;"></div>
                        <div style="width: {(total_inorganicos/total_general*100) if total_general > 0 else 0}%; height: 100%; background: #2196F3;"></div>
                        <div style="width: {(total_peligrosos/total_general*100) if total_general > 0 else 0}%; height: 100%; background: #FF9800;"></div>
                    </div>
                    
                    <div style="display: flex; margin-bottom: 20px;">
                        <div style="flex: 1; text-align: center;">
                            <p style="font-size: 12px; margin: 0; color: #2e7d32;">ORGÁNICOS</p>
                            <p style="font-size: 18px; font-weight: bold; margin: 5px 0; color: #2e7d32;">{total_organicos:.2f} kg</p>
                            <p style="font-size: 12px; margin: 0; color: #2e7d32;">{(total_organicos/total_general*100) if total_general > 0 else 0:.1f}%</p>
                        </div>
                        <div style="flex: 1; text-align: center;">
                            <p style="font-size: 12px; margin: 0; color: #1565c0;">INORGÁNICOS</p>
                            <p style="font-size: 18px; font-weight: bold; margin: 5px 0; color: #1565c0;">{total_inorganicos:.2f} kg</p>
                            <p style="font-size: 12px; margin: 0; color: #1565c0;">{(total_inorganicos/total_general*100) if total_general > 0 else 0:.1f}%</p>
                        </div>
                        <div style="flex: 1; text-align: center;">
                            <p style="font-size: 12px; margin: 0; color: #e65100;">PELIGROSOS</p>
                            <p style="font-size: 18px; font-weight: bold; margin: 5px 0; color: #e65100;">{total_peligrosos:.2f} kg</p>
                            <p style="font-size: 12px; margin: 0; color: #e65100;">{(total_peligrosos/total_general*100) if total_general > 0 else 0:.1f}%</p>
                        </div>
                    </div>
                    
                    <div style="background: #f8f9fa; border-radius: 8px; padding: 15px;">
                        <h5 style="margin-top: 0;">Top Contribuyentes</h5>
                        {''.join([f"""
                        <div style="display: flex; align-items: center; margin-bottom: 10px;">
                            <div style="background: #6c757d; color: white; width: 30px; height: 30px; 
                                      border-radius: 50%; display: flex; align-items: center; justify-content: center;
                                      margin-right: 10px; font-size: 12px; font-weight: bold;">
                                {emp[1:]}
                            </div>
                            <div style="flex-grow: 1;">
                                <p style="margin: 0; font-size: 14px;">{st.session_state.employees[emp]['nombre']}</p>
                                <div style="height: 6px; background: #e9ecef; border-radius: 3px; margin-top: 5px;">
                                    <div style="width: {(valor/empleados_activos.iloc[0]*100)}%; height: 100%; background: #007b5e; border-radius: 3px;"></div>
                                </div>
                            </div>
                            <div style="margin-left: 10px; font-weight: bold; font-size: 14px;">
                                {valor:.1f} kg
                            </div>
                        </div>
                        """ for emp, valor in empleados_activos.items()])}
                    </div>
                    
                    <p style="text-align: center; font-size: 12px; color: #6c757d; margin-top: 20px;">
                        ID Reporte: REP-{uuid.uuid4().hex[:6].upper()}
                    </p>
                </div>
                """, unsafe_allow_html=True)

    def ejecutar(self):
        st.markdown("<h1 class='main-title'>EcoTrack: Gestión Inteligente de Residuos</h1>", unsafe_allow_html=True)
        st.markdown("<div class='main-container'>", unsafe_allow_html=True)
        
        tab_simulacion, tab_analisis = st.tabs([
            "🔄 Sistema Automático", 
            "📊 Análisis y Reportes"
        ])
        
        with tab_simulacion:
            st.markdown("<h3>🔌 Sistema Automático de Registro de Residuos</h3>", unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                # Sección de empleados y QR
                st.markdown("<h4>👤 Escaneo de QR de Empleado</h4>", unsafe_allow_html=True)
                
                # Seleccionar empleado para simular escaneo
                employee_selector = st.selectbox(
                    "Seleccionar empleado para simulación:",
                    options=list(st.session_state.employees.keys()),
                    format_func=lambda x: f"{x} - {st.session_state.employees[x]['nombre']}",
                    key="employee_selector_key"
                )
                
                # Botón para escanear QR
                if st.button("Simular Escaneo de QR"):
                    st.session_state.qr_scanned = True
                    st.session_state.current_employee = employee_selector
                    self.agregar_log(f"QR escaneado: Empleado {employee_selector}")
                    self.agregar_log(f"Identificado: {st.session_state.employees[employee_selector]['nombre']}")
                
                # Mostrar QR y tarjeta de empleado si hay uno seleccionado
                if st.session_state.qr_scanned and st.session_state.current_employee:
                    emp_id = st.session_state.current_employee
                    emp_data = st.session_state.employees[emp_id]
                    
                    # Tarjeta de empleado
                    st.markdown(f"""
                    <div class='employee-card'>
                        <h4>🆔 Empleado Identificado</h4>
                        <p><strong>ID:</strong> {emp_id}</p>
                        <p><strong>Nombre:</strong> {emp_data['nombre']}</p>
                        <p><strong>Departamento:</strong> {emp_data['departamento']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # QR simulado del empleado
                    st.markdown("<div class='qr-container'>", unsafe_allow_html=True)
                    qr_image = self.generar_qr_simulado(emp_id)
                    st.image(qr_image, width=150, output_format="PNG", caption="QR del empleado")
                    st.markdown("</div>", unsafe_allow_html=True)
                
            with col2:
                # Sección de báscula y RJ232
                st.markdown("<h4>⚖️ Simulación de Báscula (RJ232)</h4>", unsafe_allow_html=True)
                
                # Botón para conectar báscula
                if not st.session_state.scale_connected:
                    if st.button("Conectar Báscula (RJ232)"):
                        self.simular_conexion_rj232()
                else:
                    st.success("✅ Báscula conectada y lista para usar")
                
                # Selección de tipo de residuo
                if st.session_state.scale_connected:
                    tipo_residuo = st.radio(
                        "Seleccione tipo de residuo a pesar:",
                        ["Orgánicos", "Inorgánicos", "Peligrosos"],
                        horizontal=True
                    )
                    
                    # Botón para pesar
                    if st.button("Simular Colocación de Bolsa y Pesaje"):
                        if st.session_state.qr_scanned:
                            peso = self.simular_lectura_bascula(tipo_residuo)
                        else:
                            self.agregar_log("ERROR: Escanee primero un QR de empleado")
                
                # Mostrar peso actual
                if st.session_state.current_weight > 0:
                    st.markdown(f"""
                    <div class='scale-reading'>
                        <span>⚖️ {st.session_state.current_weight} kg</span>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Botón para guardar registro
                    if st.button("Confirmar y Guardar Registro"):
                        if st.session_state.current_employee and st.session_state.waste_type:
                            self.guardar_registro(
                                st.session_state.current_employee,
                                st.session_state.waste_type,
                                st.session_state.current_weight
                            )
                            st.success("✅ Registro guardado exitosamente")
                        else:
                            st.error("Error: Falta información del empleado o tipo de residuo")
            
            # Terminal de simulación
            st.markdown("<h4>🖥️ Terminal de Comunicación</h4>", unsafe_allow_html=True)
            terminal = st.empty()
            terminal.markdown("<div class='terminal'>{}</div>".format("<br>".join(st.session_state.terminal_logs)), unsafe_allow_html=True)
            
            # Botón para reiniciar simulación
            if st.button("Reiniciar Simulación"):
                st.session_state.qr_scanned = False
                st.session_state.current_employee = None
                st.session_state.scale_connected = False
                st.session_state.current_weight = 0.0
                st.session_state.waste_type = None
                st.session_state.terminal_logs = []
                self.agregar_log("Sistema reiniciado.")
                st.experimental_rerun()
                
        with tab_analisis:
            self.mostrar_graficos_avanzados()

        st.markdown("</div>", unsafe_allow_html=True)

def main():
    app = EcoTrackApp()
    app.ejecutar()

if __name__ == "__main__":
    main()