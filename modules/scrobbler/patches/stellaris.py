# File contains last.fm metadata patches for the Stellaris game.

stellaris_patches = {
    "config": {
        "process_name": "stellaris",
    },
    "remove": [
        "Paradox Interactive & ",
        " (From Stellaris Original Game Soundtrack)",
        " (Original Game Soundtrack)",
    ],
    "replace": {
        # Patch artist
        "Martin Hall": "Meyer",
        # Patch track name
        "Stellaris Suite: Creation and Beyond": "Stellaris Suite (Creation & Beyond)",
        "To the End of the Galaxy": "To the Ends of the Galaxy (Instrumental)",
        "Infinite Being": "Infinite Being (Instrumental)",
        "Distant Nebula": "Distant Nebula (Instrumental)",
        "Faster Than Light": "Faster Than Light (Instrumental)",
        "Sigmatauri": "Sigma Tauri",
        "In Memory of Mr": "In Memory of Mercedes Romero",
        "The Federations Theme": "A Brighter Tomorrow",
        "Evil Federation Theme": "Hegemonic Dominion",
        "Galactic UN Theme": "Call to Assembly",
        "Diplomacy Theme": "Unity and Paperwork",
        "Journey Beyond the Galaxy": "Journey Through the Galaxy",
        "Super Massive Fleet": "Supermassive Fleet",
        "Robotics and Beyond": "Synthetic Dawn Main Theme",
        "Robotics": "Robo Sapiens",
        # Patch album name
        "Stellaris Megacorp": "Stellaris: Megacorp",
        "Stellaris Utopia": "Stellaris: Utopia",
        "Stellaris Synthethic Dawn": "Stellaris: Synthetic Dawn",
        "Stellaris: Distant Stars": "Stellaris Distant Stars",
    },
    "album": {
        "Stellaris: Ancient Relics": {
            "artist": "Meyer",
            "tracks": [
                "Among The Ruins",
                "Finding Sanctuary",
                "Abyss",
                "Our Heritage",
            ],
        },
        "Stellaris: Apocalypse": {
            "artist": "Meyer",
            "album_artist": "Meyer [feat. Andreas Waldetoft]",
            "tracks": [
                "Doomsday",
                "Hostile Fleet Detected",
                "Then Comes Light",
            ],
        },
        "Stellaris: Federations": {
            "artist": "Meyer",
            "tracks": [
                "A Brighter Tomorrow",
                "Hegemonic Dominion",
                "Call to Assembly",
                "Unity and Paperwork",
            ],
        },
        "Stellaris: Nemesis": {
            "artist": "Andreas Waldetoft",
            "tracks": [
                "Coronation of the Dark Emperor",
                "Nemesis Main Theme",
                "Supermassive Fleet",
            ],
        },
        "Stellaris Humanoids": {
            "artist": "Andreas Waldetoft",
            "album_artist": "Andreas Waldetoft & Meyer",
            "tracks": [
                "In Memory of Mr Luminous",
                "The Imperial Fleet Second Coming",
                "Towards Utopia Nova Flare",
            ],
        },
    },
}
