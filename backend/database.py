from supabase import create_client, Client
from .config import SUPABASE_KEY,SUPABASE_URL

class Database:
    _client: Client = None
    @classmethod
    def get_client(cls) -> Client:
        if cls._client is None:
            cls._client = create_client(SUPABASE_URL, SUPABASE_KEY)
        return cls._client


