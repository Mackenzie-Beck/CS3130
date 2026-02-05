import Controller
import View
import Model

def main():
    
    controller = Controller.Controller()
    model = Model.Model()
    view = View.View()

    controller.view = view
    controller.Model = model
    view.controller = controller

    # Initialize server connection parameters
    controller.SERVERIP = 'localhost'
    controller.SERVERPORT = 20500
    controller.ENCODER = 'utf-8'
    controller.BUFFER = 1024

    view.main_menu()


if __name__ == "__main__":
    main()