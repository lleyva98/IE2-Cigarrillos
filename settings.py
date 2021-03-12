from os import environ

SESSION_CONFIGS = [
     dict(
        name='Quiz_1',
        display_name="Experimento_1.0",
        num_demo_participants=20,
            app_sequence=['Quiz_1', 'Choices', 'Quiz_2', 'Biases']
     ),
]

PARTICIPANT_FIELDS=['non_smoker','e1','e2','e3','e4']

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

use_browser_bots=True

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = ''
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'e#q61l4jlg%cm74dalj7((8!wrnno@b8jh072o+ip0n!%16!@3'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
