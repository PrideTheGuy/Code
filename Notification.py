# Function to send the SMS messages
def send_sms():
    client = Client(account_sid, auth_token)
    phone_numbers = entry_phone_numbers.get().split(',')  # Extract phone numbers from the entry field
    message_body = entry_message_body.get()

    for phone_number in phone_numbers:
        message = client.messages.create(
            body=message_body,
            from_=twilio_phone_number,
            to=phone_number.strip()
        )
        output_text.insert(tk.END, f"SMS sent to {phone_number.strip()}: {message.sid}\n")

# Create the main window
window = tk.Tk()
window.title("Twilio SMS Integration")
window.geometry("400x300")

# Create labels and entry fields
label_phone_numbers = tk.Label(window, text="Phone Numbers (comma-separated):")
label_phone_numbers.pack()
entry_phone_numbers = tk.Entry(window)
entry_phone_numbers.pack()

label_message_body = tk.Label(window, text="Message Body:")
label_message_body.pack()
entry_message_body = tk.Entry(window)
entry_message_body.pack()

# Create a button to send the SMS messages
button_send_sms = tk.Button(window, text="Send SMS", command=send_sms)
button_send_sms.pack()

# Create a text widget to display the output
output_text = tk.Text(window, height=10, width=40)
output_text.pack()

# Start the GUI event loop
window.mainloop()

