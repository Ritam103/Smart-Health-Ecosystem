# ai-service/chatbot.py
def get_response(user_input):
    user_input = user_input.lower().strip()
    
    # Symptom checks
    if "fever" in user_input or "hot" in user_input:
        return "Rest, drink water, and monitor your temperature. If above 100.4°F (38°C) for over 24 hours, see a doctor."
    elif "cough" in user_input:
        return "Stay hydrated and rest. Persistent cough? Consult a healthcare provider."
    elif "heart rate" in user_input or "pulse" in user_input:
        return "Normal range is 60-100 bpm. Enter your value (e.g., 'My heart rate is 120') for advice."
    elif "my heart rate is" in user_input:
        try:
            hr = int(''.join(filter(str.isdigit, user_input)))
            if hr > 100:
                return "Your heart rate is high. Rest and check again. If it persists, seek medical help."
            elif hr < 60:
                return "Your heart rate is low. If you feel dizzy, see a doctor."
            else:
                return "Your heart rate is normal."
        except ValueError:
            return "Please provide a number (e.g., 'My heart rate is 80')."
    # Emergency
    elif "chest pain" in user_input or "can’t breathe" in user_input:
        return "This could be serious. Call emergency services now."
    # General
    elif "hello" in user_input or "hi" in user_input:
        return "Hi! How can I assist you with your health today?"
    else:
        return "Sorry, I’m not sure how to help with that. Try asking about symptoms or vitals."
