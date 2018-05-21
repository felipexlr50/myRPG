def getSqls():

    result = []

    sessionCreate = '''
    CREATE TABLE IF NOT EXISTS `rpg`.`session` (`id` VARCHAR(56) NOT NULL ,
    `ownerId` VARCHAR(56) NOT NULL , `name` TEXT NOT NULL ,
    `playersIds` TEXT NULL ,`users` TEXT NULL ,`description` TEXT NULL ,
    `progress` TEXT NULL ,`npcs` TEXT NULL ,`items` TEXT NULL ,`skills` TEXT NULL ,
    `quests` TEXT NULL ,`create_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,
    PRIMARY KEY (`id`)) ENGINE = MyISAM;'''
    result.append(sessionCreate)

    userCreate = '''
    CREATE TABLE IF NOT EXISTS `rpg`.`user` ( 
    `id` VARCHAR(56) NOT NULL  , 
    `name` TEXT NOT NULL , `email` TEXT NOT NULL , 
    `password` TEXT NOT NULL , 
    `sessions` TEXT NULL , 
    `chars` TEXT NULL ,
    create_data TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`id`)) ENGINE = MyISAM;'''
    result.append(userCreate)

    playerCreate = '''
    CREATE TABLE IF NOT EXISTS `rpg`.`player` ( 
    `id` VARCHAR(56) NOT NULL , 
    `name` TEXT NOT NULL , `race` TEXT NOT NULL , 
    `gender` TEXT NOT NULL , `job` TEXT NULL , 
    `story` TEXT NULL , `exp` TEXT NULL , `level` TEXT NULL , 
    `quests` TEXT NULL , `items` TEXT NULL , `skills` TEXT NULL , 
    `status_point` TEXT NULL , 
    `status` TEXT NULL ,
    create_data TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`id`)) ENGINE = MyISAM;'''
    result.append(playerCreate)

    itemCreate = '''
    CREATE TABLE IF NOT EXISTS `rpg`.`item` ( 
    `id` VARCHAR(56) NOT NULL  , `name` TEXT NOT NULL , 
    `description` TEXT NULL , `allow` TEXT NULL ,
    `value` INT NOT NULL DEFAULT '0' ,
    create_data TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`id`)) ENGINE = MyISAM;'''
    result.append(itemCreate)

    questCreate = '''
    CREATE TABLE IF NOT EXISTS `rpg`.`quest` ( `id` VARCHAR(56) NOT NULL  , 
    `name` TEXT NULL , 
    `objective` TEXT NULL , `reward` TEXT NOT NULL ,
    create_data TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`id`)) ENGINE = MyISAM;'''
    result.append(questCreate)

    skillCreate = '''
    CREATE TABLE IF NOT EXISTS `rpg`.`skill` ( 
    `id` VARCHAR(56) NOT NULL  , 
    `name` TEXT NOT NULL , `description` TEXT NOT NULL , 
    `dmg` INT NULL , `cost` INT NULL , `isPassive` INT NOT NULL ,
    create_data TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`id`)) ENGINE = MyISAM;'''
    result.append(skillCreate)

    npcCreate = '''
    CREATE TABLE IF NOT EXISTS `rpg`.`npc` ( 
    `id` VARCHAR(56) NOT NULL  , 
    `name` TEXT NOT NULL , `race` TEXT NOT NULL , 
    `gender` TEXT NOT NULL , `job` TEXT NULL , 
    `story` TEXT NULL , `level` TEXT NULL , 
    `items` TEXT NULL , `skills` TEXT NULL ,
    create_data TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (`id`)) ENGINE = MyISAM;'''
    result.append(npcCreate)

    masterCreate = '''
    CREATE TABLE IF NOT EXISTS rpg.master (
        `id` VARCHAR(56) NOT NULL ,
        userId VARCHAR(56) NOT NULL,
        sessionId VARCHAR(56) NOT NULL,
        create_data TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id),
        FOREIGN KEY (userId) REFERENCES user(id),
        FOREIGN KEY (sessionId) REFERENCES session(id)
    ) ENGINE = MyISAM;'''
    result.append(masterCreate)

    return result
