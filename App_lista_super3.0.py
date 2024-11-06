from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.uix.scrollview import ScrollView 
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window 

class PantallaInicio (Screen): 
    def __init__(self, **kawargs):
        super().__init__(**kawargs)

        layout = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)
        WelcomeLabel = Label (text = "App Lista del Super", font_size = '30sp', color = (0,0,0,1) )
        layout.add_widget(WelcomeLabel)

        boton_registro = Button(text = "Anotar productos", pos_hint = {"center_x": 0.5}, background_color = (0.6, 1, 0.6, 1))
        boton_registro.bind (on_press = self.CambiarRegistro) 
        layout.add_widget(boton_registro)

        boton_verduras = Button(text = "Verduras y Fruta", pos_hint = {"center_x": 0.5}, background_color = (0.6, 1, 0.6, 1))
        boton_verduras.bind (on_press = self.CambiarVerduras) 
        layout.add_widget(boton_verduras)

        boton_total = Button(text = "Total", pos_hint = {"center_x": 0.5}, background_color = (0.6, 1, 0.6, 1))
        boton_total.bind (on_press = self.CambiarTotal) 
        layout.add_widget(boton_total)

        self.add_widget(layout)

    def CambiarRegistro (self, instance): 
        self.manager.current = 'registro'
    
    def CambiarTotal (self, instance):
        self.manager.current = 'total'

    def CambiarVerduras (self, instance): 
        self.manager.current = 'verduras'

class RegistroGastos (Screen): 
    def __init__(self, **kwargs): 
        super().__init__(**kwargs)

        Window.clearcolor = (1,1,1,1)
        
        self.layout = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)

        self.producto_input = TextInput (hint_text = "Ingrese el articulo", multiline = False, size_hint_y = None, height = 80)
        self.layout.add_widget(self.producto_input)

        self.precio_input = TextInput (hint_text = "Ingrese el precio del articulo", multiline = False, size_hint_y = None, height = 80, input_filter = 'float')
        self.layout.add_widget(self.precio_input)

        self.cantidad_input = TextInput (hint_text = "Ingresa la cantidad de este producto", multiline = False, size_hint_y = None, height = 80, input_filter = 'int')
        self.layout.add_widget(self.cantidad_input)

        boton_agregar = Button (text = "Agregar producto", size_hint = (0.5, None), height = 100, pos_hint = {"center_x":0.5}, background_color = (0,1,0,1))
        boton_agregar.bind(on_press = self.AgregarProducto)
        self.layout.add_widget(boton_agregar)

        self.resultado_label = Label(text = "", color = (0,0,0,1))
        self.layout.add_widget(self.resultado_label)

        boton_volver = Button(text = "Volver", pos_hint = {"center_x": 0.5}, background_color = (0.6, 1, 0.6, 1))
        boton_volver.bind (on_press = self.volver_registro) 
        self.layout.add_widget(boton_volver)

        self.add_widget(self.layout)

        self.lista_precios = []

    def volver_registro (self, instance):
        self.manager.current = 'inicio'

    def AgregarProducto (self, instance):
        producto = self.producto_input.text
        try: 
            cantidad = int(self.cantidad_input.text)
            precio = float(self.precio_input.text)
            total_precio = precio * cantidad
            self.lista_precios.append ((producto, total_precio))

            self.producto_input.text = ""
            self.precio_input.text = ""
            self.cantidad_input.text = ""
            self.resultado_label.text = "Producto Agregado"
        except ValueError: 
            self.resultado_label.text = "Ingresa un precio valido"

