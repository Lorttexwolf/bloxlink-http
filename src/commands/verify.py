from unicodedata import category
from snowfin import Module, slash_command, slash_option, Interaction, Button, Choice
from resources.bloxlink import Bloxlink

class VerifyCommand(Module):
    category = "Account"

    @slash_command("verify")
    async def verify(self, ctx: Interaction):
        """link your Roblox account to your Discord account and get your server roles"""

        return (
            "To verify with Bloxlink, click the link below",
            Button("Verify with Bloxlink", url="https://blox.link/dashboard/verifications/verify?page=username", emoji="🔗"),
            Button("Stuck? See a Tutorial", url="https://www.youtube.com/watch?v=0SH3n8rY9Fg&list=PLz7SOP-guESE1V6ywCCLc1IQWiLURSvBE&index=2", emoji="❔")
        )

    @slash_command("verifyall")
    @slash_option("update", "Would you like to update member's roles, nicknames, or both?", type=3,
        choices=[Choice("Roles", "roles"), Choice("Nicknames", "nicknames"), Choice("Both", "both")],
        required=True
    )
    async def verifyall(self, ctx: Interaction, update: str):
        """force update everyone in the server"""

        return "This command is not yet implemented. This will require probably sending an event to a websocket node since it's not possible to chunk a server through the API."

