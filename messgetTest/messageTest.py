from slackclient import SlackClient

slack_token = os.environ["SLACK_API_TOKEN"]
#slack_token = 'xoxb-321298797442-p2JAZKIGLJL5aEc526RX8rAw'
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="#general",
  text="Hello from Python!"
)
