
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.graphics import Color, Rectangle


class NumberConverterApp(App):
    def build(self):
        self.title = 'Number System Converter'
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Set the background color to white
        with self.layout.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)

        self.input_text = TextInput(hint_text="Enter a number", background_color=(1, 1, 1, 0.8),
                                    foreground_color=(0, 0, 0, 1))
        self.output_label = Label(text="Converted number will appear here", color=(0, 0, 0, 1))

        self.converter_spinner = Spinner(text='From', values=('Binary', 'Octal', 'Decimal', 'Hexadecimal'),
                                         background_color=(1, 1, 1, 0.8))
        self.result_spinner = Spinner(text='To', values=('Binary', 'Octal', 'Decimal', 'Hexadecimal'),
                                      background_color=(1, 1, 1, 0.8))

        self.layout.add_widget(self.input_text)
        self.layout.add_widget(self.converter_spinner)
        self.layout.add_widget(self.result_spinner)
        self.layout.add_widget(self.output_label)

        self.input_text.bind(text=self.on_input_change)
        self.converter_spinner.bind(text=self.on_input_change)
        self.result_spinner.bind(text=self.on_input_change)

        return self.layout

    def on_input_change(self, instance, value):
        input_text = self.input_text.text.strip()
        if not input_text:
            self.output_label.text = "Converted number will appear here"
            return

        try:
            if self.converter_spinner.text == 'Binary':
                input_base = 2
                self.update_colors((0, 0.5, 0), (0, 0, 0))
            elif self.converter_spinner.text == 'Octal':
                input_base = 8
                self.update_colors((0.1, 0.3, 0.5), (1, 1, 1))
            elif self.converter_spinner.text == 'Decimal':
                input_base = 10
                self.update_colors((0, 0, 0), (1, 1, 1))
            elif self.converter_spinner.text == 'Hexadecimal':
                input_base = 16
                self.update_colors((0.4, 0.2, 0.8), (1, 1, 1))

            decimal = int(input_text, input_base)

            if self.result_spinner.text == 'Binary':
                self.output_label.text = f"Binary: {bin(decimal)[2:]}"
            elif self.result_spinner.text == 'Octal':
                self.output_label.text = f"Octal: {oct(decimal)[2:]}"
            elif self.result_spinner.text == 'Decimal':
                self.output_label.text = f"Decimal: {decimal}"
            elif self.result_spinner.text == 'Hexadecimal':
                self.output_label.text = f"Hexadecimal: {hex(decimal)[2:]}"
        except ValueError:
            self.output_label.text = "Invalid input"

    def update_colors(self, background_color, text_color):
        # Update background and text colors
        self.layout.canvas.before.clear()
        with self.layout.canvas.before:
            Color(*background_color)
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)
        self.input_text.background_color = background_color + (0.8,)
        self.input_text.foreground_color = text_color + (1,)
        self.output_label.color = text_color + (1,)


if __name__ == '__main__':
    NumberConverterApp().run()


