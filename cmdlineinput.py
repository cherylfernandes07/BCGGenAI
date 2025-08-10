import extractdata

amount = extractdata.getTotalRevenue()

def simple_chatbot(user_query):
   if user_query == "What is the total revenue?":
       return "The total revenue is "+ str(amount) + "\n Would you like to know how much this increased by?"
   elif user_query == "How has net income changed over the last year?":
       return "The net income has [increased/decreased] by [amount] over the last year."
   # Add more conditions for other predefined queries
   else:
       return "Sorry, I can only provide information on predefined queries."
   

# name = input("Enter your question: ")
# print("Hello,", name)
while True:
    user_input = input("Enter a question (or type 'quit' to exit): ").strip().lower()
    #question = input("Enter your question: ")

    if user_input == 'quit':
        print("Exiting program.")
        break  # Exit the loop and terminate the program
    else:
        question = input("Enter your question: ")
        print(simple_chatbot(question))
        # Add your program's logic here based on other commands
        # For example:
        # if user_input == 'hello':
        #     print("Hi there!")
        # elif user_input == 'status':
        #     print("Program is running normally.")


