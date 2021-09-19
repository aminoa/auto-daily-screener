# auto-daily-screener

This is the first finished version of the Auto Daily Screener. It navigates through the NYU login pages and then generate the codes to successfully automate the login process. It is currently unfinished. The relevant files are the ads.py and the settings.py. 

# Codes Generation Documentation:
When DUO mobile gives a mobile URL to use, ads.py strips the url into a domain and key. The script sends a request to the DUO url and then generates an HOTP secret. After, the secret is convert to UTF-8 from ASCII and then an HOTP is generated using pyotp. Finally, a code is generated from the hotp.

Credit to Bye DUO and DUO Bypass for the codes generation. Made with Selenium and QT.