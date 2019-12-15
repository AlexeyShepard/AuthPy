from SQLConnector import *
from Helper import *

from sqlalchemy import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.label import Label

class MainWindow(App):

    __Connector = SQLConnector("mysql", "mysql", "authpy", "localhost")

    #Компоненты окна

    __LoginRegTI = TextInput(text="Логин", multiline=False, font_size=32)
    __PasswordRegTI = TextInput(text="Пароль", multiline=False, password=True, font_size=32)
    __RegBtn = Button(text="Регистрация", font_size=32)

    __LoginLogTI = TextInput(text="Логин", multiline=False, font_size=32)
    __PasswordLogTI = TextInput(text="Пароль", multiline=False, password=True, font_size=32)
    __PinTI = TextInput(text="Пин-код", multiline=False, font_size=32)
    __LogBtn = Button(text="Авторизация", font_size=32)
    __LabelLogTI = Label(text="Статус:", font_size=32)

    #Сallback функции

    def onClickRegButton(instance, self):
        print("Произошла регистрация")
        instance.__Connector.insertUser(instance.__LoginRegTI.text, instance.__PasswordRegTI.text, Helper().randomPin() , False)


    def onClickLoginButton(instance, self):
        print("Произошла авторизация")
        result = instance.__Connector.selectUser(instance.__LoginLogTI.text, instance.__PasswordLogTI.text, instance.__PinTI.text)
        if result is None:
            instance.__LabelLogTI.text = "Статус: Данные введены не верно =("
        else:
            instance.__LabelLogTI.text = "Статус: Вы успешно авторизованы"

    #Форматирование окна приложения

    def build(self):
        self.__RegBtn.bind(on_press=self.onClickRegButton)
        self.__LogBtn.bind(on_press=self.onClickLoginButton)

        return self.formatDesign()

    def formatDesign(self):
        mainLayout = BoxLayout(orientation="horizontal", padding=[100], spacing=30)

        regLayout = BoxLayout(orientation="vertical", spacing=30)
        regLayout.add_widget(self.__LoginRegTI)
        regLayout.add_widget(self.__PasswordRegTI)
        regLayout.add_widget(self.__RegBtn)

        logLayout = BoxLayout(orientation="vertical", spacing=30)
        logLayout.add_widget(self.__LoginLogTI)
        logLayout.add_widget(self.__PasswordLogTI)
        logLayout.add_widget(self.__PinTI)
        logLayout.add_widget(self.__LogBtn)
        logLayout.add_widget(self.__LabelLogTI)

        mainLayout.add_widget(regLayout)
        mainLayout.add_widget(logLayout)

        return mainLayout
