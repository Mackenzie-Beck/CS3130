import Controller
import View
import Model

def main():
    
    controller = Controller.Controller()
    model = Model.Model()
    view = View.View()

    controller.View = view
    controller.Model = model
    view.controller = controller

    view.main_menu()


if __name__ == "__main__":
    main()