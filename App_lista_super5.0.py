# Hecho por Leonardo Martínez Peña
# 12/12/2024

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.uix.scrollview import ScrollView 
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window 

storage = JsonStore("listas.json")

class PantallaInicio (Screen): 
    def __init__(self, **kawargs):
        super().__init__(**kawargs)

        main_layout = FloatLayout()

        layout = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)

        info_Button = Button(text = 'i', size_hint = (0.1,0.05), pos_hint = {'right': 1, 'top': 1})
        info_Button.bind(on_release = self.show_info)
        main_layout.add_widget(info_Button)

        WelcomeLabel = Label (text = "Tu Lista del Super", font_size = '30sp', color = (0,0,0,1) )
        layout.add_widget(WelcomeLabel)

        boton_registro = Button(text = "Anotar productos", pos_hint = {"center_x": 0.5}, background_color = (0.5, 1, 0, 1))
        boton_registro.bind (on_press = self.CambiarRegistro) 
        layout.add_widget(boton_registro)

        boton_verduras = Button(text = "Verduras y Frutas", pos_hint = {"center_x": 0.5}, background_color = (0.5, 1, 0, 1))
        boton_verduras.bind (on_press = self.CambiarVerduras) 
        layout.add_widget(boton_verduras)

        boton_descuentos = Button(text = "Hay descuentos!!", pos_hint = {"center_x": 0.5}, background_color = (0.5, 1, 0, 1))
        boton_descuentos.bind (on_press = self.CambiarDescuentos)
        layout.add_widget(boton_descuentos)

        boton_listas = Button(text = "Listas", pos_hint = {"center_x": 0.5}, background_color = (0.68, 0.86, 0.68, 1))
        boton_listas.bind (on_press = self.CambiarListas)
        layout.add_widget(boton_listas)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def show_info(self, instance):
        close_button = Button(text = "Cerrar", size_hint = (1,0.2), on_release = lambda x: popup.dismiss())
        content = BoxLayout(orientation = 'vertical')
        content.add_widget(Label(text = 'Esta app fue hecha unicamente\npor una persona, soy en\nestudiante de ingieneria en robotica\ny sistemas, mi pasatiempo es\nprogramar y sigo estudiando para\ncrear mejores cosas.\nEs la primera app de varias, espero. \n\nMuchas gracias por instalarla.\n\nAtt. El desarrollador', size_hint = (1,0.8)))
        content.add_widget(close_button)
        popup = Popup(title = 'Sobre mi', content = content, size_hint = (0.9,0.9))
        popup.open()

    def CambiarRegistro (self, instance): 
        self.manager.current = 'registro'

    def CambiarVerduras (self, instance): 
        self.manager.current = 'verduras'
    
    def CambiarDescuentos (self, instance):
        self.manager.current = 'descuentos'
    
    def CambiarListas (self, instance):
        self.manager.current = 'listas'

class RegistroGastos (Screen): 
    def __init__(self, **kwargs): 
        super().__init__(**kwargs)
                                    
        Window.clearcolor = (1, 1, 0.9, 1)
        
        self.layout = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)

        self.intruction_lable = Label (text = "Ingresa tus productos", font_size = '25sp', color = (0,0,0,1))
        self.layout.add_widget(self.intruction_lable)

        self.producto_input = TextInput (hint_text = "Ingrese el articulo", multiline = False, size_hint_y = None, height = 100, font_size= '16sp')
        self.layout.add_widget(self.producto_input)

        self.precio_input = TextInput (hint_text = "Ingrese el precio del articulo", multiline = False, size_hint_y = None, height = 100, input_filter = 'float', font_size = '16sp')
        self.layout.add_widget(self.precio_input)

        self.cantidad_input = TextInput (hint_text = "Ingresa la cantidad de este producto", multiline = False, size_hint_y = None, height = 100, input_filter = 'int', font_size = '16sp')
        self.layout.add_widget(self.cantidad_input)

        boton_agregar = Button (text = "Agregar producto", size_hint = (0.8, None), height = 200, pos_hint = {"center_x":0.5}, background_color = (0,1,0,1))
        boton_agregar.bind(on_press = self.AgregarProducto)
        self.layout.add_widget(boton_agregar)

        self.resultado_label = Label(text = "", color = (0,0,0,1), font_size = '16sp', halign = "center", valign = "middle")
        self.layout.add_widget(self.resultado_label)

        boton_volver = Button(text = "Volver", pos_hint = {"center_x": 0.5}, background_color = (1, 0.7, 0.8, 1))
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
            self.resultado_label.markup = True
            self.resultado_label.text = f"[b]Producto Agregado[/b]"
        except ValueError: 
            self.resultado_label.markup = True
            self.resultado_label.text = f"[b][color=#FF4500]Ingrese un costo valido[/color][/b]"

