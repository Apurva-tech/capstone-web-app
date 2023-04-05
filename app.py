import streamlit as st
import time 
import psutil

from Search_2D import env, env1, seafloorenv, warehouseenv
from Search_2D.Anytime_D_Star import ADStar

from Search_2D.Bidirectional_a_star import BidirectionalAStar
from Search_2D.DStar import DStar
from Search_2D.LPAStar import LPAStar
from Search_2D.RTAAStar import RTAAStar
from Search_2D.plotting import Plotting
from Search_3D.Dstar3D import D_star

def main():
    option = st.sidebar.selectbox(
    'Choose 2D algorithm',
    ('D* Algorithm', 'Bi-directional Algorithm',  'LPA* Algorithm', 'Anytime D* Algorithm', 'RTAA* Algorithm'))

    # algorithm3d = st.sidebar.selectbox(
    # 'Choose among 3d algorithms',
    # ('D* 3D', 'LPA* 3D', 'ARA* 3D', 'RTAA* 3D'))

    currentEnv = env

    environments = st.sidebar.selectbox(
    'Choose environment',
    ('Mars Rover', 'Elevated rocky terrain', 'Seafloor Terrain', 'Industry Warehouse Terrain'))

    if environments == 'Mars Rover': 
       currentEnv = env
       html = '<html><body><img style="margin-bottom: 10px;" src="https://www.vaisala.com/sites/default/files/styles/16_9_liftup_extra_large/public/images/LIFT-Mars_3D-illustration_1600x900.jpg" alt="Mars rover" width="300" height="150"></body></html>'
       st.sidebar.markdown(html, unsafe_allow_html=True)

    elif environments == 'Elevated rocky terrain': 
       currentEnv = env1
       html = '<html><body><img style="margin-bottom: 10px;" src="https://developers.google.com/static/maps/documentation/gaming/images/elevation2.png" alt="Mars rover" width="300" height="150"></body></html>'
       st.sidebar.markdown(html, unsafe_allow_html=True)

    elif environments == 'Seafloor Terrain' :
       currentEnv = seafloorenv
       html = '<html><body><img style="margin-bottom: 10px;" src="https://cdna.artstation.com/p/assets/images/images/003/214/442/large/anil-isbilir-highresscreenshot00002-copy.jpg" alt="Mars rover" width="300" height="150"></body></html>'
       st.sidebar.markdown(html, unsafe_allow_html=True)
    
    elif environments == 'Industry Warehouse Terrain': 
       currentEnv = warehouseenv
       html = '<html><body><img style="margin-bottom: 10px;" src="https://www.360connect.com/wp-content/uploads/2020/12/forklift-835340_1920.jpg" alt="Mars rover" width="300" height="150"></body></html>'
       st.sidebar.markdown(html, unsafe_allow_html=True)
    
    
    if option == 'D* Algorithm': 
        s_start = (5, 5)
        s_goal = (45, 25)
        dstar = DStar(s_start, s_goal, currentEnv)
        dstar.run(s_start, s_goal) 

    elif option == 'Bi-directional Algorithm': 
        x_start = (5, 5)
        x_goal = (45, 5)

        start = time.time()
        bastar = BidirectionalAStar(x_start, x_goal, "euclidean", currentEnv)
        plot =  Plotting(x_start, x_goal, currentEnv)
        path, visited_fore, visited_back = bastar.searching()
        end = time.time()


        successMessage = ' ⌛ Time of execution of Bidirectional A* algorithm: ' + str((end-start) * 10**3) + ' ms'
        st.sidebar.success(successMessage)
        
        cpu = '💻 CPU usage: ' + str(psutil.cpu_percent(4))
        st.sidebar.success(cpu)
        ram = '💽 RAM Used (GB): ' + str(psutil.virtual_memory()[3]/1000000000)
        st.sidebar.success(ram)

        plot.animation_bi_astar(path, visited_fore, visited_back, "Bidirectional-A*")

    elif option == 'LPA* Algorithm': 
       x_start = (5, 5)
       x_goal = (45, 25)
       lpastar = LPAStar(x_start, x_goal, "Euclidean", currentEnv)
       lpastar.run() 

    elif option == 'Anytime D* Algorithm': 
       x_start = (5, 5)
       x_goal = (40, 25)
       dstar = ADStar(x_start, x_goal, 2.5, "euclidean", currentEnv)
       dstar.run() 
    
    elif option == 'RTAA* Algorithm':
       s_start = (10, 5)
       s_goal = (45, 25)

       start = time.time()
       rtaa = RTAAStar(s_start, s_goal, 240, "euclidean", currentEnv)
       plot = Plotting(s_start, s_goal, currentEnv)
       rtaa.searching()
       end = time.time()
       successMessage = ' ⌛ Time of execution of Real-time Adaptive A* (RTAA*) algorithm: ' + str((end-start) * 10**3) + ' ms'
       st.sidebar.success(successMessage)

       cpu = '💻 CPU usage: ' + str(psutil.cpu_percent(4))
       st.sidebar.success(cpu)
       ram = '💽 RAM Used (GB): ' + str(psutil.virtual_memory()[3]/1000000000)
       st.sidebar.success(ram)
       plot.animation_lrta(rtaa.path, rtaa.visited, "Real-time Adaptive A* (RTAA*)")




if __name__ == '__main__':
    main()