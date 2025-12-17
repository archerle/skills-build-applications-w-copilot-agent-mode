from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Eliminando datos existentes...')
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Creando equipos...')

        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        self.stdout.write('Creando usuarios...')
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team_id=str(marvel.id)),
            User.objects.create(name='Captain America', email='cap@marvel.com', team_id=str(marvel.id)),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team_id=str(marvel.id)),
            User.objects.create(name='Batman', email='batman@dc.com', team_id=str(dc.id)),
            User.objects.create(name='Superman', email='superman@dc.com', team_id=str(dc.id)),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team_id=str(dc.id)),
        ]

        self.stdout.write('Creando actividades...')
        Activity.objects.create(user_id=str(users[0].id), type='Correr', duration=30, date=timezone.now())
        Activity.objects.create(user_id=str(users[1].id), type='Nadar', duration=45, date=timezone.now())
        Activity.objects.create(user_id=str(users[3].id), type='Bicicleta', duration=60, date=timezone.now())

        self.stdout.write('Creando workouts...')
        Workout.objects.create(name='Entrenamiento Marvel', description='Rutina intensa de superhéroes', difficulty='Alta')
        Workout.objects.create(name='Entrenamiento DC', description='Rutina de fuerza y resistencia', difficulty='Media')

        self.stdout.write('Creando leaderboard...')
        Leaderboard.objects.create(user_id=str(users[0].id), score=100)
        Leaderboard.objects.create(user_id=str(users[3].id), score=90)
        Leaderboard.objects.create(user_id=str(users[1].id), score=80)

        self.stdout.write(self.style.SUCCESS('¡Base de datos poblada con datos de prueba!'))
