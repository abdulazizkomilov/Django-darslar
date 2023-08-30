"""
 * Send an SMS message using the Infobip API.
 *
 * This example is already pre-populated with your account data:
 * 1. Your account Base URL
 * 2. Your account API key
 * 3. Your recipient phone number
 *
 * THIS CODE EXAMPLE IS READY BY DEFAULT. HIT RUN TO SEND THE MESSAGE!
 *
 * Send sms API reference: https://www.infobip.com/docs/api#channels/sms/send-sms-message
 * See Readme file for details.
"""
import random
from infobip_channels.sms.channel import SMSChannel

BASE_URL = "https://ejv5qn.api.infobip.com"
API_KEY = "505755f17769e60ae5b42f0595add8a2-fed04b6a-f25e-4bff-bc48-3ec9fef8c73a"
RECIPIENT = "998931159963"


def main():
    # Initialize the SMS channel with your credentials.
    channel = SMSChannel.from_auth_params(
        {
            "base_url": BASE_URL,
            "api_key": API_KEY,
        }
    )

    code = random.randint(10000, 99999)
    # Send a message with the desired fields.
    sms_response = channel.send_sms_message(
        {
            "messages": [
                {
                    "destinations": [{"to": RECIPIENT}],
                    # "text": "Your activate code: ",
                    "text": code,
                }
            ]
        }
    )
    print(sms_response)

    # Get delivery reports for the message. It may take a few seconds show the just-sent message.
    query_parameters = {"limit": 10}
    delivery_reports = channel.get_outbound_sms_delivery_reports(
        query_parameters)

    # See the delivery reports.
    print(delivery_reports)


if __name__ == "__main__":
    main()
