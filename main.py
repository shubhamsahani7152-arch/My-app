from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class JankariApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.title_label = Label(text="Apni Jankari App", font_size=24, size_hint=(1, 0.2))
        layout.add_widget(self.title_label)
        
        self.user_input = TextInput(text='', hint_text='Yahan likho kya janna hai...', multiline=False, size_hint=(1, 0.2))
        layout.add_widget(self.user_input)
        
        self.search_btn = Button(text='Jankari Khojo', size_hint=(1, 0.2), background_color=(0.1, 0.6, 0.8, 1))
        self.search_btn.bind(on_press=self.get_info)
        layout.add_widget(self.search_btn)
        
        self.result_label = Label(text='Yahan jankari aayegi...', font_size=18, size_hint=(1, 0.4))
        layout.add_widget(self.result_label)
        
        return layout

    def get_info(self, instance):
        query = self.user_input.text.lower()
        if not query:
            self.result_label.text = "Pehle kuch type toh karo bhai!"
            return
            
        if "india" in query:
            self.result_label.text = "India ek desh hai jo Asia mein hai. Iski rajdhani New Delhi hai."
        elif "python" in query:
            self.result_label.text = "Python ek aasaan aur powerful programming language hai."
        elif "kivy" in query:
            self.result_label.text = "Kivy ek Python library hai jisse mobile apps banate hain."
        else:
            self.result_label.text = f"'{query}' ke baare mein jankari jald hi update ki jayegi!"

if __name__ == '__main__':
    JankariApp().run()

