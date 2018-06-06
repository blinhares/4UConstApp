import kivy
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen #para funcionar o gerenciamento de telas
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.factory import Factory

Window.softinput_mode = 'below_target' #PARA QUE O TECLADO N ESCONDA OS INPUT
Window.clearcolor =[1,1,1,1] #ALTERA A COR DE FUNDO PARA BRANCO


import diariodebordo #IMPORTAR CODIGO PARA DIARIO DE BORDO


class MenuP(Screen): #cria a classe do Menu Principal
    pass

class AvisoDb(Popup):
    pass

class GerTela(ScreenManager):
    def __init__(self, **kwargs):
        super(GerTela, self).__init__(**kwargs)


class MenuApp(App):
    def build(self):
        return GerTela()

janela = MenuApp()
janela.run()