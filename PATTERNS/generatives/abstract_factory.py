"""Абстрактная фабрика
Позволяет создавать семейство связанных между собой классов без привязки к конкретному классу.
Все взаимодействие идет через интерфейс базового класса.

В каких случаях?
1. Если разрабатываемая система не должна зависеть от того как компонуются,
создаются и представляются входящие в нее объекты
2. Объекты, входящие в взаимосвязанное семейство должны использоваться вместе.
3. Конфигурация системы должна производиться одним из семейством составляющих ее объектов
4. Необходимо скрыть от пользователей реализацию,
но предоставить интерфейсы для использования модуля (класса, библиотеки)
5. Если уже используются Фабричный метод и необходимо ввести в систему новые типы продуктов

Преимущества:
1. Клиентский код не привязан к продукту.
2. Гарантирует сочетаемость создаваемых продуктов.
3.
Недостатки:
1. Много дополнительных классов - сложнее код
2. 
"""


from abc import ABC, abstractmethod

"""
Базовые классы графического пользовательского интерфейса
"""
class StatusBar(ABC):
    def __init__(self, system:str):
        self._system = system

    @abstractmethod
    def create(self): pass

class MainMenu(ABC):
    def __init__(self, system:str):
        self._system = system

    @abstractmethod
    def create(self): pass

class MainWindow(ABC):
    def __init__(self, system:str):
        self._system = system

    @abstractmethod
    def create(self): pass

"""
Производные классы графического пользовательского интерфейса для операционной системы Windows
"""

class WindowsStatusBar(StatusBar):
    def __init__(self):
        super().__init__('Windows')

    def create(self):
        print(f'Created status bar for {self._system}')


class WindowsMainMenu(MainMenu):
    def __init__(self):
        super().__init__('Windows')

    def create(self):
        print(f'Created main menu for {self._system}')


class WindowsMainWindow(MainWindow):
    def __init__(self):
        super().__init__('Windows')

    def create(self):
        print(f'Created main window for {self._system}')

"""
Производные классы графического пользовательского интерфейса для операционной системы Linux
"""

class LinuxStatusBar(StatusBar):
    def __init__(self):
        super().__init__('Linux')

    def create(self):
        print(f'Created status bar for {self._system}')


class  LinuxMainMenu(MainMenu):
    def __init__(self):
        super().__init__('Linux')

    def create(self):
        print(f'Created main menu for {self._system}')


class LinuxMainWindow(MainWindow):
    def __init__(self):
        super().__init__('Linux')

    def create(self):
        print(f'Created main window for {self._system}')

"""
Базовый класс абстрактной фабрики
"""

class GuiAbstractFactory(ABC):

    @abstractmethod
    def getStatusBar(self) -> StatusBar: pass

    @abstractmethod
    def getMainMenu(self) -> MainMenu: pass

    @abstractmethod
    def getMainWindow(self) -> MainWindow: pass

"""
Производные классы абстрактной фабрики,
Конкретные реализации для каждой из операционных систем
"""

class WindowsGuiFactory(GuiAbstractFactory):
    def getStatusBar(self) -> StatusBar:
        return WindowsStatusBar()

    def getMainMenu(self) -> MainMenu:
        return WindowsMainMenu()

    def getMainWindow(self) -> MainWindow:
        return WindowsMainWindow()


class LinuxGuiFactory(GuiAbstractFactory):
    def getStatusBar(self) -> StatusBar:
        return LinuxStatusBar()

    def getMainMenu(self) -> MainMenu:
        return LinuxMainMenu()

    def getMainWindow(self) -> MainWindow:
        return LinuxMainWindow()


"""
Клиентский класс использующий фабрику для создания GUI
"""
class App:
    def __init__(self, factory: GuiAbstractFactory): # <<-- В независимости от ОС, вызывается абстрактная фабрика и она уже управляет созданием классов
        self._gui_factory = factory

    def create_gui(self):
        mainwindow = self._gui_factory.getMainWindow()
        status_bar = self._gui_factory.getStatusBar()
        main_menu = self._gui_factory.getMainMenu()
        mainwindow.create()
        main_menu.create()
        status_bar.create()


def create_factory(system_name:str)-> GuiAbstractFactory:
    factory_dict = {
        "Windows": WindowsGuiFactory,
        "Linux": LinuxGuiFactory,

    }
    return factory_dict[system_name]()



# from __future__ import annotations

