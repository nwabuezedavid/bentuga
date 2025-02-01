import smtplib

try:
    server = smtplib.SMTP("chestburgbank.com", 465)
    server.starttls()  # ✅ Important for TLS
    server.login("support@chestburgbank.com", "nwabueze666$")
    server.sendmail(
        "support@chestburgbank.com",
        "nwabuezedavid666@gmail.com",
        "Subject: Test Email\n\nHello, this is a test email."
    )
    server.quit()
    print("✅ Email sent successfully!")
except Exception as e:
    print(f"❌ Error: {e}")
