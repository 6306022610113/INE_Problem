import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

color_map = []
#South
G.add_edge('prachuap khiri khan','chumphon',weight=189)
G.add_edge('chumphon','ranong',weight=126)
G.add_edge('ranong','pangnga',weight=231)
G.add_edge('chumphon','surachthani',weight=184)
G.add_edge('pangnga','phuket',weight=87)
G.add_edge('ranong','surachthani',weight=218)
G.add_edge('pangnga','surachthani',weight=159)
G.add_edge('surachthani','krabi',weight=156)
G.add_edge('pangnga','krabi',weight=74)
G.add_edge('surachthani','pattalung',weight=224)
G.add_edge('surachthani','nakorn sritammarach',weight=140)
G.add_edge('krabi','trang',weight=126)
G.add_edge('krabi','nakorn sritammarach',weight=172)
G.add_edge('trang','nakorn sritammarach',weight=131)
G.add_edge('nakorn sritammarach','pattalung',weight=109)
G.add_edge('trang','pattalung',weight=58)
G.add_edge('trang','stoon',weight=144)
G.add_edge('stoon','songkra',weight=125)
G.add_edge('pattalung','songkra',weight=122)
G.add_edge('nakorn sritammarach','songkra',weight=182)
G.add_edge('songkra','yala',weight=131)
G.add_edge('songkra','pattani',weight=105)
G.add_edge('yala','pattani',weight=41)
G.add_edge('yala','narathiwad',weight=89)
G.add_edge('pattani','narathiwad',weight=96)

#Eastern
G.add_edge('ley','nongkai',weight=234)
G.add_edge('ley','nongbualampoo',weight=99)
G.add_edge('ley','chaiyapoom',weight=227)
G.add_edge('chaiyapoom','nakorn ratchasima',weight=121)
G.add_edge('nakorn ratchasima','buriram',weight=127)
G.add_edge('buriram','surin',weight=55)
G.add_edge('surin','srisakate',weight=105)
G.add_edge('srisakate','ubon ratchathani',weight=65)
G.add_edge('ubon ratchathani','amnajjarern',weight=77)
G.add_edge('amnajjarern','mukdaharn',weight=99)
G.add_edge('mukdaharn','nakorn panom',weight=110)
G.add_edge('nakorn panom','bungkarn',weight=181)
G.add_edge('bungkarn','nongkai',weight=135)
G.add_edge('nongkai','uttaradit',weight=52)
G.add_edge('nongbualampoo','uttaradit',weight=51)
G.add_edge('uttaradit','bungkarn',weight=207)
G.add_edge('uttaradit','sakonnakorn',weight=166)
G.add_edge('bungkarn','sakonnakorn',weight=195)
G.add_edge('sakonnakorn','nakorn panom',weight=94)
G.add_edge('sakonnakorn','mukdaharn',weight=114)
G.add_edge('sakonnakorn','karasin',weight=129)
G.add_edge('uttaradit','karasin',weight=147)
G.add_edge('khonkaen','uttaradit',weight=121) 
G.add_edge('nongbualampoo','khonkaen',weight=118)
G.add_edge('ley','khonkaen',weight=207)
G.add_edge('nongbualampoo','chaiyapoom',weight=194)
G.add_edge('chaiyapoom','khonkaen',weight=140)
G.add_edge('khonkaen','nakorn sawan',weight=192)
G.add_edge('nakorn sawan','mahasarakam',weight=214)
G.add_edge('mahasarakam','buriram',weight=149)
G.add_edge('buriram','roied',weight=149)
G.add_edge('roied','surin',weight=145)
G.add_edge('roied','srisakate',weight=146)
G.add_edge('yasothorn','srisakate',weight=103)
G.add_edge('yasothorn','ubonratchathani',weight=103)
G.add_edge('amnajjarern','yasothorn',weight=57)
G.add_edge('mukdaharn','yasothorn',weight=115)
G.add_edge('yasothorn','roied',weight=68)
G.add_edge('mukdaharn','roied',weight=149)
G.add_edge('roied','karasin',weight=49)
G.add_edge('mahasarakam','roied',weight=44)
G.add_edge('mahasarakam','karasin',weight=48)
G.add_edge('karasin','khonkaen',weight=77)
G.add_edge('khonkaen','mahasarakam',weight=72)
G.add_edge('mukdaharn','karasin',weight=164)