# class AbstractFactory(ABC):
#     """
#     Интерфейс Абстрактной Фабрики объявляет набор методов, которые возвращают
#     различные абстрактные продукты. Эти продукты называются семейством и связаны
#     темой или концепцией высокого уровня. Продукты одного семейства обычно могут
#     взаимодействовать между собой. Семейство продуктов может иметь несколько
#     вариаций, но продукты одной вариации несовместимы с продуктами другой.
#     """
#     @abstractmethod
#     def create_product_a(self) -> AbstractProductA:
#         pass
#
#     @abstractmethod
#     def create_product_b(self) -> AbstractProductB:
#         pass
#
#
# class ConcreteFactory1(AbstractFactory):
#     """
#     Конкретная Фабрика производит семейство продуктов одной вариации. Фабрика
#     гарантирует совместимость полученных продуктов. Обратите внимание, что
#     сигнатуры методов Конкретной Фабрики возвращают абстрактный продукт, в то
#     время как внутри метода создается экземпляр конкретного продукта.
#     """
#
#     def create_product_a(self) -> AbstractProductA:
#         return ConcreteProductA1()
#
#     def create_product_b(self) -> AbstractProductB:
#         return ConcreteProductB1()
#
#
# class ConcreteFactory2(AbstractFactory):
#     """
#     Каждая Конкретная Фабрика имеет соответствующую вариацию продукта.
#     """
#
#     def create_product_a(self) -> AbstractProductA:
#         return ConcreteProductA2()
#
#     def create_product_b(self) -> AbstractProductB:
#         return ConcreteProductB2()
#
#
# class AbstractProductA(ABC):
#     """
#     Каждый отдельный продукт семейства продуктов должен иметь базовый интерфейс.
#     Все вариации продукта должны реализовывать этот интерфейс.
#     """
#
#     @abstractmethod
#     def useful_function_a(self) -> str:
#         pass
#
#
# """
# Конкретные продукты создаются соответствующими Конкретными Фабриками.
# """
#
#
# class ConcreteProductA1(AbstractProductA):
#     def useful_function_a(self) -> str:
#         return "The result of the product A1."
#
#
# class ConcreteProductA2(AbstractProductA):
#     def useful_function_a(self) -> str:
#         return "The result of the product A2."
#
#
# class AbstractProductB(ABC):
#     """
#     Базовый интерфейс другого продукта. Все продукты могут взаимодействовать
#     друг с другом, но правильное взаимодействие возможно только между продуктами
#     одной и той же конкретной вариации.
#     """
#     @abstractmethod
#     def useful_function_b(self) -> None:
#         """
#         Продукт B способен работать самостоятельно...
#         """
#         pass
#
#     @abstractmethod
#     def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
#         """
#         ...а также взаимодействовать с Продуктами A той же вариации.
#
#         Абстрактная Фабрика гарантирует, что все продукты, которые она создает,
#         имеют одинаковую вариацию и, следовательно, совместимы.
#         """
#         pass
#
#
# """
# Конкретные Продукты создаются соответствующими Конкретными Фабриками.
# """
#
#
# class ConcreteProductB1(AbstractProductB):
#     def useful_function_b(self) -> str:
#         return "The result of the product B1."
#
#     """
#     Продукт B1 может корректно работать только с Продуктом A1. Тем не менее, он
#     принимает любой экземпляр Абстрактного Продукта А в качестве аргумента.
#     """
#
#     def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
#         result = collaborator.useful_function_a()
#         return f"The result of the B1 collaborating with the ({result})"
#
#
# class ConcreteProductB2(AbstractProductB):
#     def useful_function_b(self) -> str:
#         return "The result of the product B2."
#
#     def another_useful_function_b(self, collaborator: AbstractProductA):
#         """
#         Продукт B2 может корректно работать только с Продуктом A2. Тем не менее,
#         он принимает любой экземпляр Абстрактного Продукта А в качестве
#         аргумента.
#         """
#         result = collaborator.useful_function_a()
#         return f"The result of the B2 collaborating with the ({result})"
#
#
# def client_code(factory: AbstractFactory) -> None:
#     """
#     Клиентский код работает с фабриками и продуктами только через абстрактные
#     типы: Абстрактная Фабрика и Абстрактный Продукт. Это позволяет передавать
#     любой подкласс фабрики или продукта клиентскому коду, не нарушая его.
#     """
#     product_a = factory.create_product_a()
#     product_b = factory.create_product_b()
#
#     print(f"{product_b.useful_function_b()}")
#     print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    system_name = "Linux"
    ui = create_factory(system_name)
    app = App(ui)
    app.create_gui()

    # """
    # Клиентский код может работать с любым конкретным классом фабрики.
    # """
    # print("Client: Testing client code with the first factory type:")
    # client_code(ConcreteFactory1())
    #
    # print("\n")

    # print("Client: Testing the same client code with the second factory type:")
    # client_code(ConcreteFactory2())