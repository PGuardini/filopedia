# como o server django estará rodando na raiz do projeto,
# não cabe voltar uma pasta para chegar em data
#DATA_PATH = "data/"
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent # Sobe até a raiz
DATA_PATH = os.path.join(BASE_DIR, 'data/')