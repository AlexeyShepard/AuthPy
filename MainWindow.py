import peewee
from SQLConnector import *
from UserModel import *

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class MainWindow(App):

    #Компоненты окна

    __LoginRegTI = TextInput(text="Логин", multiline=False, font_size=32)
    __PasswordRegTI = TextInput(text="Пароль", multiline=False, password=True, font_size=32)
    __RegBtn = Button(text="Регистрация", font_size=32)

    __PinTI = TextInput(text="Пин-код", multiline=False, font_size=32)
    __AuthBtn = Button(text="Подтвердить", font_size=32)

    __LoginLogTI = TextInput(text="Логин", multiline=False, font_size=32)
    __PasswordLogTI = TextInput(text="Пароль", multiline=False, password=True, font_size=32)
    __LogBtn = Button(text="Авторизация", font_size=32)

    #Сallback функции

    def onClickRegButton(instance, self):
        print("Произошла регистрация")
        Connector = SQLConnector("root", "root", "AuthPy", "localhost")
        Connector.connect()
        u = UserModel('alexey','12345','55555',False)
        u.save()


    def onClickAuthButton(instance, self):
        print("Произошла аутентификация")

    def onClickLoginButton(instance, self):
        print("Произошла авторизация")

    #Форматирование окна приложения

    def build(self):
        self.__RegBtn.bind(on_press=self.onClickRegButton)
        self.__AuthBtn.bind(on_press=self.onClickAuthButton)
        self.__LogBtn.bind(on_press=self.onClickLoginButton)

        return self.formatDesign()

    def formatDesign(self):
        mainLayout = BoxLayout(orientation="horizontal", padding=[100], spacing=30)

        regLayout = BoxLayout(orientation="vertical", spacing=30)
        regLayout.add_widget(self.__LoginRegTI)
        regLayout.add_widget(self.__PasswordRegTI)
        regLayout.add_widget(self.__RegBtn)

        pinLayout = BoxLayout(orientation="vertical", spacing=30)
        pinLayout.add_widget(self.__PinTI)
        pinLayout.add_widget(self.__AuthBtn)
        pinLayout.add_widget(Widget())

        logLayout = BoxLayout(orientation="vertical", spacing=30)
        logLayout.add_widget(self.__LoginLogTI)
        logLayout.add_widget(self.__PasswordLogTI)
        logLayout.add_widget(self.__LogBtn)

        mainLayout.add_widget(regLayout)
        mainLayout.add_widget(pinLayout)
        mainLayout.add_widget(logLayout)

        return mainLayout
