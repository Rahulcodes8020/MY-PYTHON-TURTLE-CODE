from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
import webbrowser

class PhoneApp(App):
    def build(self):
        
        layout = BoxLayout(orientation='vertical')
        
        
        scroll_view = ScrollView(size_hint=(1, None), height=400)
        
        
        grid_layout = GridLayout(cols=3, padding=10, spacing=10, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        
        apps = {
            "YouTube": "https://www.youtube.com",
            "Facebook": "https://www.facebook.com",
            "Twitter": "https://www.twitter.com",
            "Google": "https://www.google.com",
            "Instagram": "https://www.instagram.com",
            "Snapchat" : "https://www.Snapchat.com",
            "Calllog" : "https://www.Calllog.com",
            "Contact" : "https://www.Contact.com",
            "Whatsapp" : "https://www.Whatsapp.com"
            
        }

        
        for app_name, url in apps.items():
            button = Button(text=app_name, size_hint_y=None, height=50)
            button.bind(on_release=lambda btn, url=url: self.open_app(url))
            grid_layout.add_widget(button)

        scroll_view.add_widget(grid_layout)
        layout.add_widget(scroll_view)
        
        return layout

    def open_app(self, url):
        webbrowser.open(url)  


if __name__ == "__main__":
    PhoneApp().run()
