import smtplib
import os
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load credentials
load_dotenv()
SENDER_EMAIL = os.getenv("EMAIL_USER")
APP_PASSWORD = os.getenv("EMAIL_PASS")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

def clean_markdown(text):
    """
    Removes hashtags and underscores, but PRESERVES double asterisks 
    so we can convert them to bold later.
    """
    # Remove hashtags
    text = re.sub(r'#+', '', text)
    # Remove underscores
    text = text.replace('_', '')
    return text.strip()

def send_email(subject, body):
    """
    Sends the news briefing with a clean design, larger font, and bold mini-headers.
    """
    if not SENDER_EMAIL or not APP_PASSWORD:
        print("Error: Email credentials not found in .env file.")
        return

    message = MIMEMultipart()
    message["From"] = f"Intelligence Daily <{SENDER_EMAIL}>"
    message["To"] = RECEIVER_EMAIL
    message["Subject"] = subject

    # Format the body into clean HTML sections
    sections = body.split('## ')
    html_content = ""
    
    # Intro
    intro = sections[0].strip().replace('\n', '<br>')
    html_content += f'<div style="font-size: 16px; color: #555; margin-bottom: 30px; line-height: 1.6;">{intro}</div>'
    
    for section in sections[1:]:
        lines = section.split('\n')
        header = clean_markdown(lines[0].replace('*', '')) # Clean header
        content_lines = lines[1:]
        
        list_items = ""
        for line in content_lines:
            line = line.strip()
            if line:
                # 1. Clean basic markdown
                clean_line = clean_markdown(line)
                # 2. Remove the leading asterisk if it exists
                clean_line = re.sub(r'^[*-]\s*', '', clean_line)
                # 3. Convert **text:** into <b>text:</b>
                clean_line = re.sub(r'\*\*(.*?)\*\*', r'<b style="color: #000;">\1</b>', clean_line)
                
                if clean_line:
                    list_items += f'<li style="margin-bottom: 15px; line-height: 1.7;">{clean_line}</li>'

        if list_items:
            html_content += f"""
            <div style="margin-bottom: 40px;">
                <div style="font-size: 14px; font-weight: bold; color: #000; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 18px; border-bottom: 1px solid #eee; padding-bottom: 8px;">{header}</div>
                <ul style="padding-left: 20px; margin: 0; font-size: 16px; color: #333;">{list_items}</ul>
            </div>
            """

    # Final HTML Wrapper
    html_body = f"""
    <html>
    <body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #ffffff; color: #333; margin: 0; padding: 40px 20px;">
        <div style="max-width: 650px; margin: 0 auto;">
            <div style="border-bottom: 2px solid #000; padding-bottom: 15px; margin-bottom: 35px;">
                <h1 style="font-size: 28px; font-weight: bold; margin: 0; letter-spacing: -0.5px;">Intelligence Daily</h1>
                <p style="font-size: 12px; color: #999; margin: 5px 0 0; text-transform: uppercase; letter-spacing: 2px;">{subject}</p>
            </div>
            {html_content}
            <div style="margin-top: 60px; border-top: 1px solid #eee; padding-top: 20px; text-align: center; font-size: 11px; color: #bbb; text-transform: uppercase; letter-spacing: 2px;">
                Automated Intelligence • Portfolio V2.5 • Simple English Edition
            </div>
        </div>
    </body>
    </html>
    """
    message.attach(MIMEText(html_body, "html"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        text = message.as_string()
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, text)
        server.quit()
        print("✅ Premium Simple-English Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email. Error: {e}")

if __name__ == "__main__":
    send_email("Intelligence Daily - May 08, 2026", "## TOP STORIES\n* **Big News:** This is a test. (Source: TC)")
