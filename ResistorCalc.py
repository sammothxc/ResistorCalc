from picoware.system.view_manager import ViewManager
from picoware.system.view import View

vm = None

try:
    vm = ViewManager()
    vm.add(
        View(
            "app_tester",
            run,
            start,
            stop,
        )
    )
    vm.switch_to("app_tester")
    while True:
        vm.run()
except Exception as e:
    print("Error during testing:", e)
finally:
    del vm
    vm = None

def start(view_manager):
    '''Start the app'''
    from picoware.system.vector import Vector
    from time import sleep

    draw = view_manager.get_draw()
    draw.clear()
    draw.text(Vector(10, 10), "Example App")
    draw.swap()

    sleep(2)  # Brief pause to let user read the header
    return True

def run(view_manager):  
    '''Run the app'''
    from picoware.system.buttons import (
        BUTTON_BACK,
        BUTTON_UP,
        BUTTON_DOWN,
        BUTTON_LEFT,
        BUTTON_CENTER,
        BUTTON_RIGHT,
    )
    input_manager = view_manager.input_manager
    button = input_manager.get_last_button()
    if button == BUTTON_BACK:
        input_manager.reset() # reset to avoid multiple back presses
        view_manager.back()

def stop(view_manager):
    '''Stop the app'''
    from gc import collect
    # clean up any global variables here
    collect()