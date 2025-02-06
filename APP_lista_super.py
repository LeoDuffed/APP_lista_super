# Este es un ejemplo de como se usa kivy.
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 

class FirstLista(App):
    def build (self):
        layout = BoxLayout(orientation='vertical')

        self.instruction_label = Label (text= 'Ingresa el nombre del producto y su costo')
        layout.add_widget(self.instruction_label)

        self.producto_input = TextInput(hint_text= 'Nombre del producto')
        layout.add_widget(self.producto_input)

        self.costo_input = TextInput(hint_text= 'Costo del producto que acabas de ingresar')
        layout.add_widget(self.costo_input)

        agregar_button = Button (text = 'Agregar Producto')
        agregar_button.bind(on_press = self.agregar_producto)
        layout.add_widget(agregar_button)

        self.suma_label = Label (text = "Suma total: 0 ")
        layout.add_widget(self.suma_label)

        self.suma_total = 0

        return layout
    
    def agregar_producto(self, instance): 
        try: 
            producto = self.producto_input.text
            costo = float(self.costo_input.text)
            self.suma_total += costo
            self.suma_label.text = f"Suma total: {self.suma_total}"

            self.producto_input.text = ""
            self.costo_input.text= ""
        except ValueError:
            self.instruction_label.text = "Por favor ingrese un costo valido."

if __name__ == '__main__':
    FirstLista().run()

#compilando