class VerdurasFrutas (Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        main_layout = FloatLayout()
        
        self.layout = BoxLayout (orientation = 'vertical', padding = 20, spacing = 10 )

        info_Button = Button(text = 'i', size_hint = (0.1,0.05), pos_hint = {'right': 1, 'top':1})
        info_Button.bind (on_release = self.show_info)
        main_layout.add_widget(info_Button)

        insctruction_label = Label (text = "Verduras y Frutas", font_size = '30sp', color = (0,0,0,1))
        self.layout.add_widget(insctruction_label)

        self.producto_input = TextInput (hint_text = "Ingresa el producto", multiline = False, font_size = '16sp', size_hint_y = None, height = 100) 
        self.layout.add_widget(self.producto_input)

        self.precio_por_kilo = TextInput (hint_text = "Ingresa el valor por kilo", multiline = False, font_size = '16sp', size_hint_y = None, height = 100)
        self.layout.add_widget(self.precio_por_kilo)

        self.gramaje_input = TextInput (hint_text = "Ingresa en gramos lo que agarraste", multiline = False, font_size = '16sp', size_hint_y = None, height = 100)
        self.layout.add_widget(self.gramaje_input)

        agregar_button = Button (text = "Agregar producto", size_hint = (0.8, None), height = 200, pos_hint = {"center_x":0.5}, background_color = (0,1,0,1))
        agregar_button.bind(on_press = self.agregar_producto)
        self.layout.add_widget(agregar_button)

        self.resultado_label = Label (text = "", color = (0,0,0,1), font_size = '16sp', halign = "center", valign = "middle")
        self.layout.add_widget(self.resultado_label)
        
        boton_volver = Button (text = "Volver", pos_hint = {"center_x": 0.5}, background_color = (1, 0.7, 0.8, 1))
        boton_volver.bind (on_press= self.volver_registro)
        self.layout.add_widget(boton_volver)

        main_layout.add_widget(self.layout)

        self.add_widget(main_layout)

        self.lista_precios = []

    def show_info(self, instance):
        close_button = Button(text = "Cerrar", size_hint = (1,0.2), on_release= lambda x: popup.dismiss())
        content = BoxLayout(orientation = 'vertical')
        content.add_widget(Label(text = 'Para ingresar el peso de\nla fruta/verdura que agarraste\n\nEjemplo:\n\n • .5 kilos = 500 gramos\n Ingresa los 500.\n • 1 kilo = 1000 gramos.\nIngresa los 1000.', size_hint = (0.7,0.7)))
        content.add_widget(close_button)
        popup = Popup(title = 'informacion', content = content, size_hint =(0.9,0.9))
        popup.open()

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
            self.resultado_label.markup = True
            self.resultado_label.text = f"[b]Producto Agregado[/b]"
        except ValueError: 
            self.resultado_label.markup = True
            self.resultado_label.text = f"[b][color=#FF4500]Ingrese peso o costo valido[/color][/b]"

    def volver_registro(self, instance): 
        self.manager.current = 'inicio'

class ProductosDescuentos (Screen):
        def __init__ (self, **kwargs):
            super().__init__(**kwargs)

            main_layout = FloatLayout()

            self.layout = BoxLayout (orientation = 'vertical', padding = 20, spacing = 10)

            info_Button = Button(text = 'i', size_hint = (0.1,0.05), pos_hint = {'right': 1, 'top': 1})
            info_Button.bind (on_release = self.show_info)
            main_layout.add_widget(info_Button)

            self.intruction_label = Label(text = "Ingresa tus productos",font_size = '25sp', color = (0,0,0,1))
            self.layout.add_widget(self.intruction_label)

            self.producto_input = TextInput(hint_text = "Ingrese tu articulo", multiline = False, size_hint_y = None, height = 100, font_size = '16sp')
            self.layout.add_widget(self.producto_input)

            self.precio_input = TextInput(hint_text = "Ingresa el costo del articulo", multiline = False, size_hint_y = None, height = 100, font_size = '16sp')
            self.layout.add_widget(self.precio_input)

            self.descuento_input = TextInput(hint_text = "Ingresa cuanto descuento tiene", multiline = False, size_hint_y = None, height = 100, font_size = '16sp')
            self.layout.add_widget(self.descuento_input)

            self.cantidad_input = (TextInput(hint_text = "Ingresa la cantidad de productos que llevarás", multiline = False, size_hint_y = None, height = 100, font_size = '16sp'))
            self.layout.add_widget(self.cantidad_input)

            boton_agragar = Button (text = "Agregar producto", size_hint = (0.8, None), height = 200, pos_hint = {"center_x": 0.5}, background_color = (0,1,0,1))
            boton_agragar.bind (on_press = self.AgregarProducto)
            self.layout.add_widget(boton_agragar)

            self.resultado_label = Label(text = "", color = (0,0,0,1), font_size = '16sp', halign = "center", valign = "middle")
            self.layout.add_widget(self.resultado_label)

            boton_volver = Button (text = "Volver", pos_hint = {"center_x": 0.5}, background_color = (1, 0.7, 0.8, 1))
            boton_volver.bind(on_press = self.volver_registro)
            self.layout.add_widget(boton_volver)

            main_layout.add_widget(self.layout)

            self.add_widget(main_layout)

            self.lista_precios = []

        def show_info(self, instance):
            close_button = Button(text = "Cerrar", size_hint = (1,0.2), on_release= lambda x: popup.dismiss())
            content = BoxLayout(orientation = 'vertical')
            content.add_widget(Label(text = 'Para ingresar el descuento\nde lo que agarraste\n\nEjemplo:\n\n • 30% --> ingresa 30 \n • 50% --> ingresa 50', size_hint = (0.7,0.7)))
            content.add_widget(close_button)
            popup = Popup(title = 'informacion', content = content, size_hint =(0.7,0.6))
            popup.open()

        def volver_registro (self, instance): 
            self.manager.current = 'inicio'

        def AgregarProducto (self, instance):
            producto = self.producto_input.text
            try: 
                cantidad = int(self.cantidad_input.text)
                precio = float(self.precio_input.text)
                descuento = float(self.descuento_input.text)
                descuento = ((descuento / 100) - 1) * -1
                precio = precio * descuento
                total_precio = precio * cantidad
                self.lista_precios.append ((producto, total_precio))

                self.producto_input.text = ""
                self.precio_input.text = ""
                self.descuento_input.text = ""
                self.cantidad_input.text = ""
                self.resultado_label.markup = True
                self.resultado_label.text = f"[b]Producto agregado[/b]"
            except ValueError: 
                self.resultado_label.markup = True
                self.resultado_label.text = f"[b][color=#FF4500]Ingrese un costo valido[/color][/b]"



class PaginaListas(Screen): 
    def __init__(self, **k): 
        super().__init__(**k)

        self.main_layout = FloatLayout()

        self.layout = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)

        info_button = Button(text = 'i', size_hint = (0.1,0.05), pos_hint = {'right':1, 'top':1})
        info_button.bind (on_release = self.show_info)
        self.main_layout.add_widget(info_button)

        instruction_label = Label (text = "Ve y Edita tus listas", font_size = '30sp', color = (0,0,0,1))
        self.layout.add_widget(instruction_label)

        boton_total = Button(text = "Total", pos_hint = {"center_x": 0.5}, background_color = (0.5, 1, 0, 1))
        boton_total.bind (on_press = self.CambiarTotal) 
        self.layout.add_widget(boton_total)

        boton_borrar = Button(text = "Borrar Productos", pos_hint = {"center_x": 0.5}, background_color = (0.5,1,0,1))
        boton_borrar.bind (on_press = self.CambiarBorrar)
        self.layout.add_widget(boton_borrar)

        boton_VerListas = Button(text = "Todas las listas",pos_hint = {"center_x":0.5}, background_color = (0.5,1,0,1))
        boton_VerListas.bind(on_press = self.CambiarAllListas)
        self.layout.add_widget(boton_VerListas)

        boton_volver = Button (text = 'Volver', pos_hint = {"center_x":0.5}, background_color = (1, 0.7, 0.8, 1))
        boton_volver.bind (on_press = self.volver_registro)
        self.layout.add_widget(boton_volver)
        
        self.main_layout.add_widget(self.layout)

        self.add_widget(self.main_layout)
    
    def show_info(self, instance):
        self.close_button = Button(text = "Cerrar", size_hint = (1,0.2), on_release = lambda x: popup.dismiss())
        content = BoxLayout(orientation = 'vertical')
        content.add_widget(Label(text = 'En esta pagina puedes ver\ny editar tu lista, ademas\npuedes guardar tu lista\ny ver tus listas\npasadas.', size_hint = (1,0.8)))
        content.add_widget(self.close_button)
        popup = Popup(title = 'Informacion', content = content, size_hint = (0.9,0.9))
        popup.open()

    def CambiarTotal (self, instance):
        self.manager.current = 'total'

    def CambiarBorrar (self, instance):
        self.manager.current = 'borrar'

    def CambiarAllListas(self, instance):
        self.manager.current = 'all'

    def volver_registro (self, instance):
        self.manager.current = 'inicio'

    
