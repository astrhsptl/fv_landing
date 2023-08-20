class About:
    def __init__(self, data, **kwargs) -> None:
        self.title = data['title']
        self.description =  data['description']
        try:
            self.svg = data['svg']
        except:
            self.svg = None


cases = [
            About({
                'title': 'kibtop.ru',
                'description': 'Сайт интернет-магазина, ориентированный на русскоговорящую, англоговорящую и турецкую аудиторию',
            }),
            About({
                'title': 'Ваш Грузовой',
                'description': 'Лендинг компании “Ваш Грузовой”, занимающейся грузоперевозками',
            }),
            About({
                'title': 'ВВБ',
                'description': 'Сервис подписания криптографическим шифром',
            })
        ]

about_us = [
            About({
                'title': 'Надежность',
                'description': 'Мы готовы быть вашим надежным партнером в сфере информационных технологий и обеспечить ваше будущее в надежных руках',
                'svg': 'images/svg/reliability.svg',
            }),
            About({
                'title': 'Скорость',
                'description': 'Мы выполняем все заказы в оптимальные сроки, не перенося дедлайны ',
                'svg': 'images/svg/speed.svg',
            }),
            About({
                'title': 'Гибкий подход',
                'description': 'Мы готовы предоставить индивидуальный подход к каждому проекту и решению задач нашего клиента',
                'svg': 'images/svg/contact.svg',
            }),
            About({
                'title': 'Безопасность',
                'description': 'Мы заботимся о безопасности данных наших клиентов, не допуская утечки информации о ваших проектах',
                'svg': 'images/svg/security.svg',
            }),
            About({
                'title': 'Вклад в будущее',
                'description': 'Сотрудничая с нами, вы получаете долговременную поддержку продукта и возможность постоянного сотрудничества с надёжным партнёром',
                'svg': 'images/svg/fv.svg',
            }),
            About({
                'title': 'Команда мечты',
                'description': 'Сотрудничая с нами, вы полагаетесь на команду специалистов, с каждым днём всё больше развивающихся в IT сфере',
                'svg': 'images/svg/team.svg',
            }),
        ]

services = ['Frontend', 'Backend', 'Data analysis', 'Dev Ops', 'Mobile development']