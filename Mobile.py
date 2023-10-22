from kivymd.uix.screen import MDScreen
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine,MDExpansionPanelTwoLine
import numpy as np
from matplotlib import pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import Content
from kivy.properties import ObjectProperty
from kivy.uix.label import Label










class MobileView(MDScreen):
      sc=ObjectProperty()
      nav_drawer=ObjectProperty()
      

      def __init__(self, **kwargs):
            super().__init__(**kwargs)

            M1 = MDExpansionPanel(icon="account-circle", content=Content.Content1(), panel_cls=MDExpansionPanelTwoLine(text="jagan",secondary_text="Administrator",theme_text_color="Custom",text_color="#B9BAB5",secondary_theme_text_color="Custom",secondary_text_color="#B9BAB5"), )
            M2 = MDExpansionPanel(icon="pencil-box", content=Content.Content2(),panel_cls=MDExpansionPanelOneLine(text="Master",theme_text_color="Custom",text_color="#B9BAB5"), )
            M3 = MDExpansionPanel(icon="layers-triple", content=Content.Content3(),panel_cls=MDExpansionPanelOneLine(text="Order Management",theme_text_color="Custom",text_color="#B9BAB5"), )
            M4 = MDExpansionPanel(icon="cube", content=Content.Content4(),panel_cls=MDExpansionPanelOneLine(text="Process",theme_text_color="Custom",text_color="#B9BAB5"), )
            M5 = MDExpansionPanel(icon="gamepad-round-down", content=Content.Content5(),panel_cls=MDExpansionPanelOneLine(text="Stock Movement",theme_text_color="Custom",text_color="#B9BAB5"), )
            M6 = MDExpansionPanel(icon="flash-triangle", content=Content.Content6(),panel_cls=MDExpansionPanelOneLine(text="Cutting",theme_text_color="Custom",text_color="#B9BAB5"), )
            M7 = MDExpansionPanel(icon="layers-triple-outline", content=Content.Content7(),panel_cls=MDExpansionPanelOneLine(text="Production",theme_text_color="Custom",text_color="#B9BAB5"), )
            M8 = MDExpansionPanel(icon="alpha-m", content=Content.Content8(),panel_cls=MDExpansionPanelOneLine(text="General",theme_text_color="Custom",text_color="#B9BAB5"), )
            M9 = MDExpansionPanel(icon="database", content=Content.Content9(),panel_cls=MDExpansionPanelOneLine(text="Stores",theme_text_color="Custom",text_color="#B9BAB5"), )
            M10 = MDExpansionPanel(icon="view-compact", content=Content.Content10(),panel_cls=MDExpansionPanelOneLine(text="Accounts",theme_text_color="Custom",text_color="#B9BAB5"), )
            M11 = MDExpansionPanel(icon="database", content=Content.Content11(),panel_cls=MDExpansionPanelOneLine(text="Simple Production",theme_text_color="Custom",text_color="#B9BAB5"), )
            M12 = MDExpansionPanel(icon="ambulance", content=Content.Content12(),panel_cls=MDExpansionPanelOneLine(text="Warehouse",theme_text_color="Custom",text_color="#B9BAB5"), )
            M13 = MDExpansionPanel(icon="cog", content=Content.Content13(),panel_cls=MDExpansionPanelOneLine(text="Reports", theme_text_color="Custom",text_color="#B9BAB5"), )
            M14 = MDExpansionPanel(icon="chart-box", content=Content.Content14(),panel_cls=MDExpansionPanelOneLine(text="Settings", theme_text_color="Custom",text_color="#B9BAB5"), )
            M15 = MDExpansionPanel(icon="layers-triple-outline", content=Content.Content15(),panel_cls=MDExpansionPanelOneLine(text="Stock Auditing", theme_text_color="Custom",text_color="#B9BAB5"), )

            self.ids.box.add_widget(M1)
            self.ids.box.add_widget(M2)
            self.ids.box.add_widget(M3)
            self.ids.box.add_widget(M4)
            self.ids.box.add_widget(M5)
            self.ids.box.add_widget(M6)
            self.ids.box.add_widget(M7)
            self.ids.box.add_widget(M8)
            self.ids.box.add_widget(M9)
            self.ids.box.add_widget(M10)
            self.ids.box.add_widget(M11)
            self.ids.box.add_widget(M12)
            self.ids.box.add_widget(M13)
            self.ids.box.add_widget(M14)
            self.ids.box.add_widget(M15)

            x1 = np.array(["Apr'22", "may'22", "Jun'22", "Jul'22","Aug'22","Sep'22","Oct'22","Nov'22","Dec'22","Jan'23","Feb'23","Mar'23"])

            y1 = np.array([3, 0, 1, 0, 0, 1, 3, 2, 10, 4, 5, 0])

            fig = plt.figure()
            ax = plt.axes()
            # Setting the background color
            ax.set_facecolor("#202940")
            fig.set_facecolor("#202940")

            fig = plt.bar(x1,y1, color="#e60000")
            #fig = plt.bar(y1, color="#2dad38")
            plt.xticks(rotation=35)


            self.ids.bar.add_widget(FigureCanvasKivyAgg(plt.gcf(),size_hint_y=.7))

      def sam(self):
          data=self.ids.gettxt.text
          for x in data:
                
                l=Label(text=str(x))
                self.ids.put.add_widget(l) 
      

      