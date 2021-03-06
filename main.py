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
from datetime import datetime


#Coloca teclado abaixo da entrada e muda fundo para branco
Window.softinput_mode = 'below_target'
Window.clearcolor =[1,1,1,1]

class GerTela(ScreenManager):
    def __init__(self, **kwargs):
        super(GerTela, self).__init__(**kwargs)

class MenuP(Screen):
    pass
class DiarBord(Screen):

    def hora_e_data(self):
        diaehora = datetime.now()
        self.ids.db3.text = str(diaehora.day)
        self.ids.db4.text = str(diaehora.month)
        self.ids.db5.text = str(diaehora.year)
        self.ids.db6.text = str(diaehora.hour)
        self.ids.db7.text = str(diaehora.minute)

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
               'Hora', 'Minutos', 'Nome', 'Placa','Hodometro', 'Obs']
    dadopadrao = ['Escolha Uma Obra', 'Escolha Uma Equipe', 'Escolha o dia', 'Escolha o Mes', 'Escolha o Ano',
                  'Insira a Hora', 'Insira os Minutos', 'Ex: Pedro', 'Ex: ABC1423','Ex: 23999', 'Ex: Deslocamento a Torre 05']
    def verificar(self):
        dpad = self.dadopadrao
        i = 1
        contador = 0
        while i < (len(self.legenda) + 1) :
            if dpad[i - 1].find(self.ids['db'+str(i)].text) >= 0:
                self.ids['db' + str(i)].color=(1,0,0,1)
                contador = contador + 1
            else:
                self.ids['db' + str(i)].color = (1, 1, 1, 1)
            i = i +1
        #todo ver nescessiade destas duas linha
        if dpad[i - 2].find(self.ids['db' + str(i - 1)].text) >= 0:
            self.ids['db' + str(i - 1)].text = "-"
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
        #todo implementar melhor a menssagem( colocar um try)
        popup = Popup(title='Aviso', content=Label(text='Dados Salvos'),
                      auto_dismiss=True, size_hint=(1, .5))
        popup.open()
    def limp_dados(self):
        i = 1
        contador = 0
        while i < (len(self.legenda) + 1):
            self.ids['db' + str(i)].text = self.dadopadrao[i - 1]
            i = i + 1
    def enviar_db(self,chave,legenda):
        corpo_do_email = MenuApp().coletar_dados(chave,legenda)
        if corpo_do_email == None:
            popup = Popup(title='Aviso', content=Label(text='Nao Existem Dados a Enviar'),
                          auto_dismiss=True, size_hint=(1, .5))
            popup.open()
        else:
            email.send(recipient="brunobarbosa@quatrou.com.br",
                       subject=chave, text=corpo_do_email, create_chooser=False)

class MenuApp(App):
    '''
    def enviar_dados(self,chave,legenda):
        store = JsonStore('4u.json')
        # procura linha com a chave
        try:
            for item in store:
                if item.find(chave) >= 0:
                    chaveencontrada = True
                    break
                else:
                    popup = Popup(title='Aviso', content=Label(text='Nao Existem Dados a Enviar'),
                                  auto_dismiss=True, size_hint=(1, .5))
                    popup.open()
                    break
            #todo verificar legenda fica louca
            if chaveencontrada == True:
                texto = ""
                for leg in legenda:
                    texto = texto + leg + ";"
                texto = texto + "\n"
                for item in store:
                    if item.find(chave) >= 0:
                        #pegar cada valor de cada item que é compatival com a chave
                        aux = store[item]
                        for leg in legenda:
                            texto = texto + aux[leg] + ";"
                        texto = texto + "\n"
                    else:
                        pass
                email.send(recipient="brunobarbosa@quatrou.com.br",
                           subject=chave, text=texto, create_chooser=False)
            else:
                pass
        except:
            popup = Popup(title='Aviso', content=Label(text='Nao Existem Dados a Enviar'),
                          auto_dismiss=True, size_hint=(1, .5))
            popup.open()
    '''
    def coletar_dados(self,chave,legenda):
        store = JsonStore('4u.json')
        # procura linha com a chave
        try:
            for item in store:
                if item.find(chave) >= 0:
                    chaveencontrada = True
                    break
                else:
                    break
            if chaveencontrada == True:
                texto = ""
                for leg in legenda:
                    texto = texto + leg + ";"
                texto = texto + "\n"
                for item in store:
                    if item.find(chave) >= 0:
                        #pegar cada valor de cada item que é compatival com a chave
                        aux = store[item]
                        for leg in legenda:
                            texto = texto + aux[leg] + ";"
                        texto = texto + "\n"
                    else:
                        pass
                return texto
            else:
                pass
        except:
            pass

    def build(self):
        return GerTela()

janela = MenuApp()
janela.run()