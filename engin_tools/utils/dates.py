from datetime import datetime

RU_MONTH = {
    'января': '01',
    'февраля': '02',
    'марта': '03',
    'апреля': '04',
    'мая': '05',
    'июня': '06',
    'июля': '07',
    'августа': '08',
    'сентября': '09',
    'октября': '10',
    'ноября': '11',
    'декабря': '12',
}


def get_current_year():
    return getattr(get_current_year, 'current_year')


setattr(get_current_year, 'current_year', datetime.now().year)
