import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_edge('Loei','Nong Khai',weight=234)
G.add_edge('Loei','Nongbualamphu',weight=99)
G.add_edge('Loei','Khon Kaen',weight=207)
G.add_edge('Loei','Chaiyaphum',weight=227)
G.add_edge('Nong Khai','Udon Thani',weight=52)
G.add_edge('Nong Khai','Bueng Kan',weight=135)
G.add_edge('Nongbualamphu','Udon Thani',weight=51)
G.add_edge('Nongbualamphu','Khon Kaen',weight=118)
G.add_edge('Chaiyaphum','Khon Kaen',weight=140)
G.add_edge('Chaiyaphum','Nakhon Ratchasima',weight=121)
G.add_edge('Udon Thani','Bueng Kan',weight=207)
G.add_edge('Udon Thani','Sakon Nakhon',weight=166)
G.add_edge('Udon Thani','Kalasin',weight=147)
G.add_edge('Udon Thani','Khon Kaen',weight=121)
G.add_edge('Khon Kaen','Kalasin',weight=77)
G.add_edge('Khon Kaen','Maha Sarakham',weight=72)
G.add_edge('Khon Kaen','Nakhon Ratchasima',weight=192)
G.add_edge('Nakhon Ratchasima','Maha Sarakham',weight=214)
G.add_edge('Nakhon Ratchasima','Buri Ram',weight=127)
G.add_edge('Bueng Kan','Nakhon Phanom',weight=181)
G.add_edge('Bueng Kan','Sakon Nakhon',weight=195)
G.add_edge('Sakon Nakhon','Nakhon Phanom',weight=94)
G.add_edge('Sakon Nakhon','Mukdahan',weight=114)
G.add_edge('Sakon Nakhon','Kalasin',weight=129)
G.add_edge('Kalasin','Mukdahan',weight=164)
G.add_edge('Kalasin','Roi Et',weight=49)
G.add_edge('Kalasin','Maha Sarakham',weight=48)
G.add_edge('Maha Sarakham','Roi Et',weight=44)
G.add_edge('Maha Sarakham','Buri Ram',weight=149)
G.add_edge('Nakhon Phanom','Mukdahan',weight=110)
G.add_edge('Mukdahan','Roi Et',weight=149)
G.add_edge('Mukdahan','Yasothon',weight=115)
G.add_edge('Mukdahan','Amnat Charoen',weight=99)
G.add_edge('Roi Et','Yasothon',weight=68)
G.add_edge('Roi Et','Buri Ram',weight=149)
G.add_edge('Roi Et','Surin',weight=145)
G.add_edge('Roi Et','Si Sa Ket',weight=146)
G.add_edge('Buri Ram','Surin',weight=55)
G.add_edge('Si Sa Ket','Ubon Ratchathani',weight=65)
G.add_edge('Yasothon','Amnat Charoen',weight=57)
G.add_edge('Yasothon','Ubon Ratchathani',weight=103)
G.add_edge('Yasothon','Si Sa Ket',weight=103)
G.add_edge('Amnat Charoen','Ubon Ratchathani',weight=77)
G.add_edge('Surin','Si Sa Ket',weight=77)

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
        nx.draw(G,pos ,with_labels=True,font_color="black",font_size="5",node_size= 2000)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
        plt.show()
        again = input('Enter y to do again or n it exit: ')
except:
    print('End')





