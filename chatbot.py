from flask import Flask, render_template

chatbotapp = Flask(_name_)

@chatbotapp.route('/')
def bot():
    return render_template("chatbot.html")

if _name_ == "main":
    chatbotapp.run(debug=True,use_reloader=False)