#North
G.add_edge('maehongsorn','chiangmai',weight=237)
G.add_edge('maehongsorn','tak',weight=452)
G.add_edge('tak','lampoon',weight=241)
G.add_edge('chiangmai','lampoon',weight=35)
G.add_edge('lampang','lampoon',weight=80)
G.add_edge('lampang','chiangmai',weight=112)
G.add_edge('chiangmai','payao',weight=160)
G.add_edge('chiangmai','chiangrai',weight=190)
G.add_edge('lampang','chiangrai',weight=229)
G.add_edge('payao','lampang',weight=142)
G.add_edge('pare','chiangrai',weight=243)
G.add_edge('chiangrai','payao',weight=92)
G.add_edge('chiangrai','nan',weight=218)
G.add_edge('payao','nan',weight=148)
G.add_edge('pare','payao',weight=143)
G.add_edge('pare','nan',weight=119)
G.add_edge('lampang','pare',weight=96)
G.add_edge('lampang','sukothai',weight=195)
G.add_edge('pare','sukothai',weight=163)
G.add_edge('lampang','tak',weight=188)
G.add_edge('pare','uttaradit',weight=72)
G.add_edge('uttaradit','sukothai',weight=91)
G.add_edge('pitsanulok','uttaradit',weight=108)
G.add_edge('sukothai','pisanulok',weight=58)
G.add_edge('sukothai','tak',weight=85)
G.add_edge('pitsanulok','petchchaboon',weight=177)
G.add_edge('pijit','pitsanulok',weight=57)
G.add_edge('pitsanulok','kampangpetch',weight=110)
G.add_edge('kampangpetch','sukothai',weight=71)
G.add_edge('tak','kampangpetch',weight=62)
G.add_edge('pijit','kampangpetch',weight=100)
G.add_edge('nakorn sawan','kampangpetch',weight=132)
G.add_edge('nakorn sawan','uthaithani',weight=43)
G.add_edge('nakorn sawan','pijit',weight=104)
G.add_edge('nakorn sawan','pitsanulok',weight=133)
G.add_edge('pijit','petchchaboon',weight=133)
G.add_edge('petchchaboon','nakorn sawan',weight=202)

#Central
G.add_edge('nakorn sawan','uthaithani',weight=43)
G.add_edge('uthaithani','chainat',weight=26)
G.add_edge('nakorn sawan','chainat',weight=62)
G.add_edge('chainat','singburi',weight=57)
G.add_edge('singburi','nakorn sawan',weight=100)
G.add_edge('lopburi','nakorn sawan',weight=151)
G.add_edge('lopburi','singburi',weight=32)
G.add_edge('angthong','singburi',weight=40)
G.add_edge('lopburi','angthong',weight=42)
G.add_edge('lopburi','ayutthaya',weight=73)
G.add_edge('suparnburi','angthong',weight=44)
G.add_edge('uthaithani','suparnburi',weight=101)
G.add_edge('angthong','ayutthaya',weight=39)
G.add_edge('ayutthaya','suparnburi',weight=64)
G.add_edge('karnjanaburi','suparnburi',weight=98)
G.add_edge('suparnburi','nakorn pathom',weight=97)
G.add_edge('karnjanaburi','nakorn pathom',weight=67)
G.add_edge('karnjanaburi','rachburi',weight=81)
G.add_edge('nakorn pathom','rachburi',weight=48)
G.add_edge('samutsakorn','rachburi',weight=67)
G.add_edge('nakorn pathom','samutsakorn',weight=67)
G.add_edge('rachburi','samutsongkram',weight=35)
G.add_edge('samutsakorn','samutsongkram',weight=38)
G.add_edge('petchburi','rachburi',weight=58)
G.add_edge('samutsongkram','petchburi',weight=57)
G.add_edge('bangkok','nakorn pathom',weight=57)
G.add_edge('bangkok','samutsongkram',weight=37)
G.add_edge('nonthaburi','nakorn pathom',weight=64)
G.add_edge('ayutthaya','nakorn pathom',weight=107)
G.add_edge('nonthaburi','suparnburi',weight=95)
G.add_edge('nonthaburi','ayutthaya',weight=75)
G.add_edge('nonthaburi','bangkok',weight=22)
G.add_edge('pathumthani','bangkok',weight=42)
G.add_edge('ayutthaya','pathumthani',weight=50)
G.add_edge('pathumthani','nonthaburi',weight=27)
G.add_edge('pathumthani','nakorn nayok',weight=117)
G.add_edge('saraburi','pathumthani',weight=85)
G.add_edge('saraburi','ayutthaya',weight=69)
G.add_edge('saraburi','lopburi',weight=47)
G.add_edge('nakorn nayok','saraburi',weight=58)
G.add_edge('prachinburi','nakorn nayok',weight=20)
G.add_edge('prachinburi','bangkok',weight=145)
G.add_edge('chachiengsao','nakorn nayok',weight=75)
G.add_edge('chachiengsao','bangkok',weight=85)
G.add_edge('chachiengsao','prachinburi',weight=74)
G.add_edge('samutprakarn','bangkok',weight=26)
G.add_edge('samutprakarn','chonburi',weight=70)
G.add_edge('chachiengsao','chonburi',weight=50)
G.add_edge('prachinburi','srakaew',weight=104)
G.add_edge('srakaew','chachiengsao',weight=130)
G.add_edge('chantaburi','chachiengsao',weight=206)
G.add_edge('srakaew','chantaburi',weight=161)
G.add_edge('chachiengsao','trad',weight=69)
G.add_edge('chantaburi','rayong',weight=111)
G.add_edge('chachiengsao','rayong',weight=135)

