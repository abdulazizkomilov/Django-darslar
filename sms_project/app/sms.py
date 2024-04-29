import random
from infobip_channels.sms.channel import SMSChannel

BASE_URL = "https://ejv5qn.api.infobip.com"
API_KEY = "30a84cc24821da0deb651478d0ba6716-8caed106-3383-4182-b146-4a3fdefae2bd"
RECIPIENT = "998997623107"

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
