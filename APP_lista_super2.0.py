from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ListaSuperApp(App):
    def build(self):
        # Crear la interfaz principal
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Etiqueta para mostrar instrucciones
        instruction_label = Label(text="Ingrese el nombre del producto y su costo", font_size='18sp')
        layout.add_widget(instruction_label)

        # Campo de texto para el nombre del producto
        self.producto_input = TextInput(hint_text="Nombre del producto", font_size='16sp', multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.producto_input)

        # Campo de texto para el costo del producto
        self.costo_input = TextInput(hint_text="Costo del producto", font_size='16sp', multiline=False, input_filter='float', size_hint_y=None, height=40)
        layout.add_widget(self.costo_input)

        # Botón para agregar producto
        agregar_button = Button(text="Agregar Producto", font_size='18sp', background_color=(0, 1, 0, 1))
        agregar_button.bind(on_press=self.agregar_producto)
        layout.add_widget(agregar_button)

        # Etiqueta para mostrar la suma total
        self.suma_label = Label(text="Suma total: 0", font_size='20sp', color=(1, 0, 0, 1))
        layout.add_widget(self.suma_label)

        # ScrollView para la lista de productos
        scroll_view = ScrollView(size_hint=(1, None), height=200)
        self.lista_productos = BoxLayout(orientation='vertical', size_hint_y=None)
        self.lista_productos.bind(minimum_height=self.lista_productos.setter('height'))
        scroll_view.add_widget(self.lista_productos)
        layout.add_widget(scroll_view)

        # Inicializa la suma
        self.suma_total = 0

        return layout

    def agregar_producto(self, instance):
        # Obtener valores de los campos
        producto = self.producto_input.text
        try:
            costo = float(self.costo_input.text)
            self.suma_total += costo
            self.suma_label.text = f"Suma total: {self.suma_total}"

            # Crear una nueva etiqueta para el producto y agregarla a la lista
            producto_label = Label(text=f"{producto}: ${costo}", font_size='16sp', size_hint_y=None, height=30)
            self.lista_productos.add_widget(producto_label)

            # Limpia los campos
            self.producto_input.text = ""
            self.costo_input.text = ""
        except ValueError:
            # En caso de un valor inválido
            self.suma_label.text = "Por favor ingrese un costo válido"

# Ejecutar la aplicación
if __name__ == '__main__':
    ListaSuperApp().run()
