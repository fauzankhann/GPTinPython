import openai

openai.api_key = "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"


def generate_response(prompt):
    # Call the OpenAI API to generate response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the response text from the API response
    response_text = response.choices[0].text.strip()

    return response_text


while True:
    # Let user input
    user_prompt = input("What do you want to ask?: ")

    # Generate response with the OpenAI API (call function)
    gpt_response = generate_response(user_prompt)

    # Print the response
    print("GPT: " + gpt_response)
