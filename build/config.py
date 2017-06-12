# imports - standard imports
import os

# imports - third-party imports
import addict

# imports - module imports
from build.util import pardir, relurljoin, unique_id

CONFIG                                      = addict.Dict()

CONFIG.environment                          = os.getenv('WEBDEV_ENV', 'development')
CONFIG.exclude                              = [
    'Gemfile',
    'Gemfile.lock',
    'requirements',
    'requirements.txt',
    'build',
    'Makefile',
    'LICENSE',
    'README.md',
    'TODO.md'
]
CONFIG.sass.style                           = 'compressed'
CONFIG.gems                                 = [
    'jekyll-seo-tag'
]

# paths
CONFIG.path.root                            = pardir(__file__, 2)
CONFIG.path.assets                          = os.path.join(CONFIG.path.root, 'assets')
CONFIG.path.images                          = os.path.join(CONFIG.path.assets,  'img')

# brand
CONFIG.brand.name                           = 'Hugo Guel'
CONFIG.brand.email                          = 'hugoguelartist@gmail.com'
CONFIG.brand.phone                          = '+18322160282'
CONFIG.brand.description                    = "Official Website of Artist Hugo Guel. Discover a collection of Hugo Guel's most prominent artworks."
CONFIG.brand.social.facebook                = 'https://www.facebook.com/Club-de-Arte-Latino-Americano-Artista-Hugo-Guel-211925969251288'

# URLs
CONFIG.url                                  = 'hugoguel.com'
CONFIG.baseurl                              = '/'
CONFIG.urls.assets                          = relurljoin(CONFIG.baseurl,    'assets')
CONFIG.urls.data                            = relurljoin(CONFIG.urls.assets,  'data')
CONFIG.urls.images                          = relurljoin(CONFIG.urls.assets,   'img')
CONFIG.urls.icons                           = relurljoin(CONFIG.urls.images, 'icons')

CONFIG.lang                                 = 'en'

# colors
CONFIG.color.primary                        = '#464A47'
CONFIG.color.accent                         = '#EDE9E0'

# navbar
CONFIG.data.navbar.links                    = [
    { 'title': 'Home',        'url': CONFIG.baseurl },
    { 'title': 'Biography',   'url': relurljoin(CONFIG.baseurl,   '#biography') },
    { 'title': 'CV', 'dropdown': True, 'menu': [
            { 'title': 'English', 'url': relurljoin(CONFIG.urls.data, 'Hugo-Guel-CV-en.pdf') },
            { 'title': 'Spanish', 'url': relurljoin(CONFIG.urls.data, 'Hugo-Guel-CV-es.pdf') }
        ]
    },
    { 'title': 'Exhibitions', 'url': relurljoin(CONFIG.baseurl,   'exhibitions.html') },
    { 'title': 'Portfolio',   'url': relurljoin(CONFIG.baseurl,   '#portfolio') },
    { 'title': 'Store',       'url': relurljoin(CONFIG.baseurl,   'store.html') },
    { 'title': 'Contact',     'url': relurljoin(CONFIG.baseurl,   'contact.html') }
]

CONFIG.data.about.paragraphs                = [
    """Hugo Guel the Artist was born January 16, 1963, in Nueva Rosita, Coahuila, Mexico, the second of five children. He witnessed a huge mine explosion when he was six and drew a picture of a mother mourning the death of her son. He pursued his talents as an artist and received his first public attention at eighteen when he won first place twice in the CONACUR painting and drawing competition in Saltillo, Coahuila. He achieved his first commercial success with murals displayed in government offices, schools and hospitals during the period of 1983 to 1988, and explored other media such as reliefs and sculptures in wood, iron, bronze, and aluminum, including the 23 foot high iron sculpture of an eagle eating a snake which welcomes visitors to Morelos, Coahuila. He currently produces works for the Laurenzo’s family restaurants, in Houston, Texas."""
]

