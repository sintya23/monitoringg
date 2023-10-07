import requests
import smtplib
from email.message import EmailMessage


# URL yang ingin diperiksa
url = "https://homeaccess.net.id/"

# Lakukan permintaan HTTP untuk memeriksa status kode
response = requests.get(url)

 # Mengirim notifikasi lewat email
email_address = "sintyakumara191005@gmail.com"  # Email pengirim
email_password = "dnihcazejglzsddt"  # Kata sandi email pengirim
recipient_address = "sintyakumara191005@gmail.com"  # Email penerima

# Fungsi untuk mengirim notifikasi email
def kirim_notifikasi(email_address, email_password, recipient_address, subject, message):
    # Membuat pesan email
    msg = EmailMessage()
    msg.set_content(message)
    msg["Subject"] = subject
    msg["From"] = email_address
    msg["To"] = recipient_address

    # Mengirim email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Server SMTP dan port
        server.starttls()  # Mengenkripsi koneksi
        server.login(email_address, email_password)  # Login ke email pengirim
        server.send_message(msg)  # Mengirim pesan email
        server.quit()  # Keluar dari server
        print("Notifikasi email telah dikirim.")
    except Exception as e:
        print(f"Gagal mengirim email: {e}")

    if response.status_code >= 190 or response.status_code < 200: pesan = f"Situs web {url} tidak dapat diakses. Status code: {response.status_code}"
    kirim_notifikasi(email_address, email_password, recipient_address, "Notifikasi Situs Web Tidak Dapat Diakses", pesan)