class ListaTotal(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        layout = BoxLayout (orientation = 'vertical', padding = 20, spacing = 10)

        instruction_label = Label(text = "Ve y Guarda tus listas", font_size = '20sp', color = (0,0,0,1))
        layout.add_widget(instruction_label)

        self.scroll_view = ScrollView (size_hint = (1, None), size = (Window.width, 300))
        self.productos_layout = GridLayout (cols = 1, spacing = 15, size_hint_y = 10)
        self.productos_layout.bind(minimum_height = self.productos_layout.setter ('height'))
        self.scroll_view.add_widget(self.productos_layout)
        layout.add_widget(self.scroll_view)

        boton_calcular_total = Button (text = "Total", size_hint = (0.8, None), height = 300, pos_hint = {"center_x":0.5}, background_color =(0.6, 0.8, 1, 1))
        boton_calcular_total.bind(on_press = self.calcular_total)
        layout.add_widget(boton_calcular_total)

        self.total_label = Label(text = "")
        layout.add_widget(self.total_label)

        self.lista_input = TextInput(hint_text = "Escribe el nombre de la lista", size_hint_y = None)
        layout.add_widget(self.lista_input)

        boton_guardar_lista = Button (text = "Guardar Lista", size_hint = (0.8,None), height = 300, pos_hint = {"center_x": 0.5}, background_color = (0.6,0.8,1,1))
        boton_guardar_lista.bind(on_press = self.confirmar_lista)
        layout.add_widget(boton_guardar_lista)

        self.guardar_label = Label(text = "", color = (0,0,0,1), font_size = '16sp', halign = "center", valign = "middle")
        layout.add_widget(self.guardar_label)

        boton_volver = Button(text = "Volver", pos_hint = {"center_x": 0.5}, background_color = (1, 0.7, 0.8, 1))
        boton_volver.bind (on_press = self.volver_registro) 
        layout.add_widget(boton_volver)

        self.add_widget(layout)

    def volver_registro (self, instance):
        self.manager.current = 'listas'

    def confirmar_lista(self, instance):
        close_button = Button(text = "Cancelar",pos_hint = {"center_x":0.5}, height = 300, background_color = (1,0,0,1), size_hint = (0.8,None), on_release = lambda x: popup.dismiss())
        content = BoxLayout(orientation = 'vertical')
        boton_comfirmar = Button(text = "Confirmar", height = 300,pos_hint = {"center_x":0.5}, size_hint = (0.8,None), background_color = (0,1,0,1), on_release = lambda x: popup.dismiss())
        boton_comfirmar.bind(on_press = self.guardar_lista)
        content.add_widget(boton_comfirmar)
        content.add_widget(close_button)
        popup = Popup(content = content, size_hint = (0.9,0.4), title = "Deseas Guardar tu lista")
        popup.open()

    def guardar_lista(self, instace):
        registro_gastos = App.get_running_app().root.get_screen('registro').lista_precios
        verduras_futas = App.get_running_app().root.get_screen('verduras').lista_precios
        productos_descuentos = App.get_running_app().root.get_screen('descuentos').lista_precios
        all_products = registro_gastos + verduras_futas + productos_descuentos

        list_name = self.lista_input.text.strip()

        if not list_name: 
            self.guardar_label.markup = True
            self.guardar_label = f"[b][color=#FF4500]Error, ingrese nombre[/color][/b]"
            return 
        
        if storage.exists("listas"):
            listas_guardadas = storage.get("listas")["items"]
        else: 
            listas_guardadas = {}
        
        if list_name in listas_guardadas:
            self.guardar_label.markup = True
            self.guardar_label.text = f"[b][color=#FF4500]Error[/color][/b]\n"f"[color=#000000]Ya existe una lista con ese nombre[/color]"
            return 

        listas_guardadas[list_name] = all_products
        storage.put ("listas", items = listas_guardadas)
        
        self.lista_input.text = ""
        self.guardar_label.text = ""
        self.guardar_label.markup = True
        self.guardar_label.text = f"[b][color=#006400]Lista guardada con éxito![/color][/b]\n"f"[color=#000000]{list_name}[/color]"

    def calcular_total(self, instance):
        registro_gastos = App.get_running_app().root.get_screen('registro').lista_precios
        verduras_futas = App.get_running_app().root.get_screen('verduras').lista_precios
        productos_descuentos = App.get_running_app().root.get_screen('descuentos').lista_precios
        all_products = registro_gastos + verduras_futas + productos_descuentos
        total = sum(precio for nombre, precio in all_products)
        self.total_label.markup = True
        self.total_label.text = f"[b][color=#000000]Total[/b][/color]\n"f"[b][color=#000000]${total:.2f}[/b][/color]"
        self.total_label.color = (0,0,0,1)

    def on_enter(self):
        self.productos_layout.clear_widgets()
        registro_gastos = App.get_running_app().root.get_screen('registro').lista_precios
        verduras_futas = App.get_running_app().root.get_screen('verduras').lista_precios
        productos_descuentos = App.get_running_app().root.get_screen('descuentos').lista_precios
        all_products = registro_gastos + verduras_futas + productos_descuentos
        for nombre, precio in all_products: 
            etiqueta = Label(text = f"{nombre} - ${precio:.2f}", size_hint_y = None, height = 40)
            self.productos_layout.add_widget(etiqueta)
            etiqueta.color = (0,0,0,1)


class BorrarProductos (Screen):    
    def __init__(self, **kw):
        super().__init__(**kw)

        self.layout = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)

        self.instruction_label = Label (text = "Borra productos de tu lista", font_size = '20sp', color = (0,0,0,1))
        self.layout.add_widget(self.instruction_label)

        self.scroll_view = ScrollView (size_hint = (1, None), size = (Window.width, 300))
        self.productos_layout = GridLayout (cols = 1, spacing = 15, size_hint_y = 10)
        self.productos_layout.bind(minimum_height = self.productos_layout.setter ('height'))
        self.scroll_view.add_widget(self.productos_layout)
        self.layout.add_widget(self.scroll_view)

        self.producto_lista_input = TextInput(hint_text = "Ingresa el numero del producto", multiline = False, font_size = '16sp', size_hint_y = None, height = 100)
        self.layout.add_widget(self.producto_lista_input)

        boton_borrar_articulo = Button(text = "Borrar", pos_hint = {"center_x":0.5},size_hint = (0.5, None), height = 150, background_color = (1,0,0,1))
        boton_borrar_articulo.bind(on_press = self.borrar_producto)
        self.layout.add_widget(boton_borrar_articulo)

        self.label_borrado = Label (text = "",color = (0,0,0,1), font_size = '16sp', halign = "center", valign = "middle")
        self.layout.add_widget(self.label_borrado)

        boton_volver = Button(text = "Volver", pos_hint = {"center_x": 0.5}, background_color = (1, 0.7, 0.8, 1))
        boton_volver.bind (on_press = self.volver_registro) 
        self.layout.add_widget(boton_volver)

        self.add_widget(self.layout)

    def on_enter(self):
        self.productos_layout.clear_widgets()
        registro_gastos = App.get_running_app().root.get_screen('registro').lista_precios
        verduras_futas = App.get_running_app().root.get_screen('verduras').lista_precios
        productos_descuentos = App.get_running_app().root.get_screen('descuentos').lista_precios
        all_products = registro_gastos + verduras_futas + productos_descuentos
        i = 0
        for nombre, precio in all_products: 
            i +=1
            etiqueta = Label(text = f"[{i}]  {nombre} - ${precio:.2f}", size_hint_y = None, height = 40)
            self.productos_layout.add_widget(etiqueta)
            etiqueta.color = (0,0,0,1)

    def borrar_producto(self, instance):
        try: 
            producto = int(self.producto_lista_input.text) - 1
            registro_gastos = App.get_running_app().root.get_screen('registro').lista_precios
            verduras_futas = App.get_running_app().root.get_screen('verduras').lista_precios
            productos_descuentos = App.get_running_app().root.get_screen('descuentos').lista_precios
            self.lista = registro_gastos + verduras_futas + productos_descuentos

            if 0 <= producto < len (self.lista[0]):    

                if producto < len (registro_gastos): 
                    producto_borrado = registro_gastos.pop (producto)

                elif producto < len (registro_gastos) + len (verduras_futas): 
                    producto_borrado = verduras_futas.pop(producto - len(registro_gastos))
                
                else: 
                    producto_borrado = productos_descuentos.pop (producto - len(registro_gastos) - len(verduras_futas))

                nombre_producto = (producto_borrado[0] if isinstance(producto_borrado, tuple) else str (producto_borrado))

                self.productos_layout.clear_widgets()
                self.on_enter()

                self.label_borrado.markup = True
                self.label_borrado.text = f"[b][color=#FF4500]¡Producto eliminado con éxito![/color][/b]\n"f"[color=#000000]{nombre_producto}[/color]"

            else: 
                self.label_borrado.markup = True
                self.label_borrado.text = f"[b][color=#FF4500]Ingrese un numero valido[/color][/b]"

        except ValueError: 
            self.label_borrado.markup = True
            self.label_borrado.text = f"[b][color=#FF4500]Ingrese un numero valido[/color][/b]"

        self.producto_lista_input.text = ""

    def volver_registro (self, instance):
        self.manager.current = 'listas'