CONFIG.data.images.gallery                  = [
    {
        'src': relurljoin(CONFIG.urls.images, 'gallery', filename)
    }
    for filename in os.listdir(os.path.join(CONFIG.path.images, 'gallery'))
]

CONFIG.data.thumbnails.portfolio            = [
    {
        'title': 'Paintings',
        'image': { 'src': relurljoin(CONFIG.urls.images, 'portfolio', 'thumbnails', 'paintings.jpg') },
          'url': relurljoin(CONFIG.baseurl, 'portfolio', 'paintings.html')
    },
    {
        'title': 'Murals',
        'image': { 'src': relurljoin(CONFIG.urls.images, 'portfolio', 'thumbnails', 'murals.jpg') },
          'url': relurljoin(CONFIG.baseurl, 'portfolio', 'murals.html')
    },
    {
        'title': 'Commercial',
        'image': { 'src': relurljoin(CONFIG.urls.images, 'portfolio', 'thumbnails', 'commercial.jpg') },
          'url': relurljoin(CONFIG.baseurl, 'portfolio', 'commercial')
    },
    {
        'title': 'Sculptures',
        'image': { 'src': relurljoin(CONFIG.urls.images, 'portfolio', 'thumbnails', 'sculptures.jpg') },
          'url': relurljoin(CONFIG.baseurl, 'portfolio', 'sculptures.html')
    }
]

CONFIG.data.timelines.timeline              = [
    {
        'date': { 'year': '1963' },
        'content': 'Born in México'
    },
    {
        'date': { 'year': '1981' },
        'content': 'Won the first place in Conacur painting and drawing competition'
    },
    {
        'date': { 'year': '1984' },
        'content': 'Moved to Houston, Texas'
    },
    {
        'date': { 'year': '1993' },
        'content': '23-foot-high iron sculpture of an eagle eating a serpent in Nueva Rosita, Coahuila'
    },
    {
        'date': { 'year': '1995' },
        'content': '“Águila Mexicana” a 22-foot-high stainless steel Morelos, Coahuila'
    },
    {
        'date': { 'year': '2002' },
        'content': 'A series of murals for PASAC Dinosaur exhibition for the Region Carbonifera Natural History Museum in Coahuila, México'
    }
]

CONFIG.data.timelines.exhibition            = [
    {
        'date': { 'year': '1984' },
        'content': 'Pictorial Exposition in Astro Feria, Rosita'
    },
    {
        'date': { 'year': '1988' },
        'content': 'Pictorial Exposition in the Galleria, Houston, Texas'
    },
    {
        'date': { 'year': '1989' },
        'content': 'Pictorial Exposition, Regional Delegation of INSTITUTE DEL SEGURO SOCIAL, in Monterrey, N.L Mexico'
    },
    {
        'date': { 'year': '1991' },
        'content': 'Pictorial Exhibition  “Nueva Rosita, de Noche” and “Santa Prisca” in Acuña, Coahuila, in Nueva Rosita, Coahuila'
    }
]

CONFIG.data.images.paintings                = [ ]
basepath                                    = os.path.join(CONFIG.path.images, 'portfolio', 'paintings')
for filename in os.listdir(basepath):
    path = os.path.join(basepath, filename)
    if not os.path.isdir(path):
        CONFIG.data.images.paintings.append({
            'src': relurljoin(CONFIG.urls.images, 'portfolio', 'paintings', filename)
        })

CONFIG.data.images.murals                   = [ ]
basepath                                    = os.path.join(CONFIG.path.images, 'portfolio', 'murals')
for filename in os.listdir(basepath):
    path = os.path.join(basepath, filename)
    if not os.path.isdir(path):
        CONFIG.data.images.murals.append({
            'src': relurljoin(CONFIG.urls.images, 'portfolio', 'murals', filename)
        })

CONFIG.data.breadcrumbs.portfolio           = [
    {
        'title': 'Portfolio',
          'url': relurljoin(CONFIG.baseurl, '#portfolio')
    }
]

