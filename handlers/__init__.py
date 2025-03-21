from .music_handler import register_handlers as register_music
from .admin_handler import register_handlers as register_admin
from .ai_chat_handler import register_handlers as register_ai
from .games_handler import register_handlers as register_games
from .effects_handler import register_handlers as register_effects
from .auth_handler import register_handlers as register_auth

def register_all_handlers(app, call_py):
    register_music(app, call_py)
    register_admin(app, call_py)
    register_ai(app)
    register_games(app)
    register_effects(app, call_py)
    register_auth(app)