from twilio.rest import Client


acccount_id = "aoioreworue"
auth_token = "isoiewr8jwhrew"

client = Client(acccount_id,auth_token)
call = client.messages.create(
    to = "....",
    from_ ='.....',
    body = "this is our first message"
)