class ListasGuardadas(Screen):
    def __init__(self, **k):
        super().__init__(**k)

        self.layout = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)

        instruction_label = Label(text = "Ve tus listas pasadas", font_size = '25sp', color = (0,0,0,1))
        self.layout.add_widget(instruction_label)

        self.scroll_view = ScrollView(size_hint = (1, None), size = (Window.width, 250))
        self.listas_layout = GridLayout (cols = 1, spacing = 15, size_hint_y = 10)
        self.listas_layout.bind(minimum_height = self.scroll_view.setter('height'))
        self.scroll_view.add_widget(self.listas_layout)
        self.layout.add_widget(self.scroll_view)

        self.selection_input = TextInput(hint_text = "Ingrese el numero de la lista que desea ver", multiline = False, font_size = '16sp', size_hint_y = None, height = 100)
        self.layout.add_widget(self.selection_input)

        boton_seleccionar = Button(text = "Aceptar", pos_hint = {"center_x": 0.5}, size_hint = (0.8, None), height = 200, background_color = (0.0, 0.749, 1.0))
        boton_seleccionar.bind (on_press = self.seleccionar_listas)
        self.layout.add_widget(boton_seleccionar)

        self.detalle_scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, 250))
        self.productos_pasados = GridLayout(cols=1, spacing=15, size_hint_y=None)
        self.productos_pasados.bind(minimum_height=self.productos_pasados.setter('height'))
        self.detalle_scroll_view.add_widget(self.productos_pasados)
        self.layout.add_widget(self.detalle_scroll_view)        

        self.lista_borrado = TextInput (hint_text = "Ingresa el numero de la lista que desea borrar", multiline = False, font_size = '16sp', size_hint_y = None, height = 100)
        self.layout.add_widget(self.lista_borrado)

        boton_borrar_lista = Button(text = "Borrar",pos_hint = {"center_x": 0.5}, size_hint = (0.8, None), height = 200, background_color = (0.0, 0.749, 1.0))
        boton_borrar_lista.bind (on_press = self.borrar_lista)
        self.layout.add_widget(boton_borrar_lista)

        self.label_borrado = Label (text = "", color = (0,0,0,1), font_size = '16sp', halign = "center", valign = "middle")
        self.layout.add_widget(self.label_borrado)

        boton_volver = Button(text = "Volver", pos_hint = {"center_x": 0.5}, background_color = (1,0.7,0.8,1))
        boton_volver.bind(on_press = self.volver_registro)
        self.layout.add_widget(boton_volver)

        self.add_widget(self.layout)
    
    def on_enter(self):

        self.listas_layout.clear_widgets()

        if storage.exists("listas"):
            listas_guardadas = storage.get("listas")["items"]
            for idx, list_name in enumerate(listas_guardadas.keys(), start = 1):
                etiqueta = Label(text = f"[{idx}] {list_name}", size_hint_y = None, height = 40, color = (0,0,0,1))
                self.listas_layout.add_widget(etiqueta)
        else: 
            etiqueta = Label(text = "No hay listas guardadas aun", size_hint_y = None, height = 40, color = (0,0,0,1))
            self.listas_layout.add_widget(etiqueta)

    def seleccionar_listas(self, instance):
        self.productos_pasados.clear_widgets()

        if storage.exists("listas"):
            listas_guardadas = storage.get("listas")["items"]

            try:
                seleccion = int(self.selection_input.text.strip()) - 1
                if seleccion < 0 or seleccion >= len(listas_guardadas):
                    detalles = Label(markup = True, text=f"[b][color==#FF4500] Número de lista no válido[/color][/b]", size_hint_y=None, height=40)
                    self.productos_pasados.add_widget(detalles)
                    return

                list_name = list(listas_guardadas.keys())[seleccion]
                items = listas_guardadas[list_name]
                total = 0
                for nombre, precio in items:
                    total += precio

                for nombre, precio in items:
                    detalles = Label( text=f"Lista: {list_name}\nTotal: {total}\n\n" + "\n".join(f"{nombre} - ${precio:.2f}"), size_hint_y=None, height=40, color = (0,0,0,1))

                    #detalles = Label(markup = True, text=f"[b][color=#000000]Lista: {list_name}\n[/color][/b]" + "\n".join(f"[b][color=#000000]{nombre} - ${precio:.2f}[/color][/b]"), size_hint_y=None, height=40)
                    self.productos_pasados.add_widget(detalles)

            except ValueError:
                detalles = Label(markup = True, text=f"[b][color==#FF4500] Número de lista no válido[/color][/b]", size_hint_y=None, height=40)
                self.productos_pasados.add_widget(detalles)
        else:
            detalles = Label(markup = True, text=f"[b][color==#FF4500] No hay listas guardadas[/color][/b]", size_hint_y=None, height=40)
            self.productos_pasados.add_widget(detalles)

    def borrar_lista(self, instance):

        if not storage.exists("listas"):
            self.label_borrado.markup = True
            self.label_borrado.text = f"[b][color=#FF4500]No hay listas guardadas[/color][/b]"
            return 

        listas_guardadas = storage.get("listas")["items"]

        try: 
            seleccion = int(self. lista_borrado.text.strip()) -1
            if seleccion < 0 or seleccion >= len(listas_guardadas):
                self.label_borrado.markup = True
                self.label_borrado.text = f"[b][color=#FF4500]Ingrese un numero valido[/color][/b]"
                return 
            
            
            list_name = list(listas_guardadas.keys())[seleccion]
            del listas_guardadas[list_name]

            storage.put("listas", items = listas_guardadas)

            self.label_borrado.markup = True

            self.label_borrado.text = f"[b][color=#FF4500]Lista eliminado con éxito![/color][/b]\n"f"[color=#000000]{list_name}[/color]"
            self.on_enter()
        
        except ValueError: 
            self.label_borrado.markup = True
            self.label_borrado.text = f"[b][color=#FF4500]Ingrese un numero valido[/color][/b]"
        finally: 
            self.lista_borrado.text = ""
                
    def volver_registro(self, instance):
        self.manager.current = 'listas' 
   


class ListaSuper (App): 
    def build(self): 

        sm = ScreenManager()
        sm.add_widget(PantallaInicio(name = 'inicio'))
        sm.add_widget(RegistroGastos(name = 'registro'))
        sm.add_widget(VerdurasFrutas(name = 'verduras'))
        sm.add_widget(ProductosDescuentos(name = 'descuentos'))
        sm.add_widget(PaginaListas(name = 'listas'))
        sm.add_widget(ListaTotal (name = 'total'))
        sm.add_widget(BorrarProductos(name = 'borrar'))
        sm.add_widget(ListasGuardadas(name = 'all'))
        return sm
    
ListaSuper().run()