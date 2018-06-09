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
class AvisoDb(Popup):
    pass

class DiarBord(Screen): #cria a classe do diario de bordo


    def on_pre_enter(self, *args):
        # DEFINIR EVENTO DE TECLADO
        Window.bind(on_keyboard=self.voltar)

    def voltar(sel, window, key, *args):
        # SE A TECLA FOR esc ENTAO
        if key == 27:
            # RETORNA O APP QUE ESTA RODANDO
            App.get_running_app().root.current = "mp"  # AQUI SE MUDA A JANELA QUE SE DESEJA
        return True  # significa que tudo terminou bem

    # DEFINIR COMANDO NA SAIDA
    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.voltar)

    legenda = ['Formulario','Obra', 'Tipo', 'Nome (Ex: Pedro)', 'Dia', 'Mes', 'Ano', 'Placa (Ex: ABC1234)', 'Hora Entrada', 'Minuto Entrada','Quilom. Entrada (Ex: 108423)', 'Hora Saida', 'Minuto Saida', 'Quilom. Saida (Ex: 108432)','Obs(Ex: Pneu Furado)']
    dadospadr = ['Diario de Bordo', 'Escolha Uma Obra', 'Escolha uma Altenativa', 'Ex: Pedro', 'Escolha o dia', 'Escolha o Mes', 'Escolha o Ano', 'Ex: ABC1234', 'Insira a Hora', 'Insira os Minutos', 'Ex: 108423', 'Insira a Hora', 'Insira os Minutos', 'Ex: 108432', 'Ex: Pneu Furado']
    dados = ['Diario de Bordo','','','','','','','','','','','','','','']

#LIMPA O TEXTO ANTES DE DIGITAR E CASO N TENHA SIDO DIGITADO VOLTA AO TEXTO INICIAL
    def dbverificartexto(self, identif, textopadrao):
        if self.ids[identif].text == "":
            self.ids[identif].text = textopadrao
        else:
            if self.ids[identif].text == textopadrao:
                self.ids[identif].text = ""

    def dbcoletardados(self):
        i = 0
        aux = 0
        while i < 14 : #numero de ids a ser coletados
            self.dados[i + 1] = self.ids["db" + str(i)].text
            if self.dados[i + 1].find(self.dadospadr[i + 1]) >= 0 :
                aux = aux + 1
            i = i + 1
        aux = aux - 1
        if aux > 0:
            popup = Popup(title='Aviso', content=Label(text='Dados Incompletos.\nVafor preencher todos os campos.'),
                          auto_dismiss=True, size_hint=(.5, .5))
            popup.open()
        else:
            corpo = ""
            for leg in self.legenda:
                corpo = corpo + leg + ":"
            corpo = corpo + "\n"
            for dado in self.dados:
                corpo = corpo + dado + ":"
            corpo = corpo + "\n"
            email.send(recipient="brunobarbosa@quatrou.com.br",
                   subject="Diario de Bordo",
                   text=corpo,
                   create_chooser=False)
            pass



'''#############         COMANDO DESTINADO AO TESTE DA PAGINA     ###########################################
##########################################################################################################
class DiarBordApp(App):
    def build(self):
        return DiarBord()

janela = DiarBordApp()
janela.run()
#############         COMANDO DESTINADO AO TESTE DA PAGINA     ###########################################
##########################################################################################################
'''