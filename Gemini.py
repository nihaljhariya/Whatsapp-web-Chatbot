import google.generativeai as genai

# Configure with your Gemini API key
genai.configure(api_key="__Your api Key of Gemini __")

# Chat history string (WhatsApp style)
command = '''

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