CONFIG.data.breadcrumbs.commercial          = CONFIG.data.breadcrumbs.portfolio + [
    {
        'title': 'Commercial',
          'url': relurljoin(CONFIG.baseurl, 'portfolio', 'commercial')
    }
]

CONFIG.data.thumbnails.commercial           = [
    {
        'title': 'PASAC',
        'image': { 'src': relurljoin(CONFIG.urls.images, 'portfolio', 'commercial', 'thumbnails', 'pasac.jpg') },
          'url':  relurljoin(CONFIG.baseurl, 'portfolio', 'commercial', 'pasac.html')
    },
    {
        'title': "Laurenzo's El Tiempo Cantina",
        'image': { 'src': relurljoin(CONFIG.urls.images, 'portfolio', 'commercial', 'thumbnails', 'laurenzo.jpg') },
          'url':  relurljoin(CONFIG.baseurl, 'portfolio', 'commercial', 'laurenzo.html')
    }
]

CONFIG.data.breadcrumbs.pasac               = CONFIG.data.breadcrumbs.commercial + [
    {
        'title': 'PASAC',
          'url': relurljoin(CONFIG.baseurl, 'portfolio', 'commercial', 'pasac')
    }
]

CONFIG.data.images.pasac                    = [ ]
basepath                                    = os.path.join(CONFIG.path.images, 'portfolio', 'commercial', 'pasac')
for filename in os.listdir(basepath):
    path = os.path.join(basepath, filename)
    if not os.path.isdir(path):
        CONFIG.data.images.pasac.append({
            'src': relurljoin(CONFIG.urls.images, 'portfolio', 'commercial', 'pasac', filename),
            'preview': { 'src': relurljoin(CONFIG.urls.images, 'portfolio', 'commercial', 'pasac', 'preview', filename) }
        })

CONFIG.data.breadcrumbs.laurenzo            = CONFIG.data.breadcrumbs.commercial + [
    {
        'title': "Laurenzo's El Tiempo Cantina",
          'url': relurljoin(CONFIG.baseurl, 'portfolio', 'commercial', 'laurenzo')
    }
]

CONFIG.data.images.laurenzo                 = [ ]
basepath                                    = os.path.join(CONFIG.path.images, 'portfolio', 'commercial', 'laurenzo')
for filename in os.listdir(basepath):
    path = os.path.join(basepath, filename)
    if not os.path.isdir(path):
        CONFIG.data.images.laurenzo.append({
            'src': relurljoin(CONFIG.urls.images, 'portfolio', 'commercial', 'laurenzo', filename),
            'preview': { 'src': relurljoin(CONFIG.urls.images, 'portfolio', 'commercial', 'laurenzo', 'preview', filename) }
        })

CONFIG.data.breadcrumbs.sculptures          = CONFIG.data.breadcrumbs.portfolio + [
    {
        'title': 'Sculptures',
          'url': relurljoin(CONFIG.baseurl, 'portfolio', 'sculptures')
    }
]

CONFIG.data.images.sculptures               = [ ]
basepath                                    = os.path.join(CONFIG.path.images, 'portfolio', 'sculptures')
for filename in os.listdir(basepath):
    path = os.path.join(basepath, filename)
    if not os.path.isdir(path):
        CONFIG.data.images.sculptures.append({
            'src': relurljoin(CONFIG.urls.images, 'portfolio', 'sculptures', filename),
            'preview': { 'src': relurljoin(CONFIG.urls.images, 'portfolio', 'sculptures', 'preview', filename) }
        })

