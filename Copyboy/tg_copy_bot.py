import os
import asyncio
from telethon import TelegramClient, events
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Function to get credentials
def get_credentials():
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')
    phone = os.getenv('PHONE')
    source_group_id = os.getenv('SOURCE_GROUP_ID')
    channel_id = os.getenv('CHANNEL_ID')

    if not all([api_id, api_hash, phone, source_group_id, channel_id]):
        print("Noen miljøvariabler mangler. Vennligst skriv inn dem:")
        api_id = input("API ID: ") or api_id
        api_hash = input("API Hash: ") or api_hash
        phone = input("Telefonnummer (med landskode, f.eks. +47xxxxxxxx): ") or phone
        source_group_id = input("Kilde gruppe-ID (f.eks. -1001234567890): ") or source_group_id
        channel_id = input("Kanal-ID (f.eks. -1001234567890): ") or channel_id

        # Save to .env for future use
        with open('.env', 'w') as f:
            f.write(f"API_ID={api_id}\n")
            f.write(f"API_HASH={api_hash}\n")
            f.write(f"PHONE={phone}\n")
            f.write(f"SOURCE_GROUP_ID={source_group_id}\n")
            f.write(f"CHANNEL_ID={channel_id}\n")
        print(".env-fil oppdatert!")

    return int(api_id), api_hash, phone, int(source_group_id), int(channel_id)

# Get credentials
API_ID, API_HASH, PHONE, SOURCE_GROUP_ID, CHANNEL_ID = get_credentials()

# Create the client
client = TelegramClient('session_name', API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_GROUP_ID))
async def handler(event):
    # Forward the message to the channel anonymously
    # This sends the message as the bot/user, without quoting the original
    await client.send_message(CHANNEL_ID, event.message)

async def main():
    await client.start(PHONE)
    print("Userbot kjører. Overvåker meldinger...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())