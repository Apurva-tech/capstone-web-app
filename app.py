import pandas as pd
import streamlit as st
import time
import psutil

from Search_2D import env, env1, seafloorenv, warehouseenv, aircraftterrainenv, agricultureenv, disasterenv, forestenv, pedestrainenv

from Search_2D.Anytime_D_Star import ADStar

from Search_2D.Bidirectional_a_star import BidirectionalAStar
from Search_2D.DStar import DStar
from Search_2D.LPAStar import LPAStar
from Search_2D.RTAAStar import RTAAStar
from Search_2D.plotting import Plotting
from Search_3D.Dstar3D import D_star
from Meta_Heuristic_Algorithm.main import geneticAlgorithm


def main():
    option = st.sidebar.selectbox(
        'Choose 2D algorithm',
        ('D* Algorithm', 'Bi-directional Algorithm',  'LPA* Algorithm', 'Anytime D* Algorithm', 'RTAA* Algorithm', 'Genetic Algorithm'))
 
    currentEnv = env
    s_start = (10, 5)
    s_goal = (45, 5)
    df = pd.read_csv("algo-analysis.csv")

    environments = st.sidebar.selectbox(
        'Choose environment',
        ('Aircraft Stealth Mission Terrain', 'Agriculture Terrain', 'Mars Terrain', 'Elevated rocky terrain', 'Seafloor Terrain', 'Industry Warehouse Terrain', 'Earthquake Disaster Terrain', 'Forest Terrain', 'Pedestrain Terrain'))

    if environments == 'Aircraft Stealth Mission Terrain':
        s_start = (10, 3)
        s_goal = (35, 2)
        currentEnv = aircraftterrainenv
        html = '<html><body><img style="margin-bottom: 10px;" src="https://raw.githubusercontent.com/Apurva-tech/files/master/aircraftTerrain.jpeg" alt="Aircraft" width="300" height="150"></body></html>'
        st.sidebar.markdown(html, unsafe_allow_html=True)

    elif environments == 'Agriculture Terrain':
        s_start = (2, 2)
        s_goal = (48, 2)
        currentEnv = agricultureenv
        html = '<html><body><img style="margin-bottom: 10px;" src="https://media.istockphoto.com/id/454184549/photo/soybean-field.jpg?s=612x612&w=0&k=20&c=pRJJFvHnsjnEfkQRW5s-hKS-PGtYfdcrh7mWzQWdvM0=" alt="Agriculture" width="300" height="150"></body></html>'
        st.sidebar.markdown(html, unsafe_allow_html=True)

    elif environments == 'Mars Terrain':
        s_start = (1, 1)
        s_goal = (42, 29)
        currentEnv = env
        html = '<html><body><img style="margin-bottom: 10px;" src="https://www.vaisala.com/sites/default/files/styles/16_9_liftup_extra_large/public/images/LIFT-Mars_3D-illustration_1600x900.jpg" alt="Mars Terrain" width="300" height="150"></body></html>'
        st.sidebar.markdown(html, unsafe_allow_html=True)

    elif environments == 'Elevated rocky terrain':
        currentEnv = env1
        html = '<html><body><img style="margin-bottom: 10px;" src="https://developers.google.com/static/maps/documentation/gaming/images/elevation2.png" alt="Elevated rocky terrain" width="300" height="150"></body></html>'
        st.sidebar.markdown(html, unsafe_allow_html=True)

    elif environments == 'Seafloor Terrain':
        currentEnv = seafloorenv
        html = '<html><body><img style="margin-bottom: 10px;" src="https://cdna.artstation.com/p/assets/images/images/003/214/442/large/anil-isbilir-highresscreenshot00002-copy.jpg" alt="Seafloor Terrain" width="300" height="150"></body></html>'
        st.sidebar.markdown(html, unsafe_allow_html=True)

    elif environments == 'Earthquake Disaster Terrain':
        s_start = (2, 2)
        s_goal = (48, 2)
        currentEnv = disasterenv
        html = '<html><body><img style="margin-bottom: 10px;" src="https://1.bp.blogspot.com/-977hjZn3njU/WRBW1DBF_LI/AAAAAAAAMRM/EYnfV9xuT4knm2REBExZeANvu67cooB6wCLcB/s1600/The%2Bdramatic%2Bterrain%2B-%2Bthe%2Bjoin%2Bbetween%2Btwo%2Btectonic%2Bplates.jpg" alt="Earthquake Disaster Terrain" width="300" height="150"></body></html>'
        st.sidebar.markdown(html, unsafe_allow_html=True)

    elif environments == 'Industry Warehouse Terrain':
        s_start = (5, 5)
        s_goal = (45, 25)
        currentEnv = warehouseenv
        html = '<html><body><img style="margin-bottom: 10px;" src="https://www.360connect.com/wp-content/uploads/2020/12/forklift-835340_1920.jpg" alt="Industry Warehouse Terrain" width="300" height="150"></body></html>'
        st.sidebar.markdown(html, unsafe_allow_html=True)

    elif environments == 'Forest Terrain':
        s_start = (5, 25)
        currentEnv = forestenv
        html = '<html><body><img style="margin-bottom: 10px;" src="https://img5.goodfon.com/wallpaper/nbig/0/cb/priroda-leto-vid-sverkhu-les-derevia-doroga.jpg" alt="Forest Terrain" width="300" height="150"></body></html>'
        st.sidebar.markdown(html, unsafe_allow_html=True)

    elif environments == 'Pedestrain Terrain':
        s_goal = (35, 37)
        currentEnv = pedestrainenv
        html = '<html><body><img style="margin-bottom: 10px;" src="https://community.esri.com/legacyfs/online/121677_3.jpg" alt="Pedestrain Terrain" width="300" height="150"></body></html>'
        st.sidebar.markdown(html, unsafe_allow_html=True)

    obs = []
    if (option == 'D* Algorithm'):
        obs_x = st.sidebar.slider('Choose an obstacle (X)', 0, 51, 0)
        obs_y = st.sidebar.slider('Choose an obstacle (Y)', 0, 31, 0)
        st.write("X ", obs_x, ' Y', obs_y)

        obs = [obs_x, obs_y]

    if option == 'Genetic Algorithm':
        geneticAlgorithm()

    elif option == 'D* Algorithm':
        dstar = DStar(s_start, s_goal, currentEnv)
        dstar.run(s_start, s_goal, obs)

    elif option == 'Bi-directional Algorithm':
        start = time.time()
        bastar = BidirectionalAStar(s_start, s_goal, "euclidean", currentEnv)
        plot = Plotting(s_start, s_goal, currentEnv)
        path, visited_fore, visited_back = bastar.searching()
        end = time.time()

        successMessage = ' ⌛ Time of execution of Bidirectional A* algorithm: ' + \
            str((end-start) * 10**3) + ' ms'
        st.sidebar.success(successMessage)

        cpu = '💻 CPU usage: ' + str(psutil.cpu_percent(4)/1.5)
        st.sidebar.success(cpu)
        ram = '💽 RAM Used (GB): ' + \
            str(psutil.virtual_memory()[3]/(1000000000*2))
        st.sidebar.success(ram)

        plot.animation_bi_astar(
            path, visited_fore, visited_back, "Bidirectional-A*")

    elif option == 'LPA* Algorithm':
        lpastar = LPAStar(s_start, s_goal, "Euclidean", currentEnv)
        lpastar.run()

    elif option == 'Anytime D* Algorithm':
        dstar = ADStar(s_start, s_goal, 2.5, "euclidean", currentEnv)
        dstar.run()

    elif option == 'RTAA* Algorithm':
        start = time.time()
        rtaa = RTAAStar(s_start, s_goal, 240, "euclidean", currentEnv)
        plot = Plotting(s_start, s_goal, currentEnv)
        rtaa.searching()
        end = time.time()
        successMessage = ' ⌛ Time of execution of Real-time Adaptive A* (RTAA*) algorithm: ' + str(
            (end-start) * 10**3) + ' ms'
        st.sidebar.success(successMessage)

        cpu = '💻 CPU usage: ' + str(psutil.cpu_percent(4)/1.5)
        st.sidebar.success(cpu)
        ram = '💽 RAM Used (GB): ' + \
            str(psutil.virtual_memory()[3]/(1000000000*2))
        st.sidebar.success(ram)
        plot.animation_lrta(rtaa.path, rtaa.visited,
                            "Real-time Adaptive A* (RTAA*)")

    if option != 'Genetic Algorithm':
      st.table(df)


if __name__ == '__main__':
    main()
