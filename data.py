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


hub01_pillar1 = sector([2, -14, -2, -14, -3, -15, 3, -15, ], gb_magenta2, gb_magenta, gb_black, -200, 3200, "Magenta Room")
hub01_pillar2 = sector([2, -14, 3, -15,3,-9, 2,-10, ], gb_magenta2, gb_magenta, gb_black, -400, 3200, "Magenta Room")
hub01_pillar3 = sector([-2,-10, -3,-9, -3, -15, -2, -14,], gb_magenta2, gb_magenta, gb_black, -400, 3200, "Magenta Room")
hub01_pillar4 = sector([-3, -9, -2, -10, 2, -10, 3, -9, ], gb_magenta2, gb_magenta, gb_black, -600, 3200, "Magenta Room")
hub01_room1 = sector([3, -15, -3, -15, -2, -20, 2, -20, ], gb_magenta2, gb_magenta, gb_black, 0, 3200, "Magenta Room")
hub01_room_center = sector([2, -20, -2, -20, 0, -24], gb_magenta2, gb_magenta, gb_black, 200, 3200, "Magenta Room")
hub01_room2 = sector([0, -24, -2, -20, -10, -24, -8, -28, ], gb_magenta2, gb_magenta, gb_black, 400, 3200, "Magenta Room")
hub01_room3 = sector([2, -20, 0, -24, 8, -28, 10, -24,], gb_magenta2, gb_magenta, gb_black, 400, 3200, "Magenta Room")
hub01_wing1 = sector([-2, -20, -3, -15, -15, -15, -10, -24,], gb_magenta2, gb_magenta, gb_magenta2, -200, 3200, "Magenta Room")
hub01_wing2 = sector([10, -24, 15, -15, 3, -15, 2, -20,], gb_magenta2, gb_magenta, gb_magenta2, -200, 3200, "Magenta Room")
hub01_wing3 = sector([-8,-28, 0,-32, 8,-28, 0,-24,], gb_magenta2, gb_magenta, gb_magenta2, 200, 3200, "Magenta Room")


# TODO
hub01_wing4 = sector([3, -15, 15, -15, -16,20], gb_magenta2, gb_magenta, gb_magenta2, -200, 3200, "Magenta Room")

hub01_wall1 = sector([-8,-28,-9,-29,0,-33,0,-32], gb_magenta2, gb_magenta, gb_magenta2, 1500, 3200, "Magenta Room")
hub01_wall2 = sector([0,-32, 0,-33, 9,-29, 8,-28,], gb_magenta2, gb_magenta, gb_magenta2, 1500, 3200, "Magenta Room")


join_sectorlist([final_step,
                 hub01_pillar1, hub01_pillar2, hub01_pillar3, hub01_pillar4,
                 hub01_room1,
                 hub01_room_center, hub01_room1, hub01_wing1,
                 hub01_wing2, hub01_wing3, hub01_room2, hub01_room3,
                 hub01_wall1, hub01_wall2])

current_sector = hub01_room_center
# current_sector = init_sector
topdown_max_depth = 5
