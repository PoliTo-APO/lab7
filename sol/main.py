from streaming.streaming_service import StreamingService


def main():
    print("----------------- R1 -----------------")
    ss = StreamingService()

    ss.add_movie(title="Pulp Fiction", year=1994, director="Quentin Tarantino", duration=154)
    ss.add_tv_show(title="Twin Peaks", year=1990, num_seasons=3, num_episodes=48)
    ss.add_tv_show(title="Freaks and Geeks", year=1999, num_seasons=1, num_episodes=18)
    ss.add_movie(title="There will be blood", year=2007, director="Paul Thomas Anderson", duration=158)
    ss.add_movie(title="After Hours", year=1985, director="Martin Scorsese", duration=97)

    m1 = ss.get_media_content("Pulp Fiction")
    print(m1.get_title())         # Pulp Fiction
    print(m1.get_year())          # 1994
    print(m1.get_content_type())  # movie
    print(m1)               # Pulp Fiction,1994,Quentin Tarantino,154

    tv1 = ss.get_media_content("Twin Peaks")
    print(tv1.get_title())        # Twin Peaks
    print(tv1.get_year())         # 1990
    print(tv1.get_content_type()) # tv show
    print(tv1)              # Twin Peaks,1990,3,48

    print("----------------- R2 -----------------")    
    ss.add_user("Andrea", 27)
    ss.add_user("Domenico", 17)
    ss.add_user("Giancarlo", 15)
    ss.add_user("Marco", 26)

    ss.watch("Andrea", "Pulp Fiction")
    ss.watch("Domenico", "Pulp Fiction")
    ss.watch("Domenico", "Twin Peaks")

    print([content.get_title() for content in ss.get_watched_by_user("Domenico")])        # ['Pulp Fiction', 'Twin Peaks']
    print([content.get_title() for content in ss.get_watched_by_user("Domenico", 1992)])  # ['Pulp Fiction']
    print(ss.get_watchers_of_content("Pulp Fiction"))                               # ['Andrea', 'Domenico']

    print(ss.get_watched_by_user("Giancarlo"))              # []
    print(ss.get_watchers_of_content("Freaks and Geeks"))   # []
    
    print("----------------- R3 -----------------")
    ss.add_rating("Andrea", "Pulp Fiction", 5)
    ss.add_rating("Domenico", "Pulp Fiction", 6)
    ss.add_rating("Giancarlo", "Pulp Fiction", 7)
    ss.add_rating("Marco", "Pulp Fiction", 8)
    ss.add_rating("Domenico", "Twin Peaks", 7)

    print("{:.1f}".format(ss.get_avg_content_rating("Pulp Fiction")))   # 6.5
    print("{:.1f}".format(ss.get_avg_content_rating("Twin Peaks")))     # 5.2
    print("{:.1f}".format(ss.get_avg_user_rating("Domenico")))          # 6.5

    print("----------------- R4 -----------------")
    ss.watch("Giancarlo", "Freaks and Geeks")
    print(ss.get_recommendations("Giancarlo"))  # []

    ss.watch("Domenico", "There will be blood")
    ss.watch("Domenico", "After Hours")
    print(ss.get_recommendations("Andrea"))     # ['Twin Peaks', 'After Hours', 'There will be blood']

    print("----------------- R5 -----------------")
    ss.add_movie(title="Avengers: Endgame", year=2019, director="Anthony Russo, Joe Russo", duration=181)
    ss.add_tv_show(title="WandaVision", year=2021, num_seasons=1, num_episodes=9)
    ss.add_tv_show(title="Loki", year=2021, num_seasons=1, num_episodes=6)
    ss.add_movie(title="Ant-Man and the Wasp", year=2018, director="Peyton Reed", duration=118)
    ss.add_movie(title="Avengers: Infinity War", year=2018, director="Anthony Russo, Joe Russo", duration=149)
    ss.add_movie(title="Thor: Ragnarok", year=2017, director="Taika David Cohen", duration=130)
    ss.add_movie(title="Spider-Man: Homecoming", year=2017, director="Jon Watts", duration=133)

    ss.set_previous_content("Avengers: Endgame", "WandaVision")
    ss.set_previous_content("Avengers: Endgame", "Loki")
    ss.set_previous_content("Avengers: Endgame", "Ant-Man and the Wasp")
    ss.set_previous_content("Ant-Man and the Wasp", "Avengers: Infinity War")
    ss.set_previous_content("Avengers: Infinity War", "Thor: Ragnarok")
    ss.set_previous_content("Avengers: Infinity War", "Spider-Man: Homecoming")

    print(ss.get_watch_list("Avengers: Endgame"))
    # ['WandaVision', 'Loki', 'Thor: Ragnarok', 'Spider-Man: Homecoming', 'Avengers: Infinity War', 'Ant-Man and the Wasp', 'Avengers: Endgame']
    # (Non necessariamente uguale, ma deve rispettare i vincoli)




if __name__ == "__main__":
    main()
