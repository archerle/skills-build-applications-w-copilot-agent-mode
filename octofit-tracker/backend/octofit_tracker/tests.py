from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team_id=str(team.id))
        self.assertEqual(str(user), 'Test User')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team_id=str(team.id))
        activity = Activity.objects.create(user_id=str(user.id), type='Run', duration=30, date='2025-12-17')
        self.assertEqual(activity.type, 'Run')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='Desc', difficulty='Easy')
        self.assertEqual(workout.name, 'Test Workout')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team_id=str(team.id))
        leaderboard = Leaderboard.objects.create(user_id=str(user.id), score=100)
        self.assertEqual(leaderboard.score, 100)
