import streamlit as st
import time

from Search_2D import env, env1
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
    ('Bi-directional Algorithm', 'D* Algorithm', 'LPA* Algorithm', 'Anytime D* Algorithm', 'RTAA* Algorithm'))

    # algorithm3d = st.sidebar.selectbox(
    # 'Choose among 3d algorithms',
    # ('D* 3D', 'LPA* 3D', 'ARA* 3D', 'RTAA* 3D'))

    environments = st.sidebar.selectbox(
    'Choose environment',
    ('env 1', 'env 2', 'env 3'))
 
    if option == 'D* Algorithm': 
        s_start = (5, 5)
        s_goal = (45, 25)
        if environments == 'env 1':
            dstar = DStar(s_start, s_goal, env)
            dstar.run(s_start, s_goal) 

        elif environments == 'env 2': 
            dstar = DStar(s_start, s_goal, env1)
            dstar.run(s_start, s_goal) 

    elif option == 'Bi-directional Algorithm': 
        x_start = (5, 5)
        x_goal = (45, 5)
        if environments == 'env 1': 
            start = time.time()
            bastar = BidirectionalAStar(x_start, x_goal, "euclidean", env)
            plot =  Plotting(x_start, x_goal, env)
            path, visited_fore, visited_back = bastar.searching()
            end = time.time()
            successMessage = ' ⌛ Time of execution of Bidirectional A* algorithm: ' + str((end-start) * 10**3) + ' ms'
            st.success(successMessage  )
            plot.animation_bi_astar(path, visited_fore, visited_back, "Bidirectional-A*")

        elif environments == 'env 2': 
            start = time.time()
            bastar = BidirectionalAStar(x_start, x_goal, "euclidean", env1)
            plot =  Plotting(x_start, x_goal, env1)
            path, visited_fore, visited_back = bastar.searching()
            end = time.time()
            successMessage = ' ⌛ Time of execution of Bidirectional A* algorithm: ' + str((end-start) * 10) + ' ms'
            st.success(successMessage  )
            plot.animation_bi_astar(path, visited_fore, visited_back, "Bidirectional-A*")
    
    elif option == 'LPA* Algorithm': 
       x_start = (5, 5)
       x_goal = (45, 25)
       if environments == 'env 1': 
           lpastar = LPAStar(x_start, x_goal, "Euclidean", env)
           lpastar.run()

       elif environments == 'env 2': 
           lpastar = LPAStar(x_start, x_goal, "Euclidean", env1)
           lpastar.run()

    elif option == 'Anytime D* Algorithm': 
       x_start = (5, 5)
       x_goal = (40, 25)
       if environments == 'env 1':
        dstar = ADStar(x_start, x_goal, 2.5, "euclidean", env)
        dstar.run()

       elif environments == 'env 2':
        dstar = ADStar(x_start, x_goal, 2.5, "euclidean", env1)
        dstar.run()
    
    elif option == 'RTAA* Algorithm':
       s_start = (10, 5)
       s_goal = (45, 25)

       if environments == 'env 1':
        start = time.time()
        rtaa = RTAAStar(s_start, s_goal, 240, "euclidean", env)
        plot = Plotting(s_start, s_goal, env)
        rtaa.searching()
        end = time.time()
        successMessage = ' ⌛ Time of execution of Real-time Adaptive A* (RTAA*) algorithm: ' + str((end-start) * 10**3) + ' ms'
        st.success(successMessage  )
            
        plot.animation_lrta(rtaa.path, rtaa.visited, "Real-time Adaptive A* (RTAA*)")

       if environments == 'env 2':
        start = time.time()
        rtaa = RTAAStar(s_start, s_goal, 240, "euclidean", env)
        plot = Plotting(s_start, s_goal, env1)
        rtaa.searching()
        plot.animation_lrta(rtaa.path, rtaa.visited, "Real-time Adaptive A* (RTAA*)")
        end = time.time()
    
        successMessage = ' ⌛ Time of execution of Real-time Adaptive A* (RTAA*) algorithm: ' + str((end-start) * 10**3) + ' ms'
        st.success(successMessage  )
            

    # elif algorithm3d == 'D* 3D': 
    #     D = D_star(1)
    #     D.run()



if __name__ == '__main__':
    main()