class VerdurasFrutas (Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.layout = BoxLayout (orientation = 'vertical', padding = 20, spacing = 10 )

        insctruction_label = Label (text = "Verduras y Frutas", font_size = '30sp', color = (0,0,0,1))
        self.layout.add_widget(insctruction_label)

        self.producto_input = TextInput (hint_text = "Ingresa el producto", multiline = False, font_size = '16sp', size_hint_y = None, height = 80) 
        self.layout.add_widget(self.producto_input)

        self.precio_por_kilo = TextInput (hint_text = "Ingresa el valor por kilo", multiline = False, font_size = '16sp', size_hint_y = None, height = 80)
        self.layout.add_widget(self.precio_por_kilo)

        self.gramaje_input = TextInput (hint_text = "Ingresa en gramos lo que hagarraste", multiline = False, font_size = '16sp', size_hint_y = None, height = 80)
        self.layout.add_widget(self.gramaje_input)

        agregar_button = Button (text = "Agregar producto", size_hint = (0.5, None), height = 100, pos_hint = {"center_x":0.5}, background_color = (0,1,0,1))
        agregar_button.bind(on_press = self.agregar_producto)
        self.layout.add_widget(agregar_button)

        self.resultado_label = Label (text = "", color = (0,0,0,1))
        self.layout.add_widget(self.resultado_label)
        
        boton_volver = Button (text = "Volver", pos_hint = {"center_x": 0.5}, background_color = (0,1,0,1))
        boton_volver.bind (on_press= self.volver_registro)
        self.layout.add_widget(boton_volver)

        self.add_widget(self.layout)

        self.lista_precios = []

    def agregar_producto(self, instance): 
        try: 
            producto = self.producto_input.text
            precio_kilo = float(self.precio_por_kilo.text)
            peso = float(self.gramaje_input.text)
            precio = (peso * precio_kilo)/1000          
            self.lista_precios.append ((producto, precio))

            self.producto_input.text = ""
            self.precio_por_kilo.text = ""
            self.gramaje_input.text = ""
            self.resultado_label.text = "Producto Agregado"
        except ValueError: 
            self.resultado_label.text = "Ingrese peso o costo valido"

    def volver_registro(self, instance): 
        self.manager.current = 'inicio'

class ListaTotal(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        layout = BoxLayout (orientation = 'vertical', padding = 20, spacing = 10)

        self.scroll_view = ScrollView (size_hint = (1, None), size = (Window.width, 300))
        self.productos_layout = GridLayout (cols = 1, spacing = 10, size_hint_y = 10)
        self.productos_layout.bind(minimum_height = self.productos_layout.setter ('height'))
        self.scroll_view.add_widget(self.productos_layout)
        layout.add_widget(self.scroll_view)

        boton_calcular_total = Button(text = "Calcular Total")
        boton_calcular_total.bind(on_press = self.calcular_total)
        layout.add_widget(boton_calcular_total)

        self.total_label = Label(text = "")
        layout.add_widget(self.total_label)

        boton_volver = Button(text = "Volver", pos_hint = {"center_x": 0.5}, background_color = (0,1,0,1))
        boton_volver.bind (on_press = self.volver_registro) 
        layout.add_widget(boton_volver)

        self.add_widget(layout)

    def volver_registro (self, instance):
        self.manager.current = 'inicio'

    def calcular_total(self, instance):
        registro_gastos = App.get_running_app().root.get_screen('registro').lista_precios
        verduras_futas = App.get_running_app().root.get_screen('verduras').lista_precios
        all_products = registro_gastos + verduras_futas
        total = sum(precio for nombre, precio in all_products)
        self.total_label.text = f"Total ${total:.2f}"
        self.total_label.color = (0,0,0,1)

    def on_enter(self):
        self.productos_layout.clear_widgets()
        registro_gastos = App.get_running_app().root.get_screen('registro').lista_precios
        verduras_futas = App.get_running_app().root.get_screen('verduras').lista_precios
        all_products = registro_gastos + verduras_futas
        for nombre, precio in all_products: 
            etiqueta = Label(text = f"{nombre} - ${precio:.2f}", size_hint_y = None, height = 40)
            self.productos_layout.add_widget(etiqueta)
            etiqueta.color = (0,0,0,1)

class ListaSuper (App): 
    def build(self): 

        sm = ScreenManager()
        sm.add_widget(PantallaInicio(name = 'inicio'))
        sm.add_widget(RegistroGastos(name = 'registro'))
        sm.add_widget(VerdurasFrutas(name = 'verduras'))
        sm.add_widget(ListaTotal(name = 'total'))
        return sm
    
ListaSuper().run()