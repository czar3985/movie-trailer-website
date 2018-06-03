import media


def get_content():
    # Movies included in the website and attributes for each
    thor_ragnarok = media.Movie(
        "Thor: Ragnarok",
        ("Imprisoned on the other side of the universe, the mighty Thor "
         "finds himself in a deadly gladiatorial contest that pits him "
         "against the Hulk, his former ally and fellow Avenger. Thor's "
         "quest for survival leads him in a race against time to prevent "
         "the all-powerful Hela from destroying his home world and the "
         "Asgardian civilization."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/7/7d/Thor_Ragnarok_poster.jpg"),
        "https://www.youtube.com/watch?v=ue80QwXMRHg")
    spiderman_homecoming = media.Movie(
        "Spider-Man: Homecoming",
        ("Thrilled by his experience with the Avengers, young Peter Parker "
         "returns home to live with his Aunt May. Under the watchful eye "
         "of mentor Tony Stark, Parker starts to embrace his newfound "
         "identity as Spider-Man. He also tries to return to his normal "
         "daily routine -- distracted by thoughts of proving himself to be "
         "more than just a friendly neighborhood superhero. Peter must soon "
         "put his powers to the test when the evil Vulture emerges to "
         "threaten everything that he holds dear."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/f/f9/Spider-Man_Homecoming_poster.jpg"),
        "https://www.youtube.com/watch?v=rk-dF1lIbIg")
    avengers_infinity_war = media.Movie(
        "Avengers: Infinity War",
        ("Iron Man, Thor, the Hulk and the rest of the Avengers unite to "
         "battle their most powerful enemy yet -- the evil Thanos. On a "
         "mission to collect all six Infinity Stones, Thanos plans to use "
         "the artifacts to inflict his twisted will on reality. The fate of "
         "the planet and existence itself has never been more uncertain as "
         "everything the Avengers have fought for has led up to this "
         "moment."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/4/4d/Avengers_Infinity_War_poster.jpg"),
        "https://www.youtube.com/watch?v=6ZfuNTqbHE8")
    captain_america_civil_war = media.Movie(
        "Captain America: Civil War",
        ("Political pressure mounts to install a system of accountability "
         "when the actions of the Avengers lead to collateral damage. The "
         "new status quo deeply divides members of the team. Captain "
         "America believes superheroes should remain free to defend "
         "humanity without government interference. Iron Man sharply "
         "disagrees and supports oversight. As the debate escalates into an "
         "all-out feud, Black Widow and Hawkeye must pick a side."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/5/53/Captain_America_Civil_War_poster.jpg"),
        "https://www.youtube.com/watch?v=dKrVegVI0Us")
    black_panther = media.Movie(
        "Black Panther",
        ("After the death of his father, T'Challa returns home to the "
         "African nation of Wakanda to take his rightful place as king. When"
         " a powerful enemy suddenly reappears, T'Challa's mettle as king --"
         " and as Black Panther -- gets tested when he's drawn into a "
         "conflict that puts the fate of Wakanda and the entire world at "
         "risk. Faced with treachery and danger, the young king must rally "
         "his allies and release the full power of Black Panther to defeat "
         "his foes and secure the safety of his people."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/0/0c/Black_Panther_film_poster.jpg"),
        "https://www.youtube.com/watch?v=xjDjIWPwcPU")
    antman_and_the_wasp = media.Movie(
        "Ant-Man and the Wasp",
        ("Scott Lang is grappling with the consequences of his choices as "
         "both a superhero and a father. Approached by Hope van Dyne and Dr."
         " Hank Pym, Lang must once again don the Ant-Man suit and fight "
         "alongside the Wasp. The urgent mission soon leads to secret "
         "revelations from the past as the dynamic duo finds itself in an "
         "epic battle against a powerful new enemy."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/2/2c/Ant-Man_and_the_Wasp_poster.jpg"),
        "https://www.youtube.com/watch?v=UUkn-enk2RU")
    guardians_2 = media.Movie(
        "Guardians of the Galaxy Vol. 2",
        ("Peter Quill and his fellow Guardians are hired by a powerful alien"
         " race, the Sovereign, to protect their precious batteries from "
         "invaders. When it is discovered that Rocket has stolen the items "
         "they were sent to guard, the Sovereign dispatch their armada to "
         "search for vengeance. As the Guardians try to escape, the mystery "
         "of Peter's parentage is revealed."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/a/ab/Guardians_of_the_Galaxy_Vol_2_poster.jpg"),
        "https://www.youtube.com/watch?v=dW1BIid8Osg")
    doctor_strange = media.Movie(
        "Doctor Strange",
        ("Dr. Stephen Strange's life changes after a car accident robs him "
         "of the use of his hands. When traditional medicine fails him, he "
         "looks for healing, and hope, in a mysterious enclave. He quickly "
         "learns that the enclave is at the front line of a battle against "
         "unseen dark forces bent on destroying reality. Before long, "
         "Strange is forced to choose between his life of fortune and status"
         " or leave it all behind to defend the world as the most powerful "
         "sorcerer in existence."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/c/c7/Doctor_Strange_poster.jpg"),
        "https://www.youtube.com/watch?v=HSzx-zryEgM")
    ant_man = media.Movie(
        "Ant-Man",
        ("Forced out of his own company by former protege Darren Cross, Dr. "
         "Hank Pym recruits the talents of Scott Lang, a master thief just "
         "released from prison. Lang becomes Ant-Man, trained by Pym and "
         "armed with a suit that allows him to shrink in size, possess "
         "superhuman strength and control an army of ants. The miniature "
         "hero must use his new skills to prevent Cross, also known as "
         "Yellowjacket, from perfecting the same technology and using it as "
         "a weapon for evil."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/7/75/Ant-Man_poster.jpg"),
        "https://www.youtube.com/watch?v=pWdKf3MneyI")
    age_of_ultron = media.Movie(
        "Avengers: Age of Ultron",
        ("When Tony Stark jump-starts a dormant peacekeeping program, things"
         " go terribly awry, forcing him, Thor, the Incredible Hulk and the "
         "rest of the Avengers to reassemble. As the fate of Earth hangs in "
         "the balance, the team is put to the ultimate test as they battle "
         "Ultron, a technological terror hell-bent on human extinction. "
         "Along the way, they encounter two mysterious and powerful "
         "newcomers, Pietro and Wanda Maximoff."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/f/ff/Avengers_Age_of_Ultron_poster.jpg"),
        "https://www.youtube.com/watch?v=tmeOjFno6Do")
    guardians_of_the_galaxy = media.Movie(
        "Guardians of the Galaxy",
        ("Brash space adventurer Peter Quill finds "
         "himself the quarry of relentless bounty hunters after he steals "
         "an orb coveted by Ronan, a powerful villain. To evade Ronan, "
         "Quill is forced into an uneasy truce with four disparate misfits: "
         "gun-toting Rocket Raccoon, treelike-humanoid Groot, enigmatic "
         "Gamora, and vengeance-driven Drax the Destroyer. But when he "
         "discovers the orb's true power and the cosmic threat it poses, "
         "Quill must rally his ragtag group to save the universe."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/b/b5/Guardians_of_the_Galaxy_poster.jpg"),
        "https://www.youtube.com/watch?v=2LIQ2-PZBC8")
    winter_soldier = media.Movie(
        "Captain America: The Winter Soldier",
        ("After the cataclysmic events in New York with his fellow Avengers,"
         " Steve Rogers, aka Captain America, lives in the nation's capital "
         "as he tries to adjust to modern times. An attack on a S.H.I.E.L.D."
         " colleague throws Rogers into a web of intrigue that places the "
         "whole world at risk. Joining forces with the Black Widow and a new"
         " ally, the Falcon, Rogers struggles to expose an ever-widening "
         "conspiracy, but he and his team soon come up against an unexpected"
         " enemy."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/e/e8/Captain_America_The_Winter_Soldier.jpg"),
        "https://www.youtube.com/watch?v=7SlILk2WMTI")
    thor_dark_world = media.Movie(
        "Thor: The Dark World",
        ("In ancient times, the gods of Asgard fought and won a war against "
         "an evil race known as the Dark Elves. The survivors were "
         "neutralized, and their ultimate weapon -- the Aether -- was buried"
         " in a secret location. Hundreds of years later, Jane Foster finds "
         "the Aether and becomes its host, forcing Thor to bring her to "
         "Asgard before Dark Elf Malekith captures her and uses the weapon "
         "to destroy the Nine Realms -- including Earth."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/7/7e/Thor_-_The_Dark_World_poster.jpg"),
        "https://www.youtube.com/watch?v=npvJ9FTgZbM")
    iron_man_3 = media.Movie(
        "Iron Man 3",
        ("Plagued with worry and insomnia since saving New York from "
         "destruction, Tony Stark, now, is more dependent on the suits that "
         "give him his Iron Man persona -- so much so that every aspect of "
         "his life is affected, including his relationship with Pepper. "
         "After a malevolent enemy known as the Mandarin reduces his "
         "personal world to rubble, Tony must rely solely on instinct and "
         "ingenuity to avenge his losses and protect the people he loves."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/d/d5/Iron_Man_3_theatrical_poster.jpg"),
        "https://www.youtube.com/watch?v=YLorLVa95Xo")
    avengers = media.Movie(
        "The Avengers",
        ("When Thor's evil brother, Loki , gains access to the unlimited "
         "power of the energy cube called the Tesseract, Nick Fury, director"
         " of S.H.I.E.L.D., initiates a superhero recruitment effort to "
         "defeat the unprecedented threat to Earth. Joining Fury's "
         "\"dream team\" are Iron Man, Captain America, the Hulk, Thor, the "
         "Black Widow and Hawkeye"),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/f/f9/TheAvengers2012Poster.jpg"),
        "https://www.youtube.com/watch?v=eOrNdBpGMv8")
    captain_america = media.Movie(
        "Captain America: The First Avenger",
        ("It is 1941 and the world is in the throes of war. Steve Rogers "
         "wants to do his part and join America's armed forces, but the "
         "military rejects him because of his small stature. Finally, Steve "
         "gets his chance when he is accepted into an experimental program "
         "that turns him into a supersoldier called Captain America. Joining"
         " forces with Bucky Barnes and Peggy Carter, Captain America leads "
         "the fight against the Nazi-backed HYDRA organization."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/3/37/Captain_America_The_First_Avenger_poster.jpg"),
        "https://www.youtube.com/watch?v=JerVrbLldXw")
    thor = media.Movie(
        "Thor",
        ("As the son of Odin, king of the Norse gods, Thor will soon inherit"
         " the throne of Asgard from his aging father. However, on the day "
         "that he is to be crowned, Thor reacts with brutality when the "
         "gods' enemies, the Frost Giants, enter the palace in violation of "
         "their treaty. As punishment, Odin banishes Thor to Earth. While "
         "Loki, Thor's brother, plots mischief in Asgard, Thor, now stripped"
         " of his powers, faces his greatest threat."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/f/fc/Thor_poster.jpg"),
        "https://www.youtube.com/watch?v=JOddp-nlNvQ")
    iron_man_2 = media.Movie(
        "Iron Man 2",
        ("With the world now aware that he is Iron Man, billionaire inventor"
         " Tony Stark faces pressure from all sides to share his technology "
         "with the military. He is reluctant to divulge the secrets of his "
         "armored suit, fearing the information will fall into the wrong "
         "hands. With Pepper Potts and Rhodes by his side, Tony must forge "
         "new alliances and confront a powerful new enemy."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/e/ed/Iron_Man_2_poster.jpg"),
        "https://www.youtube.com/watch?v=DIfgxIv5xmk")
    incredible_hulk = media.Movie(
        "The Incredible Hulk",
        ("Scientist Bruce Banner desperately seeks a cure for the gamma "
         "radiation that contaminated his cells and turned him into "
         "The Hulk. Cut off from his true love Betty Ross and forced to "
         "hide from his nemesis, Gen. Thunderbolt Ross, Banner soon comes "
         "face-to-face with a new threat: a supremely powerful enemy known "
         "as The Abomination."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/8/88/The_Incredible_Hulk_poster.jpg"),
        "https://www.youtube.com/watch?v=xbqNb2PFKKA")
    iron_man = media.Movie(
        "Iron Man",
        ("A billionaire industrialist and genius inventor, Tony Stark, is "
         "conducting weapons tests overseas, but terrorists kidnap him to "
         "force him to build a devastating weapon. Instead, he builds an "
         "armored suit and upends his captors. Returning to America, Stark "
         "refines the suit and uses it to combat crime and terrorism."),
        ("https://upload.wikimedia.org/wikipedia/"
         "en/7/70/Ironmanposter.JPG"),
        "https://www.youtube.com/watch?v=8hYlB38asDY")

    # Make a list of all movies in the website
    movies = [antman_and_the_wasp,
              avengers_infinity_war,
              black_panther,
              thor_ragnarok,
              spiderman_homecoming,
              guardians_2,
              doctor_strange,
              captain_america_civil_war,
              ant_man,
              age_of_ultron,
              guardians_of_the_galaxy,
              winter_soldier,
              thor_dark_world,
              iron_man_3,
              avengers,
              captain_america,
              thor,
              iron_man_2,
              incredible_hulk,
              iron_man]

    return movies
