import tweepy, os
import function
import time
#Twitter Acess
#Read tweepy Tutorial
consumer_key = '###'
consumer_secret = '###'
acess_token = '###'
acess_token_secret = '###'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acess_token, acess_token_secret)
api = tweepy.API(auth)

print 'UFRJ\nComp-1\nProfessor: Sapienza\nTurma: EE2\nAlunos: Atila Rangel, Natalia Godinho, Rafael Vazquez, Rodrigo Winks\n'

#User questions and conditions
loop = True
while loop:
    user = raw_input('Escreva o nome de usuario do twitter na qual deseja pesquisar: ')
    stop_w = raw_input('Deseja remover as Stop Words, sim ou nao? ')
    while stop_w != 'sim' and stop_w != 'nao':
        stop_w = raw_input('Comando invalido. Deseja remover as Stop Words, sim ou nao? ')
    stop_w_list = open('stopwords_portugues.txt', 'r')
    followings = raw_input('Deseja analisar os followings, sim ou nao? ')
    while followings != 'sim' and followings != 'nao':
        followings = raw_input('Comando invalido. Deseja analisar os followings, sim ou nao? ')


    public_tweets = api.user_timeline(id = user,count = 200)
    user_followings_list = api.friends_ids(id = user, count = 10)
    function.anal_tweets(api, user, stop_w, followings, public_tweets, user_followings_list)
    #Show user tweets
    print'\nTop 10\n'
    function.frequency(user)
    print'\n'
    continu = (raw_input('Deseja pesquisar mais algum outro usuario? (Se nao, digite fim) ')).lower()
    if continu == 'sim':
        loop = True
    elif continu == 'Fim' or continu == 'end' or continu == 'fim':
        print 'Fim'
        loop = False
