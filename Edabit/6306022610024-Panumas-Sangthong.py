import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_edge('Chiang Rai',"Phayao",weight=92)
G.add_edge("Chiang Rai",'Lampang',weight=229)
G.add_edge('Chiang Rai',"Chiang Mai",weight=190)
G.add_edge('Phayao',"Nan",weight=148)
G.add_edge('Phayao',"Phrae",weight=143)
G.add_edge('Phayao',"Lampang",weight=142)
G.add_edge("Chiang Mai",'Mae Hong Son',weight=237)
G.add_edge('Chiang Mai',"Lampang",weight=114)
G.add_edge('Chiang Mai',"Lamphun",weight=39)
G.add_edge('Lampang',"Lamphun",weight=82)
G.add_edge('Lampang',"Tak",weight=188)
G.add_edge('Lampang',"Sukhothai",weight=195)
G.add_edge('Lampang',"Phrae",weight=96)
G.add_edge('Tak',"Mae Hong Son",weight=508)
G.add_edge('Tak',"Lamphun",weight=241)
G.add_edge('Tak',"Sukhothai",weight=85)
G.add_edge('Tak',"Kamphaeng Phe",weight=62)
G.add_edge('Phrae',"Nan",weight=119)
G.add_edge('Phrae',"Uttaradit",weight=72)
G.add_edge('Phrae',"Sukhothai",weight=163)
G.add_edge('Sukhothai',"Uttaradit",weight=91)
G.add_edge('Sukhothai',"Kamphaeng Phe",weight=71)
G.add_edge('Sukhothai',"Phitsanulok",weight=58)
G.add_edge('Phitsanulok',"Uttaradit",weight=108)
G.add_edge('Phitsanulok',"Kamphaeng Phe",weight=110)
G.add_edge('Phitsanulok',"Phichit",weight=57)
G.add_edge('Phitsanulok',"Phetchabun",weight=177)
G.add_edge('Nakhon Sawan',"Uthai Thani",weight=43)
G.add_edge('Nakhon Sawan',"Kamphaeng Phe",weight=132)
G.add_edge('Nakhon Sawan',"Phichit",weight=104)
G.add_edge('Nakhon Sawan',"Phetchabun",weight=174)
G.add_edge('Phichit',"Phetchabun",weight=133)
G.add_edge('Phichit',"Kamphaeng Phe",weight=100)





"""
    again = 'y'
    while again.lower() == 'y': 
        print('1.No visit')
        print('2. 1 visit')
        print('3. 2 visit')
        print('4.Exit')
        key = int(input("Enter the Number:"))
        if key == 1:
"""
Province_start ='Chiang Rai' #input('Province Start: ')
Province_end ="Uthai Thani" #input('Province End: ')
all_paths = list(nx.shortest_simple_paths(G,source=Province_start,target=Province_end,weight=None))

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

def mains(text):
    myfile = open('friends.txt','w')
    for i in text:
        myfile.write(str(i) + '\n')

    myfile.close()
    print('The name were written to friends.txt')
mains(all_paths)
"""
print('Province to pass through shortest path First is :',three_shortest_path[0][:-1] )
print('Distance shortest path First from',Province_start,'to',Province_end,'is:' , three_shortest_path[0][-1],'Km')

print('Province to pass through shortest path Second is :',three_shortest_path[1][:-1] )
print('Distance shortest path Second from',Province_start,'to',Province_end,'is:' , three_shortest_path[1][-1],'Km')

print('Province to pass through shortest path Third is :',three_shortest_path[2][:-1] )
print('Distance shortest path Third from',Province_start,'to',Province_end,'is:' , three_shortest_path[2][-1],'Km')
"""
"""
        if key == 2:
            Province_start = input('Province Start: ')
            Province_stay_1 = input('Province stay: ')
            Province_end = input('Province End: ')
            path_length = nx.shortest_path_length(G,source=Province_start,target=Province_stay_1,weight='weight')
            shortest_path = list(nx.shortest_path(G,source=Province_start,target=Province_stay_1,weight='weight'))
            
            all_paths = list(nx.shortest_simple_paths(G,source=Province_stay_1,target=Province_end,weight=None))
            
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
            
            all_paths = list(nx.shortest_simple_paths(G,source=Province_stay_2,target=Province_end,weight=None))
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
        =    print('Distance shortest path First from',Province_start,'to',Province_end,'is:' , three_shortest_path[0][-1]+path_length1+path_length2,'Km')

        print('Province to pass through shortest path Second is :',shortest_path1[:-1]+shortest_path2[:-1]+three_shortest_path[1][:-1] )
        print('Distance shortest path Second from',Province_start,'to',Province_end,'is:' , three_shortest_path[1][-1]+path_length1+path_length2,'Km')

        print('Province to pass through shortest path Third is :',shortest_path1[:-1]+shortest_path2[:-1]+three_shortest_path[2][:-1] )
        print('Distance shortest path Third from',Province_start,'to',Province_end,'is:' , three_shortest_path[2][-1]+path_length1+path_length2,'Km')
    if key == 4:
        break
    else:
        again = 'y'
"""
edge_labels = nx.get_edge_attributes(G,'weight')
pos = nx.spring_layout(G)
nx.draw(G,pos ,with_labels=True,font_color="black",font_size="5",node_size= 2000)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
plt.show()
   # again = input('Enter y to do again or n it exit: ')


