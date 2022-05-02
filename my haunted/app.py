from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "The Haunted Forest"
    
    text = """Oh, no... You have entered the haunted forest... Who knows what can happen here.. Run! While you still can..."""

    choices = [
        ('enter_forest',"Go to the forest..."),
        ('run_away',"Run!!!")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/inside")
def enter_forest():
    title = "You go into the forest..."
    
    text = """... and it suddenly starts to rain. The road becomes slippery. You see a bonfire in the distance. Seems like it's the only way.."""

    choices = [
        ('bonfire',"Go towards the bonfire"),
        ('run_away',"Try to run away while it isn't too late")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/escape")
def run_away():
    title = "You run away!"
    
    text = """You run away from the forest in pitch darkness. It seems like the further away you run the closer the forest is... That's not right..."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/bonfire")
def bonfire():
    title = "Careful!"
    
    text = """Suddenly you fall down on a slippery road. As you try to get up the powers are leaving you... That was a nice trip to the forest..."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)
