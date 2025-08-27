templates = [
    'BACKEND':'django.template.backends.django.DjangoTemplates',
    'DIRS':[],
    'APP_DIRS':True,
    'OPTIONS':{
        'CONTEXT_PROCESSORS':[
            'Django.template.context_processors.debug',
            'django.template.context_processor.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',

            'home.context_processors.restaurant_name'
        ]
    }
]