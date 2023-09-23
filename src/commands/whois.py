from hikari.commands import CommandOption, OptionType
from hikari import ButtonStyle, KnownCustomEmoji, Emoji, Color
import sentry_sdk

import resources.users as users
from resources.bloxlink import instance as bloxlink
from resources.models import CommandContext
from resources.exceptions import UserNotVerified
from resources.utils import fetch
from resources.exceptions import RobloxNotFound


@bloxlink.command(
    category="Account",
    defer=True,
    options=[
        CommandOption(
            type=OptionType.USER,
            name="user",
            description="Retrieve the Roblox information of this user",
            is_required=False,
        )
    ],
)
class WhoisCommand:
    """Retrieve the Roblox information of a user."""

    async def __main__(self, ctx: CommandContext):      
        target_user = list(ctx.resolved.users.values())[0] if ctx.resolved else ctx.member
        
        try:
            roblox_account = await users.get_user(target_user, ["value"])
            
        except UserNotVerified:
            if target_user == ctx.member:
                raise UserNotVerified("You are not verified with Bloxlink!")
            else:
                raise UserNotVerified("This user is not verified with Bloxlink!")
        
        is_online = False
        # try:
        #     # TODO: Implement activity into the Roblox server.
        #     # status, req = await fetch("GET", f"https://api.roblox.com/users/{roblox_account.id}/onlinestatus/", raise_on_failure=False)
        #     is_online: bool = status["IsOnline"] if req.status == 200 else False
        # except Exception: 
        #     raise RobloxNotFound()
        
        info_embed, components = await users.format_embed(roblox_account, target_user)       
            
        await ctx.response.send(embed=info_embed, components=components)