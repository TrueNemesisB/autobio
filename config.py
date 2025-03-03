from modules import *

SESSION_NAME = 'session'

API_ID = 1890553
API_HASH = 'c6f46b5330f5953e5201c3185337ed73'

# https://developer.brawlstars.com/
BRAWLSTARS_TOKEN = ''

# http://www.last.fm/api/account/create
LASTFM_KEY = '50c4da48aa16885c9e91a6d417d601e7'  # usable example key
LASTFM_USERNAME = ''  # enter your last.fm username

MODULES = {
    # Current time
    'time': Time('%H:%M'),

    # Number of blocked accounts
    #'blocked': BlockedCount(),

    # Number of channel or group members
    'members': MembersCount(''),

    # About of the entity
    #'about': EntityInfo('True_Alexey'),

    # BrawlStars Trophies by tag
    #'trophies': BrawlStarsTrophies('', BRAWLSTARS_TOKEN),

    # Iterates strings
    'first_name': Cycle('АлексейВеликий', 'ņиʞиvǝʚņǝɔʞǝvɐ'),

    # LastFM now playing
    #'music': LastFm(LASTFM_KEY, LASTFM_USERNAME, 'nothing is playing now')
}

INTERVAL = 30

TEMPLATES = {
    'about': '⌛: $time$time$time$time$time',
    'first_name': '$first_name',
    'last_name': None
}
