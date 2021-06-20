from waitress import serve
import logging
import app
logging.basicConfig(level = logging.INFO, filename = 'songohan.log')
from paste.translogger import TransLogger
handler=TransLogger(app.app, setup_console_handler=False)
serve(handler,host='0.0.0.0',port=5000)
