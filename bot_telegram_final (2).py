import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import choice

import emoji

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

mofas  =  [
'''Ligar con la camarera

https://espectaculosluxury.com/producto/camareras-sexy/''', 

'''Atracar una comisaría

https://www.google.es/maps/place/Comisar%C3%ADa+de+Polic%C3%ADa+Nacional+distrito+Madrid-Centro/@40.4172267,-3.7112501,15z/data=!4m8!1m2!2m1!1scomisaria+sol+madrid!3m4!1s0xd42287b22043f2d:0x755a6eb4721241a1!8m2!3d40.4215847!4d-3.7101687''', 

'''Robar una bicicleta

https://as.com/deportes_accion/2020/10/07/mtb/1602080796_677686.html''', 


'''Invadir Polonia

https://es.wikipedia.org/wiki/Invasi%C3%B3n_alemana_de_Polonia_de_1939''',

'''Cantar en francés

https://www.youtube.com/watch?v=1MytlyMYwUE&ab_channel=Tino''',

'''Hacer autostop hasta Azerbaiyán:

https://www.google.com/maps/dir/Espa%C3%B1a/Bak%C3%BA,+Azerbaiy%C3%A1n/@40.27237,14.0759996,5z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0xc42e3783261bc8b:0xa6ec2c940768a3ec!2m2!1d-3.74922!2d40.463667!1m5!1m1!1s0x40307d6bd6211cf9:0x343f6b5e7ae56c6b!2m2!1d49.8670924!2d40.4092617!3e2''']

random  =  [
'''¡Haz un scaperoom con tus amigos!

https://www.google.es/maps/search/escape+room/@40.440694,-3.716103,12z/data=!4m2!2m1!6e1''',

'''Ir a tirar hachas 

https://el-hachazo.com/''',

'''Visitar la estación de metro fantasma: la antigua estación de Chamberí

http://www.madrid.org/cs/Satellite?c=CM_Actividades_FA&cid=1142678078071&pagename=ComunidadMadrid/Estructura''',

'''Safari Madrid 

https://www.safarimadrid.com/'''
            ]            

deporte  = [
'''Listado de rocódromos en Madrid:

https://www.google.es/maps/search/escalada/@40.4501,-3.7040867,12z''',

'''Ir a montar en tirolina a Cercedilla:

http://www.aventura-amazonia.com/parques-amazonia/cercedilla''',

'''Esquiar en Xanadu:

https://www.google.es/maps/place/intu+Xanad%C3%BA/@40.2996099,-3.9283459,17z/data=!3m1!4b1!4m5!3m4!1s0xd419241ef27ff49:0x7c2362934ba77b1a!8m2!3d40.2996058!4d-3.9261572''',

'''Ir de aventura en los arboles:

http://www.depinoapino.com/'''
]

entretenimiento  = [
'''¿Sabías que hay un montón de bares con juegos de mesa en Madrid? Te dejamos aquí algunos de ellos para que puedas elegir el que mejor te venga 

https://www.amigosmadrid.es/articulo/bares-con-juegos-de-mesa-en-madrid ''',

'''Una película con una experiencia más especial... ¿Qué te parece un autocine? Te dejamos la información aquí con sus horarios, precios, cartelera... 

https://autocinesmadrid.es/ ''',

'''Uno de los locales de ocio no convencional más famosos de Madrid, Sala Equis. Películas, encuentros culturales y mucho más. ¿Aún no la has visitado? Te dejamos toda la información aquí 

https://salaequis.es/ ''',

'''Una buena opción si te gusta el teatro y buscas un plan lleno de risas, puede ser asistir a un espectáculo de improvisación teatral. Algunas de las compañías más emblemáticas de la impro en Madrid son Jamming, Calambur, La escalera de Jacob... Podrás encontrar todas estas opciones y más en el siguiente enlace 

https://fortwo.es/magazine/donde-ver-improvisacion-teatral-madrid ''',

'''Una opción algo arriesgada es ir a un monólogo teatral. Es fácil encontrar uno que se adapte a ti, hay de distintos rangos de precio, temáticas... Te recomiendo que eches un vistazo a alguno lowcost de los que puedes encontrar aquí  

https://monologosenmadrid.es/ 

O alguno de mayor precio como alguno de estos  

https://www.monologosmadrid.net/ ''',

'''¿Alguna vez has soñado con ser el protagonista de un concurso de televisión? Pues en Loconcurso, esto es posible. Grupos de 6 personas se enfrentan en un divertido concurso en el que solo una persona podrá ser la ganadora. Para más información 

https://www.tofuro.com/concurso-loconcurso '''
                    
                    ]

naturaleza  =  [
'''¿Qué hay más relajante que un largo paseo por la sierra de Madrid charlando con amigos?

https://www.escapadarural.com/blog/los-mejores-rincones-de-la-sierra-de-madrid/''',

'''Ir a patinar, paseo, naturaleza, montar en barca... ¡El Retiro lo tiene todo sin salir de Madrid!

https://www.esmadrid.com/informacion-turistica/parque-del-retiro''',

'''El Parque del Oeste: un lugar bello para pasear y descansar: 

https://www.esmadrid.com/informacion-turistica/parque-del-oeste''',

'''Construido en el sigo XVIII por la duquesa de Osuna, el Parque del Capricho encierra belleza e historia que debería ser por todos conocida:

https://www.esmadrid.com/informacion-turistica/parque-del-capricho''',

'''¿Un plan céntrico y rodeado de naturaleza? Los Jardines de Sabatini son tu opción prefecta: 

https://www.esmadrid.com/informacion-turistica/jardines-de-sabatini''',

'''Un atardecer en el templo de Debod:

https://www.esmadrid.com/informacion-turistica/templo-de-debod'''
                                        ]

