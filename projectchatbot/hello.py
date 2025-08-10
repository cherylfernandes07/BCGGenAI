from flask import Flask

app = Flask(__name__)



def simple_chatbot(user_query):
   if user_query == "What is the total revenue?":
       return "The total revenue is [amount]."
   elif user_query == "How has net income changed over the last year?":
       return "The net income has [increased/decreased] by [amount] over the last year."
   # Add more conditions for other predefined queries
   else:
       return "Sorry, I can only provide information on predefined queries."
   

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
