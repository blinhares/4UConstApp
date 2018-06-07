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

class AvisoDb(Popup):
    #TODO INSERIR COMANDO PARA QUE O BOTAO SALVAR EXECUTE O COMANDO E MUDE DE TELA
    pass

class DiarBord(Screen): #cria a classe dodiario de bordo

    ########################################################################################################################################################################
    #################### PERMITE QUE O BOTÃO VOLTAR DO ANDROID OU ESC SEJAM UTILIZADOS PARA A MUDANÇA DE TELAS #############################################################
    ########################################################################################################################################################################
    ###### USAR EVENDO DE ENTRADA ###
    ##QUANDO O EVENTO OCORRER , CHAMAR A FUNC VOLTAR ###
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

    ########################################################################################################################################################################
    #################### PERMITE QUE O BOTÃO VOLTAR DO ANDROID OU ESC SEJAM UTILIZADOS PARA A MUDANÇA DE TELAS #############################################################
    ########################################################################################################################################################################


    legenda = ['Diario de Bordo', 'Tipo', 'Nome (Ex: Pedro)', 'Dia', 'Mes', 'Ano', 'Placa (Ex: ABC1234)', 'Hora Entrada', 'Minuto Entrada','Quilom. Entrada (Ex: 108432)', 'Hora Saida', 'Minuto Saida', 'Quilom. Saida (Ex: 108432)']
    dados = ['Diario de Bordo','Tipo','Nome','Dia','Mes','Ano','Placa','Hora Entrada','Minuto Entrada','Quilom. Entrada','Hora Saida','Minuto Saida','Quilom. Saida']

#LIMPA O TEXTO ANTES DE DIGITAR E CASO N TENHA SIDO DIGITADO VOLTA AO TEXTO INICIAL
    def vertexto(self,identif,text):
        if self.ids[identif].text == "":
            self.ids[identif].text = text
        else:
            if self.ids[identif].text == text:
                self.ids[identif].text = ""

#COLETA DOS DADOS
    def coletar(self,arg,ord):
        self.dados[ord] = arg

    def verificardados(self):
        validador = 0
        i = 0
        while i < len(self.legenda): # EQUANTO I É MELHOR QUE O TAMANHP DA LEGENDA FAZ
            if self.legenda[i].find(self.dados[i]) == 0:
                validador = validador + 1
            i = i + 1

        print(validador)
        if validador > 1: #CASO HAJA ERRO NA COMPARAÇÃO DOS DADOS COM A LEJENDA, INFORMAR AO USUÁRIO
            popup = Popup(title='Aviso', content=Label(text='Dados Incompletos.\n Favor verificar'),
                          auto_dismiss=True, size_hint=(.5,.5))
            popup.open()

        if validador == 1: #CASO NÃO HAJA ERRO NA COMPARAÇÃO
            return AvisoDb().open() #retorna POPUP criado no arquivo kv e declarado no corpo de main

    def salvar (self):
        #todo DEFINIR FUNCAO SALVAR

        pass


'''
#############         COMANDO DESTINADO AO TESTE DA PAGINA     ###########################################
##########################################################################################################
class DiarBordApp(App):
    def build(self):
        return DiarBord()

janela = DiarBordApp()
janela.run()
#############         COMANDO DESTINADO AO TESTE DA PAGINA     ###########################################
##########################################################################################################
'''