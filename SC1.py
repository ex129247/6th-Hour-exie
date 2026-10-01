#Name: Eden Xie
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.
EnemyStats={
    "Zombie":{
        "Damage":10,
        "Speed":5,
        "Health":100
    },
    "Skeleton": {
        "Damage": 5,
        "Speed": 10,
        "Health": 75
    },
    "Spider": {
        "Damage": 15,
        "Speed": 15,
        "Health": 50
    },
    "Creeper": {
        "Damage": 50,
        "Speed": 5,
        "Health": 25
    },
    "Slime": {
        "Damage": 2.5,
        "Speed": 2.5,
        "Health": 125
    },

}
ZombieDamage=int(input("Change Zombie damage to?"))
EnemyStats["Zombie"].update({"Damage":ZombieDamage})
SkeletonDamage=int(input("Change Skeleton damage to?"))
EnemyStats["Skeleton"].update({"Damage":SkeletonDamage})
SpiderDamage=int(input("Change Spider damage to?"))
EnemyStats["Spider"].update({"Damage":SpiderDamage})
CreeperDamage=int(input("Change Creeper damage to?"))
EnemyStats["Creeper"].update({"Damage":CreeperDamage})
SlimeDamage=int(input("Change Slime damage to?"))
EnemyStats["Slime"].update({"Damage":SlimeDamage})
print(EnemyStats)