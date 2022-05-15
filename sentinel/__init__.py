__app_name__ = "sentinel-cli"
__version__ = '0.1.0'
__host_url__ = "https://backend.hestiatkmce.live"
(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    AUTHORIZATION_ERROR,
) = range(7)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    DB_READ_ERROR: "database read error",
    DB_WRITE_ERROR: "database write error",
    AUTHORIZATION_ERROR: "NE01:Invalid authorization header",
}
