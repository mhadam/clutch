from pydantic import BaseModel


class Stats(BaseModel):
    uploaded_bytes: int
    downloaded_bytes: int
    files_added: int
    session_count: int
    seconds_active: int


class SessionStats(BaseModel):
    active_torrent_count: int
    download_speed: int
    paused_torrent_count: int
    torrent_count: int
    upload_speed: int
    cumulative_stats: Stats
    current_stats: Stats
