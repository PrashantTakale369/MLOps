class Car_System:
    def __init__(self):
        self.model = ""
        self.color = ""
        self.type = ""
        self.cc = ""
        self.menu()

    
    def menu(self):
        
        user_input = input(""" Hi how would i like to Help you ?? Please slect one Option,
                                    1. Press 1 for search model
                                    2. Press 2 for search color
                                    3. Press 3 for search type
                                    4. Press 4 for search cc
                                    5. Press 5 for search exit \n """)
    
        if user_input == "1":
            self.Select_model()
        elif user_input == "2":
            self.color_search()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input == "5":
            pass



    def Select_model(self):
        
        toyota_models = ["innova","fortuner","corolla","camry","glanza"]
        honda_models = ["city", "amaze", "cvic","jazz"]
        hyundai_models = [ "creta", "i20","verna","venue","alcazar"]
        tata_models = ["nexon","punch","harrier","safari","altroz"]

        user_input = input("""Select which Company model Do u Wnat : 
                           1.toyota_models
                           2.honda_models
                           3.hyundai_models
                           4.tata_models \n -- > """)
        
        if user_input == '1':
            car_list=toyota_models

        elif user_input == '2':
            car_list=honda_models

        elif user_input == '3':
            car_list=hyundai_models

        elif user_input == '4':
            car_list=tata_models

        else :
            print("Sorry !!")
            self.menu()
            return 
        

        search_car = input("Which car you want -- > ").strip().lower()

        if search_car in car_list:
             print("Which Car U Want is Avilable !! ")
        else :
             print("Sorry !! ")


        print("Task is Done")
        self.menu()


    def color_search(self):

        color = input("please tell us Which Color do you want -- > : ").strip().lower()
        color_arr = ["red" , "orange" , "yellow" , "pink" , "black" , "purpule" , "green"]

        tag = False
        for i in color_arr:    # we can do this also ( if color in color_arr )print{Yes}  oww that's amazing:
            if color == i:
                tag = True


        if tag == True:
            print("Yes !! Which Color u Want is Avilable : Please Procced -- > ")
        elif tag == False:
            print(" Soory  !! Which Color u Want is Out Of Avilable : Pleae Contact us -- > ")


        print("U Search Correcty !")
        print("\n")
        


    def type(self):
        pass
    def cc(self):
        pass
    def exit(self):
        pass


obj = Car_System()
