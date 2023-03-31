from js import document, alert

class Movement_calc:
    def __init__(self, square, velocity, velocity_start, acceleration, time, action, result):
        self.square = square
        self.velocity = velocity
        self.velocity_start = velocity_start
        self.acceleration = acceleration
        self.time = time
        self.action = action
        self.result = result

mov_calc = Movement_calc("", "", "", "", "", "", "")
sign = ["Square", "Velocity0", "Velocityк", "acceler", "time", "count"]

def sign_clicked(args):

    if args.target.id == "Square":
        Square()




def Square(*args, **kws):

    S = document.getElementById('S').value
    V0 = document.getElementById('V0').value
    Vk = document.getElementById('Vk').value
    a = document.getElementById('a').value
    t = document.getElementById('t').value

    if V0 * Vk * a * t != 0:
        x = V0 * t
        y = a * t ** 2
        z = y / 2
        result = x + z

        print("Answerr:", result)        

