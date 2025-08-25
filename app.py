from flask import Flask,render_template,jsonify
import random
import os

app = Flask(__name__)

# Subjects (Kaun/Kya)
subjects = [
    "Sarkar", "Janta", "Police", "Neta", "Mantri", "Vidyarthi",
    "Khiladi", "Doctor", "Kisan", "Sena", "Adhikari",
    # Funny
    "Padosi", "Billi", "Kutta", "Rickshaw Wala", "Chaiwala",
    "Memer", "Gamer", "WiFi Router", "AI Robot", "Veg Biryani",
    "Crush", "Best Friend", "Ex", "Mummy", "Papa"
]

# Verbs (Kya kar raha hai)
verbs = [
    "Hamla kiya", "Ghoshna ki", "Jeet hasil ki", "Giraftar kiya", "Shuru kiya",
    "Roka", "Launch kiya", "Samapt kiya", "Madad ki", "Dhamki di",
    # Funny
    "Dance kiya", "Selfie li", "Meme banaya", "PUBG khela", "Ludo jeeta",
    "Recharge khatam kiya", "Song gaya", "Troll kiya", "Tharki move dikhaya",
    "Ghoom gaya", "Rap gaya", "TikTok banaya", "Filter lagaya", "Ro diya",
    "Bhag gaya", "Jhaadu lagaya", "Romance kiya", "Propose kiya", "Chill kiya"
]

# Objects (Kis par/Kiske saath)
objects = [
    "Shahar", "Janta", "Bazaar", "School", "Aspatal", "Sadken",
    "Railway Station", "Hawai Adda", "Sansad", "Media", "Traffic",
    # Funny
    "WhatsApp Group", "Instagram Reel", "Chai ki Tapri", "Momos Stall",
    "Rickshaw", "Bike Stand", "Gaming Cafe", "Pados ka terrace",
    "Library ka corner", "Subzi Mandi", "Hostel Mess", "Crush ka ghar",
    "Exam Hall", "Metro Station", "Gali ka dog", "Kirane ki dukaan"
]

# Extra Details (Kab, Kahan, Kyon, Kaise)
extras = [
    "Aaj", "Kal", "Der raat", "Subah", "Dilli me", "Mumbai me",
    # Funny
    "Maggi banate waqt", "Free WiFi milne par", "Recharge khatam hone ke baad",
    "Momos khate hue", "Sleep se uthte hi", "Cricket match ke beech",
    "Online class ke dauran", "Power cut ke time", "Padosi ki shaadi me",
    "WhatsApp forward padh kar", "Instagram scroll karte waqt",
    "BGMI ke last zone me", "Nasha utarne ke baad", "Exam cancel hone par",
    "Salary milte hi", "Date par late hote waqt", "Gym me protein shake girne par"
]

#We are coveting these into the function simmple 

# flag = True
# while (flag==True):

#     sub= random.choice(subjects)
#     verb=random.choice(verbs)
#     object=random.choice(objects)
#     extra=random.choice(extras)


    
#     key = int(input("Press 1 to start.. "))
#     if key == 1:
#         print(f"Breaking News: {extra}, {sub} {verb} {object}  ")
#     else:
#         print("Stopped...")
#         flag=False
#         break
    
def funny_news():
    sub = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    extra = random.choice(extras)
    return f"🔴 Breaking News: {extra}, {sub} ne {verb} {obj}!"

@app.route("/")
def homepage():
    return render_template("index.html")
@app.route("/getnews")
def get_news():
    return jsonify({"news":funny_news()})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)

    
    
    