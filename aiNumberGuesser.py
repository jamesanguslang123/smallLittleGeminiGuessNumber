from google import genai

client = genai.Client()

userInput = 0
guess = 1
answers = []

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Hello! You are the AI opponent in a number prediction game. Introduce yourself briefly."
)

print(response.text)

while guess != userInput:

    userInput = int(input("Enter a number 1-10: "))
    answers.append(userInput)

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"""
        These are the numbers the player has entered so far: {answers}

        Predict what number they will enter next between 1 and 10.
        Output that number only.
        """
    )

    guess = int(response.text.strip())



print("Gemini got it right!")