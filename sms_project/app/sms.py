import random
from infobip_channels.sms.channel import SMSChannel

BASE_URL = "https://ejv5qn.api.infobip.com"
API_KEY = "42b9f560b55c522dc7fbaae99a4a4704-84519654-62f4-4297-9e26-835d8ec2d3a1"
RECIPIENT = "998938452244"

def main():
    channel = SMSChannel.from_auth_params(
        {
            "base_url": BASE_URL,
            "api_key": API_KEY,
        }
    )
    code = random.randint(10000, 99999)
    sms_response = channel.send_sms_message(
        {
            "messages": [
                {
                    "destinations": [{"to": RECIPIENT}],
                    "text": code,
                }
            ]
        }
    )
    query_parameters = {"limit": 10}
    delivery_reports = channel.get_outbound_sms_delivery_reports(
        query_parameters)

if __name__ == "__main__":
    main()
