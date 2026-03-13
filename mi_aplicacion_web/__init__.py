from .login import login
from .pag_inicio import inicio
from .pag_administracion import administracion
from .pag_personal import personal
from .pag_formulario import formularios
from .pag_documento import documentos
from .pag_reporte import reportes

# importamos modelos
from .modelos.personal_model import PERSONAL_TBL
from .repositorios.personal_repositorio import seleccionar_todos
from .estilos.estilo_tabla import *


