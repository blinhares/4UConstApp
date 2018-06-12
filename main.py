import kivy
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen #para funcionar o gerenciamento de telas
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.factory import Factory
from plyer import email


#Coloca teclado abaixo da entrada e muda fundo para branco
Window.softinput_mode = 'below_target'
Window.clearcolor =[1,1,1,1]

class GerTela(ScreenManager):
    def __init__(self, **kwargs):
        super(GerTela, self).__init__(**kwargs)

class MenuP(Screen):
    pass

class DiarBord(Screen):
    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.voltar)
    def voltar (sel,window, key,*args):
        #SE A TECLA FOR esc ENTAO
        if key == 27:
            App.get_running_app().root.current = "mp"
        return True
    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.voltar)
    def ver_entr(self,idn,texpadr):
        if self.ids[idn].text == texpadr:
            self.ids[idn].text = ""
        else:
            if self.ids[idn].text == "":
                self.ids[idn].text = texpadr

    legenda = ['Obra', 'Equipe', 'Dia', 'Mes', 'Ano',
               'Hora', 'Minutos', 'Nome', 'Placa', 'Obs']
    dadopadrao = ['Escolha Uma Obra', 'Escolha Uma Equipe', 'Escolha o dia', 'Escolha o Mes', 'Escolha o Ano',
                  'Insira a Hora', 'Insira os Minutos', 'Ex: Pedro', 'Ex: ABC1423', 'Ex: Deslocamento a Torre 05']
    def verificar(self):
        dpad = self.dadopadrao
        i = 1
        contador = 0
        while i < 11 :
            if dpad[i - 1].find(self.ids['db'+str(i)].text) >= 0:
                self.ids['db' + str(i)].color=(1,0,0,1)
                contador = contador + 1
            else:
                self.ids['db' + str(i)].color = (1, 1, 1, 1)
            i = i +1
        if dpad[i - 2].find(self.ids['db' + str(i - 1)].text) >= 0:
            self.ids['db' + str(i - 1)].text = "Sem Comentarios"
        contador = contador - 1
        if contador > 0:
            popup = Popup(title='Aviso', content=Label(text='Dados Incompletos.\nFavor preencher todos os campos.'),
                          auto_dismiss=True, size_hint=(1, .5))
            popup.open()
        else:
            self.salvar_dados()
            self.limp_dados()

    def salvar_dados(self):
        store = JsonStore('4u.json')
        dados = {}
        i = 0
        while i < len(self.legenda):
            if self.dadopadrao[i].find(self.ids['db' + str(i + 1)].text) >= 0:
                dados[self.legenda[i]] = '-'
            else:
                dados[self.legenda[i]] = self.ids['db' + str(i + 1)].text
            i = i + 1
        #CRIA ID DE SALVAMENTO#
        idsalv = '#DB#' + dados['Dia'] + dados['Mes'] + dados['Hora']
        store[idsalv]=dados
        popup = Popup(title='Aviso', content=Label(text='Dados Salvos'),
                      auto_dismiss=True, size_hint=(1, .5))
        popup.open()
    def limp_dados(self):
        i = 1
        contador = 0
        while i < 11:
            self.ids['db' + str(i)].text = self.dadopadrao[i - 1]
            i = i + 1
    def env_email(self):
        corpemail = ""
        for dado in self.dadopadrao:
            corpemail = corpemail + dado + ":"
        corpemail = corpemail + "\n"
        i = 1
        while i < 11:
            corpemail = corpemail + self.ids['db' + str(i)].text + ":"
            i = i + 1
        corpemail = corpemail + "\n"
        print(corpemail)
        email.send(recipient="brunobarbosa@quatrou.com.br",
                   subject="#DIARIO_DE_BORDO#",text=corpemail,create_chooser=False)

class MenuApp(App):
    def build(self):
        return GerTela()

janela = MenuApp()
janela.run()