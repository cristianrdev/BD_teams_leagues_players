from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	if request.method == 'GET':
		print('------------es un GET-----------------')
		context = {
			"leagues": League.objects.all(),
			"teams": Team.objects.all(),
			"players": Player.objects.all(),
			"title_leagues": '',
			"title_teams": '',
			"title_players": '',
		}
		return render(request, "leagues/index.html", context)
	
	else:
		print('------------es un POST-----------------')
		# if request.POST['filtro'] == '0' :
		# 	print('Volver a el index***********')
		# 	return redirect("/")



		if int(request.POST['filtro']) == 1 :
			print('es el filtro 1***********')
			context = {
			"leagues": League.objects.filter(sport='Baseball'),
			"title_teams": 'hidden',
			"title_players": 'hidden',

			}

		if int(request.POST['filtro']) == 2 :
			print('es el filtro 2***********')
			context = {
				"leagues": League.objects.filter(name__contains='Women'),
				"title_teams": 'hidden',
				"title_players": 'hidden',
			}
			

		if int(request.POST['filtro']) == 3 :
			print('es el filtro 3***********')
			context = {
			"leagues": League.objects.filter(sport__contains='Hockey'),
			"title_teams": 'hidden',
			"title_players": 'hidden',
			}

		if int(request.POST['filtro']) == 4 :
			print('es el filtro 4***********')
			context = {
			"leagues": League.objects.exclude(sport='Football'),
			"title_teams": 'hidden',
			"title_players": 'hidden',
			}

		if int(request.POST['filtro']) == 5 :
			print('es el filtro 5***********')
			context = {
			"leagues": League.objects.filter(name__contains='Conference'),
			"title_teams": 'hidden',
			"title_players": 'hidden',
			}

		if int(request.POST['filtro']) == 6 :
			print('es el filtro 6***********')
			context = {
			"leagues": League.objects.filter(name__contains='Atlantic'),
			"title_teams": 'hidden',
			"title_players": 'hidden',
			}

		if int(request.POST['filtro']) == 7 :
			print('es el filtro 7***********')
			context = {
			"title_leagues": 'hidden',
			"teams": Team.objects.filter(location='Dallas'),
			"title_players": 'hidden',
			
			}

		if int(request.POST['filtro']) == 8 :
			print('es el filtro 8***********')
			context = {
			"title_leagues": 'hidden',
			"teams": Team.objects.filter(team_name='Raptors'),
			"title_players": 'hidden',
			}

		if int(request.POST['filtro']) == 9 :
			print('es el filtro 9***********')
			context = {
			"title_leagues": 'hidden',
			"teams": Team.objects.filter(location__contains='City'),
			"title_players": 'hidden',
			}

		if int(request.POST['filtro']) == 10 :
			print('es el filtro 10***********')
			context = {
			"title_leagues": 'hidden',
			"teams": Team.objects.filter(team_name__startswith='T'),
			"title_players": 'hidden',
			}

		if int(request.POST['filtro']) == 11 :
			print('es el filtro 11***********')
			context = {
			"title_leagues": 'hidden',
			"teams": Team.objects.all().order_by('location'),
			"title_players": 'hidden',
			}

		if int(request.POST['filtro']) == 12 :
			print('es el filtro 12***********')
			context = {
			"title_leagues": 'hidden',
			"teams": Team.objects.all().order_by('-team_name'),
			"title_players": 'hidden',
			}

		if int(request.POST['filtro']) == 13 :
			print('es el filtro 13***********')
			context = {
			"title_leagues": 'hidden',
			"title_teams": 'hidden',
			"players": Player.objects.filter(last_name = 'Cooper'),
			}

		if int(request.POST['filtro']) == 14 :
			print('es el filtro 14***********')
			context = {
			"title_leagues": 'hidden',
			"title_teams": 'hidden',
			"players": Player.objects.filter(first_name = 'Joshua'),
			}

		if int(request.POST['filtro']) == 15 :
			print('es el filtro 15***********')
			# jugadores_cooper = Player.objects.
			context = {
			"title_leagues": 'hidden',
			"title_teams": 'hidden',
			"players": Player.objects.filter(last_name = 'Cooper').exclude(first_name = 'Joshua'),
			}

		if int(request.POST['filtro']) == 16 :
			print('es el filtro 16***********')
			context = {
			"title_leagues": 'hidden',
			"title_teams": 'hidden',
			"players": Player.objects.filter(first_name__in = ['Alexander' , 'Wyatt']),
			
			}


		return render(request, "leagues/index.html", context)


def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")