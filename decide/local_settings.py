ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

BASE_URL = 'http://localhost:8000'

APIS = {
    'authentication': BASE_URL,
    'base': BASE_URL,
    'booth': BASE_URL,
    'census': BASE_URL,
    'mixnet': BASE_URL,
    'postproc': BASE_URL,
    'store': BASE_URL,
    'visualizer': BASE_URL,
    'voting': BASE_URL,
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'examen',
        'USER': 'examen',
        'PASSWORD': 'examen',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