restauracion = [
'''Seguro que te va a encantar un buen desayuno o merienda en el Cereal Hunters, una cafetería dónde podrás probar esos cereales que salían en tus series favoritas, los cereales de tu infancia y hasta algunos cereales que ni te imaginas que existían. Tienes más información sobre los locales de estas cafeterías en el siguiente enlace 

https://www.cerealhunterscafe.com/   ''',

'''¿A que no sabías que el bar más antiguo del mundo se encuentra en Madrid? “Sobrino de Botín Horno de Asar”, especializado en cocina castellana y con una amplia representación de la repostería madrileña más tradicional. Lleva abierto desde 1725 y el dueño actual asegura que “el horno de leña no se ha apagado nunca en estos 294 años, ya que tiene que mantener el calor por la noche para asar por la mañana”. 

https://www.tripadvisor.es/Attraction_Review-g187514-d244300-Reviews-Sobrino_de_Botin-Madrid.html''',

'''Bocadillo de calamares en la Plaza del Sol, un clásico que nunca falla ''',

'''Prueba alguna de las mejores tortillas de la ciudad en el Pez tortilla 

https://peztortilla.com/''',

'''Resérvate el desayuno o la merienda para tomarte un mítico chocolate con churros en la famosa chocolatería de San Ginés. Abierta desde 1894, ¿y tú todavía no has ido? ''']

cultura  = ['Teatro',
            'Torneo de ajedrez ',
            'Exposición Paisajes de luz de Joanie Lemercier (Espacio Fundación Telefónica) ',
            'Exposición Arte y Ciencia del Siglo XXI (Museo de Ciencias Naturales) ',
            'Exposición de fotografía de Tomoko Yoneda (Fundación Mapfre) ',
            'Exposición Banksy (círculo de Bellas Artes) ']


def welcome(update, context):
    helpMessage =  """Lista de comandos posibles:
    - /newplan para planes de cualquier tipo
    - /newsport para planes deportivos
    - /newentreten para planes de entretenimiento
    - /newnaturaleza para planes en la naturaleza
    - /newrestauracion para elegir restaurante
    - /newcultura para planes culturales
    - /newrandom para planes sorprendentes
    - /newmofas para planes divertidos
                 
    made by Ravenclaw"""

    update.message.reply_text(helpMessage)

def newplan(update, context):

    message=choice(random + deporte + entretenimiento + naturaleza + restauracion + cultura)
    
    update.message.reply_text(message)

def newmofas(update, context):

    message=choice(mofas)
    
    update.message.reply_text(message)

def newrandom(update, context):

    message=choice(random)
    
    update.message.reply_text(message)

def newsport(update, context):

    message=choice(deporte)
    
    update.message.reply_text(message)

def newentreten(update, context):

    message=choice(entretenimiento)
    
    update.message.reply_text(message)

def newnaturaleza(update, context):

    message=choice(naturaleza)
    
    update.message.reply_text(message)

def newrestauracion(update, context):

    message=choice(restauracion)
    
    update.message.reply_text(message)

def newcultura(update, context):

    message=choice(cultura)
    
    update.message.reply_text(message)


def help(update, context):
    helpMessage= """Lista de comandos posibles:
    - /newplan para planes de cualquier tipo
    - /newsport para planes deportivos
    - /newentreten para planes de entretenimiento
    - /newnaturaleza para planes en la naturaleza
    - /newrestauracion para elegir restaurante
    - /newcultura para planes culturales
    - /newrandom para planes sorprendentes
    - /newmofas para planes divertidos
                 
    made by Ravenclaw"""
    update.message.reply_text(helpMessage)

# def new(update, context):
#     newMessage= 'Escribe el comando /new para empezar a divertirte'
#     update.message.reply_text(newMessage)


def echo(update, context):
    update.message.reply_text(update.message.text)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    updater = Updater("1635642412:AAFVv4JtXDMEwevRPbx76g_QlPfvDqM0ags", use_context=True)

    dp = updater.dispatcher


    dp.add_handler(CommandHandler("newplan", newplan))
    dp.add_handler(CommandHandler("welcome", welcome))
    dp.add_handler(CommandHandler("newsport", newsport))
    dp.add_handler(CommandHandler("newmofas", newmofas))
    dp.add_handler(CommandHandler("newentreten", newentreten))
    dp.add_handler(CommandHandler("newnaturaleza", newnaturaleza))
    dp.add_handler(CommandHandler("newrestauracion", newrestauracion))
    dp.add_handler(CommandHandler("newcultura", newcultura))
    dp.add_handler(CommandHandler("newrandom", newrandom))
    dp.add_handler(CommandHandler("help", help))
   

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()