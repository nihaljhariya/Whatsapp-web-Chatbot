import google.generativeai as genai

# Configure with your Gemini API key
genai.configure(api_key="__Your api Key of Gemini __")

# Chat history string (WhatsApp style)
command = '''
[20:30, 12/6/2024] Naruto: jo sunke coding ho sake?
[20:30, 12/6/2024] Rohan Das: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:30, 12/6/2024] Rohan Das: ye
[20:30, 12/6/2024] Rohan Das: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:31, 12/6/2024] Naruto: This is hindi
[20:31, 12/6/2024] Naruto: send me some english songs
[20:31, 12/6/2024] Naruto: but wait
[20:31, 12/6/2024] Naruto: this song is amazing
[20:31, 12/6/2024] Naruto: so I will stick to it
[20:31, 12/6/2024] Naruto: send me some english song also
[20:31, 12/6/2024] Rohan Das: hold on
[20:31, 12/6/2024] Naruto: I know what you are about to send
[20:32, 12/6/2024] Naruto: 😂😂
[20:32, 12/6/2024] Rohan Das: https://www.youtube.com/watch?v=ar-3chBG4NU
ye hindi English mix hai but best hai
[20:33, 12/6/2024] Naruto: okok
[20:33, 12/6/2024] Rohan Das: Haan
'''

# Define the system-style prompt for Gemini
prompt = (
    "You are a person named Ayush who speaks Hindi as well as English. "
    "You are from India and a coder. You analyze the following chat and respond like Ayush: "
    f"\n\nChat History:\n{command}"
)

# Generate the response
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt)

# Print the result
print(response.text)
