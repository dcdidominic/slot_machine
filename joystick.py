import pygame

class Joystick():
    def __init__(self):
        # Joystick setup
        pygame.joystick.init()
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            print("Joystick connected")
        else:
            self.joystick = None
            print("No joystick connected")

    def check_joystick_buttons(self):
        if self.joystick:
            for button in range(self.joystick.get_numbuttons()):
                if self.joystick.get_button(button):
                    print(button)
                    return True
        return False
    
    def check_joystick_pull_back(self):
        if self.joystick:
            y_axis = self.joystick.get_axis(1)  # Get the value of the y-axis (usually axis 1)
            if y_axis > 0.5:  # Adjust the threshold as needed
                return True
        return False
