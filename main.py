import requests
import click

class SMS:
    def __init__(self, number, text):
        self.number = number
        self.text = text
        self.url = "https://textbelt.com/text"
        self.data = {
            "phone": self.number,
            "message": self.text,
            "key": "dcD6xFeFNpUxM4tEwsXxeOcnQ9Y8h1T1"  # Replace with>
        }

    def sendSMS(self):
        try:
            res = requests.post(self.url, data=self.data).json()
            if res.get('success'):
                click.secho("[+] Sent Message Successfully!", fg="gre>
            else:
                click.secho("[-] Couldn't Send Message!", fg="red")
                click.secho(f"[-] Error: {res.get('error', 'Unknown e>
        except requests.exceptions.RequestException as e:
            click.secho(f"[-] Network error: {e}", fg="red")

def main():
    try:
        number = click.prompt('Enter Number (Include country code)', >
        text = click.prompt('Enter Message', type=str)
    except KeyboardInterrupt:
        click.secho("\n[-] Good bye!", fg="red")
        exit(0)

    sms = SMS(number, text)
    if click.confirm('Do you want to send the message?'):
        sms.sendSMS()
    else:
        click.secho("[-] Message not sent. Good bye!", fg="red")

if __name__ == '__main__':
    main()
