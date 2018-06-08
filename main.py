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
from plyer import email

Window.softinput_mode = 'below_target' #PARA QUE O TECLADO N ESCONDA OS INPUT
Window.clearcolor =[1,1,1,1] #ALTERA A COR DE FUNDO PARA BRANCO


import diarbordpycode #IMPORTAR CODIGO PARA DIARIO DE BORDO


class MenuP(Screen): #cria a classe do Menu Principal
    #Enviar dados por email
    def enviardados(self):
        try:
            with open('dadosdb.csv', 'r') as f:
                destinatario = "brunobarbosa@quatrou.com.br"
                assunto = "Diario de Bordo"
                corpodoemail = ""
                for linha in f:
                    print(linha)
                    corpodoemail = corpodoemail + linha
                print(corpodoemail)
                limparquivo = open('dadosdb.csv', 'w')
                email.send(recipient=destinatario,
                   subject=assunto,
                   text=corpodoemail)
        except IOError:
            popup = Popup(title='Aviso', content=Label(text='Nao ha dados para enviar'),
                          auto_dismiss=True, size_hint=(.5, .5))
            popup.open()

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