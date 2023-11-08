# import pyttsx3 as p
# import speech_recognition as sr
import re

# engine = p.init("sapi5")
# rate = engine.getProperty("rate")
# engine.setProperty("rate", 160)
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[1].id)
#

# Function to identify transfer info
def identify_transfer_info(sentence, bank_names):
    transfer_pattern = r'\b(Transfer|Send|Pay|Transaction|Wire)\b'
    # Update the account number pattern to match 10 digits with optional spaces
    account_number_pattern = r'\b\d{1}\s?\d{1}\s?\d{1}\s?\d{1}\s?\d{1}\s?\d{1}\s?\d{1}\s?\d{1}\s?\d{1}\s?\d{1}\b'
    amount_pattern = r'(\d+(?:,\d+)*(?:\.\d+)?) ?(?:naira\b)?'

    transfer_regex = re.compile(transfer_pattern, re.IGNORECASE)
    account_number_regex = re.compile(account_number_pattern)
    amount_regex = re.compile(amount_pattern, re.IGNORECASE)

    transfer_matches = transfer_regex.findall(sentence)
    account_number_matches = account_number_regex.findall(sentence)
    amount_matches = [match for match in amount_regex.findall(sentence) if match not in account_number_matches]
    if amount_matches:
        amount = amount_matches[0]
    else:
        amount = None  # or any other default value you prefer
    # Initialize the bank name as None
    bank_name = None

    bank_name_to_code = {
        "Guaranty Trust bank (GTB)": "058",
        "Access bank": "044",
        "Opay": "304",
        "9 Payment Solutions Bank": "12001",
        "AB microfinance bank": "090270",
        "Abbey Mortage Bank": "070010",
        "Above Only Microfinance bank": "090260",
        "ABU microfinance bank": "090197",
        "Access money": "927",
        "Access yello & beta": "100052",
        "Accion Microfinance bank": "090134",
        "United bank for Africa plc": "033",
        "Union bank": "032",
        "VFD microfinance bank": "566",
        "Wema bank": "035",
        "Zenith bank": "057",
        "Unity bank plc": "215",
        "Palmpay": "100033",
        "Parallex": "907",
        "Paga": "100002"

    }

    bank_code = ""

    # Check for bank names in the sentence
    for primary_name, *aliases in bank_names:
        bank_variations = [re.escape(primary_name)] + [re.escape(alt) for alt in aliases]
        bank_regex = fr'\b(?:{"|".join(bank_variations)})\b'
        if re.search(bank_regex, sentence, re.IGNORECASE):
            bank_name = primary_name
            bank_code = bank_name_to_code.get(bank_name, "")  # Get the corresponding bank code

            break  # Exit the loop once the first match is found

    result = {
        # "Transfer/Send": transfer_matches,
        "destAccountNo": "".join(account_number_matches),
        "amount": amount_matches[0],
        "bankName": bank_name,
        "bankCode" : bank_code,
        "Text": sentence  # Add the spoken text to the result
    }


    return result

#
# # Function to capture spoken text using speech recognition
# def capture_spoken_text():
#     r = sr.Recognizer()
#
#     with sr.Microphone() as source:
#         r.energy_threshold = 10000
#         r.adjust_for_ambient_noise(source, 0.7)
#         print("Listening....")
#
#         try:
#             audio = r.listen(source, timeout=90)  # Capture audio for up to 90 seconds
#             text = r.recognize_google(audio)
#             # print("You said:", text)  # Print the captured spoken text
#             return text
#
#         except sr.WaitTimeoutError:
#             print("Listening stopped. Enter text manually.")
#             return input("Enter text: ")
#         except sr.UnknownValueError:
#             print("Could not understand the audio. Enter text manually.")
#             return input("Enter text: ")
#
# def capture_audio(audio):
#     try:
#         audio = r.listen(source, timeout=90)  # Capture audio for up to 90 seconds
#         text = r.recognize_google(audio)
#         # print("You said:", text)  # Print the captured spoken text
#         return text
#     except:
#         return "Error Occured"
#

# Main program
# user_input = input("Enter text: ")

bank_name_list = [
    ("Access bank", "Access Bank", "ABank"),
    ("Guaranty Trust bank (GTB)", "GTB", "Guaranty Trust Bank", "GT Bank", "Guaranty Trust", "gtbank", "gt bank"),
    ("Opay", "opay"),
    ("9 Payment Solutions Bank", "9 PAYMENT SOLUTIONS BANK", "9Payment", "9 Payment"),
    ("AB microfinance bank", "AB MICROFINANCE BANK","ABMFB"),
    ("Abbey Mortage Bank", "ABBEY MORTAGE BANK"),
    ("Above Only Microfinance bank", "ABOVE ONLY MICROFINANCE BANK"),
    ("ABU microfinance bank", "ABU MICROFINANCE BANK", "ABUMFB"),
    ("Access money", "ACCESS MONEY"),
    ("Access yello & beta", "Access yello", "ACCESS YELLO & BETA"),
    ("United bank for Africa plc", "UNITED BANK FOR AFRICA", "UBA", "united bank"),
    ("Accion microfinance bank", "ACCION MICROFINANCE BANK", "ACCIONMFB"),
    ("Union bank", "UNION", "UNION BANK"),
    ("VFD microfinance bank", "VFDMFB"),
    ("Wema bank", "wema"),
    ("Zenith bank", "zenith"),
    ("Unity bank plc", "Unity", "unity bank"),
    ("Parallex", "parallex"),
    ("Paga", "paga"),
    ("Palmpay", "Palm pay")

]
#
# result = identify_transfer_info(user_input, bank_name_list)
# #
# #Remove spaces from the account number
# account_number = "".join(result["destAccountNo"])
# result["destAccountNo"] = account_number
#
# # Display the results in the specified format
# print(result)

# engine.say("Transfer information identified.")
# engine.runAndWait()
