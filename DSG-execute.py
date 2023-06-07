import discord


GUILD_ID = 1234567890 
USER_IDS = [1111111111, 2222222222]  

intents = discord.Intents.default()
intents.invites = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    guild = client.get_guild(GUILD_ID)
    if guild is None:
        print(f"Bot is not a member of the specified guild ID: {GUILD_ID}")
        return

    for user_id in USER_IDS:
        try:
            user = await client.fetch_user(user_id)
            invite = await guild.invites().flatten()
            if invite:
                invite_link = invite[0].url
                await user.send(f"You've been invited to join the server! {invite_link}")
                print(f"Invitation sent to user ID: {user_id}")
            else:
                print("No invite link found for the server.")
        except discord.errors.Forbidden:
            print(f"Unable to send invite to user ID: {user_id}")



