import time
import requests as req
import pyautogui
import animation
from playsound import playsound


@animation.simple_wait
def wait(x):
    time.sleep(x)
    return

#plants Plus(with seeds)
sunflowerplus = "images/sunflowerplus.PNG"
potatoplus = "images/potatoplus.PNG"
pumkinplus = "images/pumpkinPlus.PNG"
carrotplus = "images/carotPlus.PNG"
cabbageplus = "images/cabbagePlus.PNG"

#plants
sunflower = "images/sunflower.PNG"
potato = "images/potato.PNG"
pumpkin = "images/pumpkin.PNG"
carrot = "images/carrot.PNG"
cabbage = "images/cabbage"
#constant
inv = "images/inv.PNG"
hole = "images/hole.PNG"
chest = "images/chest.PNG"
button = "images/close.PNG"
goblin = "images/goblin_button.PNG"
token = "HERE_YOUR_TOKEN";  #HERE IS YOUR_TOKEN
url ="https://api.telegram.org/bot" + token + "/sendMessage?chat_id=HERE_YOUR_ID&text=";   #YOUR_CHAT_ID


# seeds on right side 
potatoseed = "images/potatoseed.PNG"
Plantseed = "images/Plantseed.PNG"
Plantseedinv = ""
#Inentory seeds
potatoseedinv = "images/potatoseedINV.PNG"
radishseedinv = "images/radishseedINV.PNG"
parshipseedinv = "images/parshipSeedINV.PNG"
cabbageseedinv = "images/cabbageSeedInv.PNG"
carotseedinv = "images/carotseedINV.PNG"
pumpkinseedinv = "images/pumpkinSeedInv.PNG"
Plantseedinv = "images/plantseedInv.PNG"

exit = "images/exit.PNG"
point = 0
z = 5

def tgsend(text):
    req.get(url + text)











# Plant(solnuch) potato pumkin carrot cabbage

def semena(variant):
    print("Choosing seeds")
    if variant == 0:
        return
    if variant == 1:
        seed = Plantseedinv  
    if variant == 2:
        seed = potatoseedinv
    if variant == 3:
        seed = pumpkinseedinv
    if variant ==4:
        seed = carotseedinv 
    if variant == 5:
        seed = cabbageseedinv
    if variant > 5:
        return  

    invLoc = pyautogui.locateOnScreen(inv, confidence=0.8)
    pyautogui.click(invLoc)
    time.sleep(1)
    seedLoc = pyautogui.locateOnScreen(seed, confidence=0.95)
    pyautogui.click(seedLoc)
    exitLoc = pyautogui.locateOnScreen(exit, confidence=0.8)
    pyautogui.click(exitLoc)
    return





# 1 (Plant(solnuch)) 2(potato) 3(pumkin) 4(carrot) 5(cabbage)

def posadka(variant):
        i=0
        while True:
            hole1Loc = pyautogui.locateOnScreen(hole, confidence=0.8)
            print("Hole on ", hole1Loc)            
            if hole1Loc == None:
                    break
            pyautogui.click(hole1Loc)
            i=i+1
            if i>30:
                playsound("clock.wav")
                tgsend("No seeds")
                return 0
            time.sleep(0.25)
        print("putting stage end")
        
        if variant == 1:
            print(60)
            wait(60)      
        if variant == 2:
            print(300)
            wait(300)      #300
        if variant == 3:
            print(1800)
            wait(1800)      #1800
        if variant == 4:
            print(3600)
            wait(3600)      #3600
        if variant == 5:
            print(7200)
            wait(7200)      #7200
 
        return
        
# 1 (Plant(solnuch)) 2(potato) 3(pumkin) 4(carrot) 5(cabbage)

def sbor(plant):
    b = 0
    if plant==0:
        print("I cant take the plants because, you didn't choose them :(")
        return
    if plant == 1:
        Plant =  sunflower
    if plant == 2:
        Plant = potato  
    if plant == 3:
        Plant =  pumpkin
    if plant == 4:
        Plant = carrot  
    if plant == 5:
        Plant = cabbage  
    while True:
        b=b+1
        PlantLoc = pyautogui.locateOnScreen(Plant, confidence=0.8)
        print("Plant on ", PlantLoc)
        if b>30:
            playsound("clock.wav")
            tgsend("Something wrong!")
            return 0
        if PlantLoc == None:
                break
        pyautogui.click(PlantLoc)
        time.sleep(0.5)
        goblinLoc = pyautogui.locateOnScreen(goblin, confidence=0.8)
        if goblinLoc != None:
            print("Goblin, i am sending message to your telegram")
            playsound("clock.wav")
            tgsend("Goblin!!!")
            print("Stopping...")
            return 0
        else:
            print("No goblin, I keep work ") 
        chestLoc = pyautogui.locateOnScreen(chest, confidence=0.4)
        if chestLoc != None:
            pyautogui.click(chestLoc)
            time.sleep(1)
            buttonLoc = pyautogui.locateOnScreen(button, confidence=0.8)
            pyautogui.click(buttonLoc)
        time.sleep(0.5)
    print("not any Plants")

# 1 (Plant(solnuch)) 2(potato) 3(pumkin) 4(carrot) 5(cabbage)

def sborPlus(variant):
    if variant == 0:
        print("no chance to take this")
        return
    if variant == 1:
        PlantPlus = sunflowerplus    
    if variant == 2:
        PlantPlus = potatoplus    
    if variant == 3:
        PlantPlus = pumkinplus    
    if variant == 4:
        PlantPlus = carrotplus    
    if variant == 5:
        PlantPlus = cabbageplus    
    while True:
        PlantPlusLoc = pyautogui.locateOnScreen(PlantPlus, confidence=0.8)
        print("Plant on ", PlantPlusLoc)
        if PlantPlusLoc == None:
            break
        pyautogui.click(PlantPlusLoc)
        time.sleep(1.5)
        
        chestLoc = pyautogui.locateOnScreen(chest, confidence=0.4)
            
        if chestLoc != None:
                pyautogui.click(chestLoc)
                

        time.sleep(1)
        buttonLoc = pyautogui.locateOnScreen(button, confidence=0.8)
        time.sleep(1)
        pyautogui.click(buttonLoc)

        time.sleep(0.5)
    print("not any Plants with seeds")






# Plant(solnuch) potato pumkin carrot cabbage

print("RadimSoftware ver 2.0")
varik = int(input("Press:\n1 for sunflower\n2 for potato\n3 for pumpkin\n4 for carrot\n5 for cabbage:"))

semena(varik)
wait(2)    
while True:
        if posadka(varik) == 0:
            break
        if sbor(varik) == 0:
            break
        if sborPlus(varik) == 0:
            break
            
        
   

# Примичание нет некоторых фотографий: соняшнк семеча   

 







