from flask import Flask, request, Response  
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings 
from botbuilder.schema import Activity 
from config import Config
from bot import MyBot

app = Flask(__name__)

# Bot settings and adapter
config = Config()
adapter_settings = BotFrameworkAdapterSettings(config.APP_ID, config.APP_PASSWORD)
adapter = BotFrameworkAdapter(adapter_settings)
bot = MyBot()

@app.route("/api/messages", methods=["POST"])
def messages():
    if "application/json" in request.headers["Content-Type"]:
        body = request.json
    else:
        return Response(status=415)

    activity = Activity().deserialize(body)
    auth_header = request.headers.get("Authorization", "")

    async def call_bot_logic():
        await adapter.process_activity(activity, auth_header, bot.on_turn)

    try:
        import asyncio
        loop = asyncio.get_event_loop()
        loop.run_until_complete(call_bot_logic())
        return Response(status=200)
    except Exception as e:
        print(f"Error: {e}")
        return Response(status=500)

if __name__ == "__main__":
    app.run(port=config.PORT)
