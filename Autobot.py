import pyautogui
import time
import pyperclip
import google.generativeai as genai

# ✅ Gemini API Key
genai.configure(api_key="__Your api Key of Gemini __")  # Replace with your key
model = genai.GenerativeModel("gemini-1.5-flash")

# ✅ Keep track of last message
last_replied_message = ""

# ✅ Extract last message from Papa ❤️
def get_last_message_from_papa(chat_log, sender_name="Papa ❤️"):
    messages = chat_log.strip().split("[2024] ")
    for msg in reversed(messages):
        if sender_name in msg:
            parts = msg.split(":")
            if len(parts) > 1:
                return parts[-1].strip()
    return None

# ✅ Detect if message is a coding request
def is_code_request(message):
    keywords = ["code", "program", "python", "c++", "cpp", "java", "add", "sum", "function"]
    return any(word in message.lower() for word in keywords)

# ✅ Open WhatsApp (once)
pyautogui.click(909, 1050)
time.sleep(2)

# ✅ Start loop
while True:
    try:
        time.sleep(10)

        # Copy chat
        pyautogui.moveTo(727, 226)
        pyautogui.dragTo(1848, 919, duration=2.0)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        chat_history = pyperclip.paste()

        if not chat_history.strip():
            print("❌ Could not copy chat.")
            continue

        last_msg = get_last_message_from_papa(chat_history)

        if last_msg and last_msg != last_replied_message:
            print("🧾 Last:", repr(last_msg))
            last_replied_message = last_msg

            if is_code_request(last_msg):
                prompt = f"Papa asked: \"{last_msg}\"\n\nYou are Ayush. Reply directly with the exact Python or C++ code. Do not joke or delay. Give clean code only."
            else:
                prompt = (
                    f"Papa said: \"{last_msg}\"\n\n"
                    "You are Ayush. Respond in 1-2 lines of Hinglish (Hindi + English). Be respectful. No emojis, no timestamps."
                )

            response = model.generate_content(prompt)
            reply = response.text.strip()

            pyperclip.copy(reply)
            pyautogui.click(841, 976)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            pyautogui.press('enter')

            print("✅ Replied to:", last_msg)
        else:
            print("⏳ No new message from Papa. Waiting...")

    except Exception as e:
        print("❌ Error occurred:", e)
        time.sleep(5)
