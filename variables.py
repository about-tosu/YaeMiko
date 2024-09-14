# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 6433468  # Get this value from my.telegram.org/apps
    API_HASH = "7895dfd061f656367ccab30032"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://ierjlkr:OG4dxzO67Zret3Zii43Hhvujkg89WVry0n9KsHE@karma.db.elephantsql.com/ierjlkr"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1002023182491
    MESSAGE_DUMP = -1002023182491

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://botmaker9675208:botmaker9675208@cluster0.sc9mq8b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Support chat and support ID
    SUPPORT_CHAT = "nothing_bots_support"
    SUPPORT_ID = -1002084958808

    # Database name
    DB_NAME = "cluster0"

    # Bot token
    TOKEN = "7040644595:AAGeIzCxS1WyZD8omiOzT98zXft5NCXSCSE"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 6848223695
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = []  # Sudo users
    DEV_USERS = []  # Dev users
    DEMONS = []  # Support users
    TIGERS = []  # Tiger users
    WOLVES = []  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
