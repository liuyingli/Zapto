#! /usr/bin/python

#/*********************************************************************************/
#/*                  Sandy Client - Urbano Gutierrez - 076                        */
#/*********************************************************************************/

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
import requests

kv = '''
<SplashScreen>:
    BoxLayout:
        size_hint: 1, 1
        canvas:
            Color:
                rgba: .5, .2 , .3, 1
            Rectangle:
                size: self.size

        Label:
            markup: True
            text: '[size= 140][b]SANDY[/b][/size]'

<LoginScreen>
    FloatLayout:
        canvas:
            Color:
                rgb: 0, 0, 0
            Rectangle:    
                size: self.size
                pos: self.pos   
        Widget:
            size: min(root.size), min(root.size)/4
            size_hint: None, None
            pos_hint: {'center_x': .5, 'center_y': .5}
            canvas:
                Color:
                    rgba: .5, .2 , .3, 1
                Rectangle:    
                    size: self.size
                    pos: self.pos
        TextInput:
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: None, None
            size: 400, 60
            password: True
            font_size: 40
            id: text_input
            text: ''
            center_y: root.height / 3
            center_x: root.width / 2
            multiline: False
                    
        Label:
            text: 'Introduce tu codigo'
           
            pos_hint: {'center_x': .5, 'center_y': .8}
            size: 150, 50
            font_size: 40
            id: text_info
                        
        Button:
            size_hint: None, None
            text: 'Log In'
            font_size: 40
            size: 250, 80
            pos_hint: {'center_x': .5, 'center_y': .1}
            on_release: root.callmodule() 

<MainScreen>:
    FloatLayout:
        size_hint: 1, 1
        canvas:
            Color:
                rgb: (0.097, 0.097, 0.097)
            Rectangle:
                size: self.size

        Image:
            pos_hint: {'center_x': .5, 'center_y': .5}
            source: 'main.png' 



'''
Builder.load_string(kv)

def server (endpoint, data=False): # Data = DIC
    url = "http://0.0.0.0:5000/" + endpoint

    if data:
        print "Working"
        r = requests.get(url, params=data)
        return r.json()

    else:
        print "Working without data"
        r = requests.get(url)
        return r.json()

def login(passw):
    data =  server("login",{"user":"Sandy_App", "key":passw})
    return data["Login"]

class SplashScreen(Screen):
    def splashOUT(dt):
        sm.current = 'login'
    Clock.schedule_once(splashOUT, 4)

class LoginScreen(Screen): 

    def callmodule(self):
        
        self.text_input = self.ids.text_input.text 
        text = self.text_input

        #Comando: <comando> <[variable]>
        if login(text):
            sm.current = 'main'

        else:
            self.text_info = "[Nothing Happens]"
            self.ids.text_info.text = self.text_info

class MainScreen(Screen):
    def splashOUT(dt):
        sm.current = 'login'
    Clock.schedule_once(splashOUT, 4)

sm = ScreenManager()
sm.add_widget(SplashScreen(name='splash'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(MainScreen(name='main'))

class Sandy(App):
    def build(self):
        return sm

Sandy().run()