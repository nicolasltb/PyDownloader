#Autor: Nicolas Lopes

import pytube

print('\n\nBem vindo ao PyDownloader!')

print('Insira a URL do video que deseja baixar:')
url = input("URL: ")

try:
    video = pytube.YouTube(url)
except:
    print("URL Invalida. Saindo...")
    exit()

#print(video.streams.filter(progressive=True, file_extension='mp4').all())

resolution_list = ['18', '20', '22']
qualidade = "Escolha a qualidade em que voce deseja baixar o video:\n" 

for resolution in resolution_list:
    if(video.streams.get_by_itag(resolution) and resolution == '18'):
        qualidade += "360p\n"
    if(video.streams.get_by_itag(resolution) and resolution == '20'):
        qualidade += "480p\n"
    if(video.streams.get_by_itag(resolution) and resolution == '22'):
        qualidade += "720p\n"
    
print(qualidade)
resolucao = input("Resolução: ")

if(resolucao == '360p'):
    stream = video.streams.get_by_itag(18)
    print('Downloading...')
    stream.download()
    print('Done')
if(resolucao == '480p'):
    stream = video.streams.get_by_itag(20)
    print('Downloading...')
    stream.download()
    print('Done')
if(resolucao == '720p'):
    stream = video.streams.get_by_itag(22)
    print('Downloading...')
    stream.download()
    print('Done')
if(resolucao == '' or resolucao != '360p' and resolucao != '480p' and resolucao != '720p'):
    print('Opção Invalida. Saindo...')
