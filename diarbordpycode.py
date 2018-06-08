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

#todo implementar aviso <AvisoDb@Popup>:

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


    legenda = ['Formulario','Obra', 'Tipo', 'Nome (Ex: Pedro)', 'Dia', 'Mes', 'Ano', 'Placa (Ex: ABC1234)', 'Hora Entrada', 'Minuto Entrada','Quilom. Entrada (Ex: 108423)', 'Hora Saida', 'Minuto Saida', 'Quilom. Saida (Ex: 108432)','Obs(Ex: Pneu Furado)']
    dadospadr = ['Diario de Bordo', 'Escolha Uma Obra', 'Escolha uma Altenativa', 'Ex: Pedro', 'Escolha o dia', 'Escolha o Mes', 'Escolha o Ano', 'Ex: ABC1234', 'Insira a Hora', 'Insira os Minutos', 'Ex: 108423', 'Insira a Hora', 'Insira os Minutos', 'Ex: 108432', 'Ex: Pneu Furado']
    dados = ['Diario de Bordo','Obra','Tipo','Ex: Pedro','Dia','Mes','Ano','Ex: ABC1234','Hora Entrada','Minuto Entrada','Quilom. Entrada','Hora Saida','Minuto Saida','Quilom. Saida','Obs']

#LIMPA O TEXTO ANTES DE DIGITAR E CASO N TENHA SIDO DIGITADO VOLTA AO TEXTO INICIAL
    def vertexto(self,identif,text):
        if self.ids[identif].text == "":
            self.ids[identif].text = text
        else:
            if self.ids[identif].text == text:
                self.ids[identif].text = ""



    def verificardados(self):
        #########  RECEBE OS DADOS  ######
        self.dados = []  # limpa a lista de dados
        for ident in self.ids:
            self.dados.append(self.ids[ident].text)

        #########  RECEBE OS DADOS  ######



        ###### CASO N SEJA COLOCADO OBSERVAÇÃO ZERAR O VALOR ######
        if self.dadospadr[len(self.dadospadr) - 1] == self.dados[len(self.dadospadr) - 1]:
            self.dados[len(self.dadospadr) - 1] = "-"

        validador = 0
        i = 0
        while i < (len(self.dadospadr)-1): # EQUANTO I É MELHOR QUE O TAMANHP DA LEGENDA FAZ
            if self.dadospadr[i].find(self.dados[i]) == 0:
                validador = validador + 1
            i = i + 1

        ########## CASO HAJA ERRO NA COMPARAÇÃO DOS DADOS COM A LEJENDA, INFORMAR AO USUÁRIO ############
        if validador > 1:
            popup = Popup(title='Aviso', content=Label(text='Dados Incompletos.\n Favor verificar'),
                          auto_dismiss=True, size_hint=(.5,.5))
            popup.open()

        ##### CASO NÃO HAJA ERRO NA COMPARAÇÃO ######
        if validador == 1:


            ###SALVA EM ARQUIVO####

            grav = open('dadosdb.csv', 'a+')
            ler = open('dadosdb.csv', 'r')

            i = 0
            for linha in ler:
                i = 1
                if i == 1:
                    break
            if i == 0:
                # adicionar legenda
                for palavra in self.legenda:
                    grav.write(palavra + ":")
                grav.write("\n")
            ## GRAVAR DADOS NO ARQUIVIO ####
            for palavra in self.dados:
                grav.write(palavra + ":")
            grav.write("\n")

            ler.close()
            grav.close()

            ###SALVA EM ARQUIVO####

            popup = Popup(title='Aviso', content=Label(text='Dados Salvos com Sucesso'),
                          auto_dismiss=True, size_hint=(.5, .5))
            popup.open()




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