CONFIG.data.products                        = [
    {
            'ID': unique_id(),
          'name': 'Fighter',
          'size': { 'width': 12, 'height': 48 },
        'medium': ['acrylic'],
          'type': 'canvas',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'Fighter') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 350 },
        'paypal': { 'ID': 'Q7UYVBHJLAYLS' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 65 },
           'paypal': { 'ID': 'DEMY23LSTSZJL' }
         }
    },
    {
            'ID': unique_id(),
          'name': 'Frida Kahlo 1',
          'size': { 'width': 32, 'height': 32 },
        'medium': ['acrylic', 'oil'],
          'type': 'canvas',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'FridaKahlo1') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 4500 },
        'paypal': { 'ID': 'UXSE3CK6KTV3J' }
    },
    {
            'ID': unique_id(),
          'name': 'Frida Kahlo 2',
          'size': { 'width': 22, 'height': 18 },
        'medium': ['acrylic'],
          'type': 'canvas',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'FridaKahlo2') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 700 },
        'paypal': { 'ID': 'NWUXUMVWL7KXJ' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 65 },
           'paypal': { 'ID': 'DEMY23LSTSZJL' }
         }
    },
    {
            'ID': unique_id(),
          'name': 'Frida Kahlo 3',
          'size': { 'width': 11, 'height': 14 },
        'medium': ['pencil'],
          'type': 'paper',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'FridaKahlo3') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 300 },
        'paypal': { 'ID': 'BZUXATNXQFYYL' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 35 },
           'paypal': { 'ID': 'UE8QQBUZ77KSJ' }
         }
    },
    {
            'ID': unique_id(),
          'name': 'Frida Kahlo 4',
          'size': { 'width': 11, 'height': 14 },
        'medium': ['china ink'],
          'type': 'NA',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'FridaKahlo4') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 350 },
        'paypal': { 'ID': 'UJBAKSB6P8P3N' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 35 },
           'paypal': { 'ID': 'UE8QQBUZ77KSJ' }
         }
    },
    {
            'ID': unique_id(),
          'name': 'Frida Kahlo 5',
          'size': { 'width': 30, 'height': 20 },
        'medium': ['acrylic'],
          'type': 'canvas',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'FridaKahlo5') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 300 },
        'paypal': { 'ID': 'ZJ3MKN9Z39RPA' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 65 },
           'paypal': { 'ID': 'DEMY23LSTSZJL' }
         }
    },
    {
            'ID': unique_id(),
          'name': 'Girl 1',
          'size': { 'width': 20, 'height': 20 },
        'medium': ['acrylic'],
          'type': 'canvas',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'Girl1') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 250 },
        'paypal': { 'ID': 'SFUN779KZZ3RW' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 35 },
           'paypal': { 'ID': 'UE8QQBUZ77KSJ' }
         }
    },
    {
            'ID': unique_id(),
          'name': 'Girl 2 Potrait',
          'size': { 'width': 24, 'height': 30 },
        'medium': ['acrylic'],
          'type': 'canvas',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'Girl2Potrait') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 250 },
        'paypal': { 'ID': 'HV2HT4RA7L4BJ' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 65 },
           'paypal': { 'ID': 'DEMY23LSTSZJL' }
         }
    },
    {
            'ID': unique_id(),
          'name': 'Girls Kissing',
          'size': { 'width': 20, 'height': 20 },
        'medium': ['acrylic'],
          'type': 'canvas',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'GirlsKissing') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 300 },
        'paypal': { 'ID': 'JTEZAEYGJXJV2' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 35 },
           'paypal': { 'ID': 'UE8QQBUZ77KSJ' }
         }
    },
    {
            'ID': unique_id(),
          'name': 'Gothic Woman',
          'size': { 'width': 24, 'height': 30 },
        'medium': ['acrylic'],
          'type': 'canvas',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'GothicWoman') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 450 },
        'paypal': { 'ID': 'Z62SXGBKBRA42' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 65 },
           'paypal': { 'ID': 'DEMY23LSTSZJL' }
         }
    },
    {
            'ID': unique_id(),
          'name': 'Johnny Cash',
          'size': { 'width': 24, 'height': 30 },
        'medium': ['acrylic'],
          'type': 'canvas',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'GuitarMan') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 400 },
        'paypal': { 'ID': 'GYBYCGNPT9REJ' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 65 },
           'paypal': { 'ID': 'DEMY23LSTSZJL' }
         }
    },
    {
            'ID': unique_id(),
          'name': 'Lajefa',
          'size': { 'width': 30, 'height': 20 },
        'medium': ['water color'],
          'type': 'NA',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'Lajefa') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 300 },
        'paypal': { 'ID': 'U344ZDRRGP2HY' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 65 },
           'paypal': { 'ID': 'DEMY23LSTSZJL' }
         }
    },
    {
            'ID': unique_id(),
          'name': 'Lindo Amaneser',
          'size': { 'width': 32, 'height': 55 },
        'medium': ['oil'],
          'type': 'canvas',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'LindoAmaneser') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 450 },
        'paypal': { 'ID': 'KNFTGHZK3S33W' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 65 },
           'paypal': { 'ID': 'DEMY23LSTSZJL' }
         }
    },
    {
            'ID': unique_id(),
          'name': 'Orgullo',
          'size': { 'width': 24, 'height': 30 },
        'medium': ['oil'],
          'type': 'canvas',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'Orgullo') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 250 },
        'paypal': { 'ID': 'UJQC3ZPYM3A5C' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 65 },
           'paypal': { 'ID': 'DEMY23LSTSZJL' }
         }
    },
    {
            'ID': unique_id(),
          'name': 'Oil Rig 1',
          'size': { 'width': 24, 'height': 48 },
        'medium': ['acrylic'],
          'type': 'canvas',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'OilRig1') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 450 },
        'paypal': { 'ID': 'MRTX75RVU8BA8' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 65 },
           'paypal': { 'ID': 'DEMY23LSTSZJL' }
         }
    },
    {
            'ID': unique_id(),
          'name': 'Oil Rig 2',
          'size': { 'width': 24, 'height': 48 },
        'medium': ['acrylic'],
          'type': 'canvas',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'OilRig2') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 450 },
        'paypal': { 'ID': 'FM9Q8YQPVTLTE' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 65 },
           'paypal': { 'ID': 'DEMY23LSTSZJL' }
         }
    },
    {
            'ID': unique_id(),
          'name': 'Red Lipstick',
          'size': { 'width': 20, 'height': 20 },
        'medium': ['acrylic'],
          'type': 'canvas',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'RedLipstick') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 250 },
        'paypal': { 'ID': 'RUK8YB6C4N3GJ' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 35 },
           'paypal': { 'ID': 'UE8QQBUZ77KSJ' }
         }
    },
    {
            'ID': unique_id(),
          'name': 'Reflejos',
          'size': { 'width': 20, 'height': 20 },
        'medium': ['acrylic, oil'],
          'type': 'canvas',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'Reflejos') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 250 },
        'paypal': { 'ID': 'BRBCYNRV54VPS' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 35 },
           'paypal': { 'ID': 'UE8QQBUZ77KSJ' }
         }
    },
    {
            'ID': unique_id(),
          'name': 'Shhh',
          'size': { 'width': 20, 'height': 20 },
        'medium': ['acrylic'],
          'type': 'canvas',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'Shhh') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 250 },
        'paypal': { 'ID': 'C4VJB8FZ6BF6Y' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 35 },
           'paypal': { 'ID': 'UE8QQBUZ77KSJ' }
         }
    },
    {
            'ID': unique_id(),
          'name': 'Virgin Mary',
          'size': { 'width': 30, 'height': 20 },
        'medium': ['acrylic'],
          'type': 'canvas',
         'image': { "src": relurljoin(CONFIG.urls.images, 'store', 'VirginMary') },
         'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 250 },
        'paypal': { 'ID': '4BHT6YBXQ2JPG' },
         'frame': {
            'price': { 'currency': { 'code': 'USD', 'symbol': '$' }, 'value': 65 },
           'paypal': { 'ID': 'DEMY23LSTSZJL' }
         }
    }
]

CONFIG.author.email                         = 'syiree.official@gmail.com'

# Jekyll SEO
CONFIG.description                          = CONFIG.brand.description
