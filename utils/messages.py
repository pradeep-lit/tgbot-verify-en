"""Message Templates"""
from config import CHANNEL_URL, VERIFY_COST, HELP_NOTION_URL


def get_welcome_message(full_name: str, invited_by: bool = False) -> str:
    """Get welcome message"""
    msg = (
        f"🎉 Welcome, {full_name}!\n"
        "You have successfully registered and received 1 credit.\n"
    )
    if invited_by:
        msg += "Thanks for joining via an invitation link. The inviter has received 2 credits.\n"

    msg += (
        "\nThis bot can automatically complete SheerID verification.\n"
        "Quick start:\n"
        "/about - Learn about the bot features\n"
        "/balance - Check your credit balance\n"
        "/help - View the full command list\n\n"
        "Get more credits:\n"
        "/qd - Daily check-in\n"
        "/invite - Invite friends\n"
        f"Join channel: {CHANNEL_URL}"
    )
    return msg


def get_about_message() -> str:
    """Get about message"""
    return (
        "🤖 SheerID Auto Verification Bot\n"
        "\n"
        "Features:\n"
        "- Automatically completes SheerID student/teacher verification\n"
        "- Supports Gemini One Pro, ChatGPT Teacher K12, Spotify Student, "
        "YouTube Student, Bolt.new Teacher verification\n"
        "\n"
        "How to earn credits:\n"
        "- 1 credit on registration\n"
        "- Daily check-in +1 credit\n"
        "- Invite friends +2 credits per person\n"
        "- Use redeem codes (based on code rules)\n"
        f"- Join channel: {CHANNEL_URL}\n"
        "\n"
        "How to use:\n"
        "1. Start verification on the website and copy the full verification link\n"
        "2. Send /verify, /verify2, /verify3, /verify4, or /verify5 with the link\n"
        "3. Wait for processing and check the result\n"
        "4. Bolt.new verification will automatically retrieve the verification code. "
        "For manual lookup, use /getV4Code <verification_id>\n"
        "\n"
        "Send /help to see more commands"
    )


def get_help_message(is_admin: bool = False) -> str:
    """Get help message"""
    msg = (
        "📖 SheerID Auto Verification Bot - Help\n"
        "\n"
        "User commands:\n"
        "/start - Start using the bot (register)\n"
        "/about - Learn about the bot features\n"
        "/balance - Check credit balance\n"
        "/qd - Daily check-in (+1 credit)\n"
        "/invite - Generate invite link (+2 credits per person)\n"
        "/use <code> - Redeem a code for credits\n"
        f"/verify <link> - Gemini One Pro verification (-{VERIFY_COST} credits)\n"
        f"/verify2 <link> - ChatGPT Teacher K12 verification (-{VERIFY_COST} credits)\n"
        f"/verify3 <link> - Spotify Student verification (-{VERIFY_COST} credits)\n"
        f"/verify4 <link> - Bolt.new Teacher verification (-{VERIFY_COST} credits)\n"
        f"/verify5 <link> - YouTube Student Premium verification (-{VERIFY_COST} credits)\n"
        "/getV4Code <verification_id> - Get Bolt.new verification code\n"
        "/help - View this help message\n"
        f"Check verification failures: {HELP_NOTION_URL}\n"
    )

    if is_admin:
        msg += (
            "\nAdmin commands:\n"
            "/addbalance <user_id> <credits> - Add credits to a user\n"
            "/block <user_id> - Block a user\n"
            "/white <user_id> - Unblock a user\n"
            "/blacklist - View blacklist\n"
            "/genkey <code> <credits> [uses] [days] - Generate redeem code\n"
            "/listkeys - View redeem code list\n"
            "/broadcast <text> - Broadcast a message to all users\n"
        )

    return msg


def get_insufficient_balance_message(current_balance: int) -> str:
    """Get insufficient balance message"""
    return (
        f"Insufficient credits! {VERIFY_COST} credits required, "
        f"current balance: {current_balance} credits.\n\n"
        "Ways to earn credits:\n"
        "- Daily check-in /qd\n"
        "- Invite friends /invite\n"
        "- Redeem a code /use <code>"
    )


def get_verify_usage_message(command: str, service_name: str) -> str:
    """Get verification command usage message"""
    return (
        f"Usage: {command} <SheerID link>\n\n"
        "Example:\n"
        f"{command} https://services.sheerid.com/verify/xxx/?verificationId=xxx\n\n"
        "How to get the verification link:\n"
        f"1. Visit the {service_name} verification page\n"
        "2. Start the verification process\n"
        "3. Copy the full URL from the browser address bar\n"
        f"4. Submit it using the {command} command"
    )
