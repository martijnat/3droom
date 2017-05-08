all_sectors = []


init_sector = sector([-10, 0,
                      -10, -5,
                      -2, -10,
                      2, -10,
                      10, -5,
                      10, 0, ], gb_blue2, gb_white, gb_white2, 0, 1600, "Move using WASD and arrow keys")

init_path = sector([-2, -15,
                    2, -15,
                    2, -10,
                    -2, -10], gb_blue2, gb_black2, gb_black, 100, 1600, "")


init_red = sector([10, -18,
                   2, -15,
                   -2, -15,
                   -10, -18,
                   -10, -25,
                   10, -25,
                   ], gb_blue2, gb_red, gb_red2, 0, 1600, "Red room")

init_red_left = sector([-2, -14,
                        -10, -5,
                        -10, -18,
                        -2, -15,
                        ], gb_blue2, gb_red, gb_red2, 0, 1600, "Red room")

init_red_right = sector([10, -5,
                         2, -14,
                         2, -15,
                         10, -18,
                         ], gb_blue2, gb_red, gb_red2, 0, 1600, "Red room")

init_red_back = sector([-10, 0,
                        -10, -5,
                        -2, -14,
                        2, -14,
                        10, -5,
                        10, 0, ], gb_blue2, gb_red, gb_red2, 0, 1600, "Red room")

join_sectors(init_sector, init_path)
join_sectors(init_path, init_red)
join_sectors(init_red, init_red_left)
join_sectors(init_red, init_red_right)
join_sectors(init_red_back, init_red_left)
join_sectors(init_red_back, init_red_right)


last_step = init_red_back

rainbow = [gb_yellow, gb_green, gb_cyan, gb_blue, gb_magenta, gb_red, ]
rainbow2 = [gb_yellow2, gb_green2, gb_cyan2, gb_blue2, gb_magenta2, gb_red2, ]

for i in range(0, 19):
    c = 0.1 * pi
    c2 = 0
    new_step = sector([2, -14,
                       2 - 4 * (1 + c2 * i) * cos(c * i), -14 -
                       4 * (1 + c2 * i) * sin(c * i),
                       2 - 4 * (1 + c2 * (1 + i)) * cos(c * (i + 1)), -
                       14 - 4 * (1 + c2 * (1 + i)) * sin(c * (i + 1)),
                       ],
                      rainbow2[i % len(rainbow2)],
                      rainbow[i % len(rainbow)],
                      rainbow2[i % len(rainbow2)],
                      50 + 50 * i, 3200 + 50 * i, "Rainbow Staircase")
    join_sectors(last_step, new_step)
    last_step = new_step

i += 1
final_step = sector([2, -14,
                     2 - 4 * (1 + c2 * i) * cos(c * i), -14 -
                     4 * (1 + c2 * i) * sin(c * i),
                     -2, -14],
                    rainbow2[i % len(rainbow2)],
                    rainbow[i % len(rainbow)],
                    rainbow2[i % len(rainbow2)],
                    50 + 50 * i, 3200 + 50 * i, "Rainbow Staircase")
join_sectors(last_step, final_step)


magenta_room1 = sector([2, -14,
                        -2, -14,
                        -2, -20,
                        2, -20, ],
                       gb_blue2,
                       gb_magenta,
                       gb_black, 300, 3200, "Magenta Room")

magenta_room_center = sector([2, -20,
                              -2, -20,
                              0, -24],
                             gb_blue2,
                             gb_black2,
                             gb_black, 400, 3200, "Magenta Room")

magenta_room2 = sector([0, -24,
                        -2, -20,
                        -10, -24,
                        -8, -28, ],
                       gb_blue2,
                       gb_magenta,
                       gb_magenta2, 300, 3200, "Magenta Room")

magenta_room3 = sector([2, -20,
                        0, -24,
                        8, -28,
                        10, -24,
                        ],
                       gb_blue2,
                       gb_magenta,
                       gb_magenta2, 300, 3200, "Magenta Room")

topdown_max_depth = 8


join_sectors(final_step, magenta_room1)
join_sectors(magenta_room_center, magenta_room1)
join_sectors(magenta_room_center, magenta_room2)
join_sectors(magenta_room_center, magenta_room3)


magenta_room2a = sector([-8, -28,
                         -10, -24,
                        -13, -22,
                         -18, -22,
                         -18, -32,
                         -10, -36,
                         -8, -32,],
                       gb_blue2,
                       gb_magenta,
                       gb_magenta2, 250, 3200, "Magenta Room")

join_sectors(magenta_room2, magenta_room2a)


# hub = sector([2,-14 -i*0.1,
#               -2,-14 -i*3,
#               20,0,
#               10,0,
#              ],gb_blue2,gb_white,gb_white2,0,4800)

# join_sectors(last_step,hub)


# current_sector = init_sector


