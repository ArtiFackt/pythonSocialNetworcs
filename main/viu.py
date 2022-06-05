# Сперва импорттируем класс блюпринта
from flask import Blueprint, render_template

# Затем создаем новый блюпринт, выбираем для него имя
main_blueprint: Blueprint = Blueprint('catalog_blueprint', __name__, template_folder='templates')


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@main_blueprint.route('/')
def main_page():
    return render_template('index.html')
