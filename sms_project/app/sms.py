import random
from infobip_channels.sms.channel import SMSChannel

BASE_URL = "https://ejv5qn.api.infobip.com"
API_KEY = "53dced0dd1a30ff10e2d6e60d960ddcb-4bd15999-8ffd-4acf-83e4-f929980abdb4"
RECIPIENT = "998505765066"

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
    print(code)
    print(sms_response)
    print(delivery_reports)

if __name__ == "__main__":
    main()