#link Central and South
G.add_edge('prachuap khiri khan','petchburi',weight=159)

#link Central and Eastern
G.add_edge('nakorn ratchasima','saraburi',weight=148)
G.add_edge('buriram','saraburi',weight=282)
print(G)
for k,m in enumerate(G):
    if (k >=0 and k <= 14):
        color_map.append('pink') #South color
    if (k >=15 and k <= 36):
        color_map.append('orange') #Eastern color
    if (k >=37 and k <= 51):
        color_map.append('blue') #North color
    if (k >=52 and k <= 77):
        color_map.append('green') #Central color
    

try:
    again = 'y'
    while again.lower() == 'y': 
        print('1.No visit')
        print('2. 1 visit')
        print('3. 2 visit')
        print('4.Exit')
        key = int(input("Enter the Number:"))
        if key == 1:
            Province_start = input('Province Start: ')
            Province_end = input('Province End: ')
            all_paths = list(nx.all_shortest_paths(G,source=Province_start,target=Province_end,weight=None))
            o = []
            p = []
            m = 0
            three_shortest_path = []
            for x,i in enumerate(all_paths):
                    
                for k in range(len(i)):
                    if k != len(i)-1:
                        o.append(nx.shortest_path_length(G,source=i[k],target=i[k+1],weight='weight'))
                all_paths[x].append(sum(o))
                o = []
            for y in all_paths:
                for t in y:
                    if type(t) == int:
                        p.append(t)
            while m != 3:
                three_shortest_path.append(all_paths[p.index(min(p))])
                k = p.index(min(p))
                p.pop(k)
                all_paths.pop(k)
                m +=1
            print('Province to pass through shortest path First is :',three_shortest_path[0][:-1] )
            print('Distance shortest path First from',Province_start,'to',Province_end,'is:' , three_shortest_path[0][-1],'Km')

            print('Province to pass through shortest path Second is :',three_shortest_path[1][:-1] )
            print('Distance shortest path Second from',Province_start,'to',Province_end,'is:' , three_shortest_path[1][-1],'Km')

            print('Province to pass through shortest path Third is :',three_shortest_path[2][:-1] )
            print('Distance shortest path Third from',Province_start,'to',Province_end,'is:' , three_shortest_path[2][-1],'Km')
        if key == 2:
            Province_start = input('Province Start: ')
            Province_stay_1 = input('Province stay: ')
            Province_end = input('Province End: ')
            path_length = nx.shortest_path_length(G,source=Province_start,target=Province_stay_1,weight='weight')
            shortest_path = list(nx.shortest_path(G,source=Province_start,target=Province_stay_1,weight='weight'))
            
            all_paths = list(nx.all_shortest_paths(G,source=Province_stay_1,target=Province_end,weight=None))
            o = []
            p = []
            m = 0
            three_shortest_path = []
            for x,i in enumerate(all_paths):
                    
                for k in range(len(i)):
                    if k != len(i)-1:
                        o.append(nx.shortest_path_length(G,source=i[k],target=i[k+1],weight='weight'))
                all_paths[x].append(sum(o))
                o = []
            for y in all_paths:
                for t in y:
                    if type(t) == int:
                        p.append(t)
            while m != 3:
                three_shortest_path.append(all_paths[p.index(min(p))])
                k = p.index(min(p))
                p.pop(k)
                all_paths.pop(k)
                m +=1
            print('Province to pass through shortest path First is :',shortest_path[:-1]+three_shortest_path[0][:-1] )
            print('Distance shortest path First from',Province_start,'to',Province_end,'is:' , three_shortest_path[0][-1]+path_length,'Km')

            print('Province to pass through shortest path Second is :',shortest_path[:-1]+three_shortest_path[1][:-1] )
            print('Distance shortest path Second from',Province_start,'to',Province_end,'is:' , three_shortest_path[1][-1]+path_length,'Km')

            print('Province to pass through shortest path Third is :',shortest_path[:-1]+three_shortest_path[2][:-1] )
            print('Distance shortest path Third from',Province_start,'to',Province_end,'is:' , three_shortest_path[2][-1]+path_length,'Km')
        if key == 3:
            Province_start = input('Province Start: ')
            Province_stay_1 = input('Province stay 1: ')
            Province_stay_2 = input('Province stay 2: ')
            Province_end = input('Province End: ')
            path_length1 = nx.shortest_path_length(G,source=Province_start,target=Province_stay_1,weight='weight')
            shortest_path1 = list(nx.shortest_path(G,source=Province_start,target=Province_stay_1,weight='weight'))

            path_length2 = nx.shortest_path_length(G,source=Province_stay_1,target=Province_stay_2,weight='weight')
            shortest_path2 = list(nx.shortest_path(G,source=Province_stay_1,target=Province_stay_2,weight='weight'))
            
            all_paths = list(nx.all_shortest_paths(G,source=Province_stay_2,target=Province_end,weight=None))
            o = []
            p = []
            m = 0
            three_shortest_path = []
            for x,i in enumerate(all_paths):
                    
                for k in range(len(i)):
                    if k != len(i)-1:
                        o.append(nx.shortest_path_length(G,source=i[k],target=i[k+1],weight='weight'))
                all_paths[x].append(sum(o))
                o = []
            for y in all_paths:
                for t in y:
                    if type(t) == int:
                        p.append(t)
            while m != 3:
                three_shortest_path.append(all_paths[p.index(min(p))])
                k = p.index(min(p))
                p.pop(k)
                all_paths.pop(k)
                m +=1
            print('Province to pass through shortest path First is :',shortest_path1[:-1]+shortest_path2[:-1]+three_shortest_path[0][:-1] )
            print('Distance shortest path First from',Province_start,'to',Province_end,'is:' , three_shortest_path[0][-1]+path_length1+path_length2,'Km')

            print('Province to pass through shortest path Second is :',shortest_path1[:-1]+shortest_path2[:-1]+three_shortest_path[1][:-1] )
            print('Distance shortest path Second from',Province_start,'to',Province_end,'is:' , three_shortest_path[1][-1]+path_length1+path_length2,'Km')

            print('Province to pass through shortest path Third is :',shortest_path1[:-1]+shortest_path2[:-1]+three_shortest_path[2][:-1] )
            print('Distance shortest path Third from',Province_start,'to',Province_end,'is:' , three_shortest_path[2][-1]+path_length1+path_length2,'Km')
        if key == 4:
            break
        else:
            again = 'y'
        edge_labels = nx.get_edge_attributes(G,'weight')
        pos = nx.spring_layout(G)
        nx.draw(G,pos ,with_labels=True,font_color="black",font_size="5",node_size= 2000,node_color=color_map)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
        plt.show()
        again = input('Enter y to do again or n it exit: ')
except:
    print('End')








