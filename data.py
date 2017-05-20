all_sectors = []


init_sector = sector([-10, 0, -10, -5, -2, -10, 2, -10, 10, -5, 10, 0, ],
                     gb_blue2, gb_black, gb_black2, 0, 1600, "Move using WASD and arrow keys")
init_path1 = sector([-2, -11, 2, -11, 2, -10, -2, -10], gb_blue2,
                    gb_black, gb_black2, 50, 1600, "Move using WASD and arrow keys")
init_path2 = sector([-2, -12, 2, -12, 2, -11, -2, -11], gb_blue2,
                    gb_black, gb_black2, 100, 1600, "Move using WASD and arrow keys")
init_path3 = sector([-2, -13, 2, -13, 2, -12, -2, -12], gb_blue2,
                    gb_black, gb_black2, 150, 1600, "Move using WASD and arrow keys")
init_path4 = sector([-2, -14, 2, -14, 2, -13, -2, -13], gb_blue2,
                    gb_black, gb_black2, 200, 1600, "Move using WASD and arrow keys")
init_path5 = sector([-2, -15, 2, -15, 2, -14, -2, -14], gb_blue2,
                    gb_black, gb_black2, 250, 1600, "Move using WASD and arrow keys")


dummy = sector([0, 0, 0, 0, 0, 0], gb_blue2, gb_black,
               gb_black2, 150, 1600, "Dummy")
init_secret1 = sector([-10, 0, 10, 0, 9, 1, -9, 1],
                      gb_blue2, gb_black, gb_black2, 50, 1600, "?")
init_secret2 = sector([-9, 1, 9, 1, 8, 2, -8, 2], gb_blue2,
                      gb_black, gb_black2, 100, 1600, "?")
init_secret3 = sector([-8, 2, 8, 2, 7, 3, -7, 3], gb_blue2,
                      gb_black, gb_black2, 150, 1600, "?")
init_secret4 = sector([-7, 3, 7, 3, 6, 4, -6, 4], gb_blue2,
                      gb_black, gb_black2, 200, 1600, "?")
init_secret5 = sector([-6, 4, 6, 4, 3, 7, -3, 7], gb_blue2,
                      gb_black, gb_black2, 250, 1600, "?")


init_white = sector([10, -18, 2, -15, -2, -15, -10, -18, -10, -25, 10, -25, ],
                    gb_blue2, gb_white, gb_white2, 0, 1600, "A new perspective")
init_white_left = sector([-2, -14, -10, -5, -10, -18, -2, -15, ],
                         gb_blue2, gb_white, gb_white2, 0, 1600, "A new perspective")
init_white_right = sector([10, -5, 2, -14, 2, -15, 10, -18, ],
                          gb_blue2, gb_white, gb_white2, 0, 1600, "A new perspective")
init_white_back = sector([-10, 0, -10, -5, -2, -14, 2, -14, 10, -5, 10, 0, ],
                         gb_blue2, gb_white, gb_white2, 0, 1600, "A new perspective")


join_sectorlist([init_sector, init_path1, init_path2, init_path3, init_path4,
                 init_path5, init_secret1, init_secret2, init_secret3, init_secret4, init_secret5])
join_sectors(init_path5, init_white)
join_sectors(init_white, init_white_left)
join_sectors(init_white, init_white_right)
join_sectors(init_white_back, init_white_left)
join_sectors(init_white_back, init_white_right)


last_step = init_white_back

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
                      50 + 50 * i, 3600 + (i-19)*130 + 50 * i, "Going up")
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
                    50 + 50 * i, 3600 + 50 * i, "Going up")
join_sectors(last_step, final_step)

hub01_pillars = [sector([2, -14, -2, -14, -3, -15, 3, -15, ], gb_blue2, gb_white, gb_white2, 400, 3600, "Press space bar to jump"),
                 sector([2, -14, 3, -15, 3, -9, 2, -10, ], gb_blue2,
                        gb_white, gb_white2, 400, 3600, "Press space bar to jump"),
                 sector([-2, -10, -3, -9, -3, -15, -2, -14, ], gb_blue2,
                        gb_white, gb_white2, 400, 3600, "Press space bar to jump"),
                 sector([-3, -9, -2, -10, 2, -10, 3, -9, ], gb_blue2, gb_white, gb_white2, 400, 3600, "Press space bar to jump"), ]

hub01_tsplit = [sector([2, -20, -2, -20, 0, -24], gb_blue2, gb_white, gb_white2, 200, 3600, "Press space bar to jump"),
                sector([3, -15, -3, -15, -2, -20, 2, -20, ], gb_blue2,
                       gb_white, gb_white2, 300, 3600, "Press space bar to jump"),
                sector([0, -24, -2, -20, -10, -24, -8, -28, ], gb_blue2,
                       gb_white, gb_white2, 0, 3600, "Press space bar to jump"),
                sector([2, -20, 0, -24, 8, -28, 10, -24, ], gb_blue2, gb_white, gb_white2, 100, 3600, "Press space bar to jump")]

hub01_floor = [sector([-2, -20, -3, -15, -15, -15, -10, -24, ], gb_blue2, gb_white, gb_white2, 0, 3600, "Press space bar to jump"),
               sector([10, -24, 15, -15, 3, -15, 2, -20, ], gb_blue2,
                      gb_white, gb_white2, 0, 3600, "Press space bar to jump"),
               sector([3, -15, 15, -15, 15, -4, 3, -9, ], gb_blue2,
                      gb_white, gb_white2, 0, 3600, "Press space bar to jump"),
               sector([-3, -9, -15, -4, -15, -15, -3, -15, ], gb_blue2,
                      gb_white, gb_white2, 0, 3600, "Press space bar to jump"),
               sector([15, -4, 10, 1, 5, 3, -5, 3, -10, 1, -15, -4, -3, -9, 3, -9, ], gb_blue2, gb_white, gb_white2, 0, 3600, "Press space bar to jump")]

hub01_slices = [sector([0, -24, -8, -28, -8, -30, ], gb_blue2, gb_white, gb_white2, 0, 3600, "Press space bar to jump"),
                sector([0, -24, -8, -30, -8, -35, ], gb_blue2, gb_white,
                       gb_white2, 0, 3600, "Press space bar to jump"),
                sector([0, -24, -8, -35, -8, -40, ], gb_blue2, gb_white,
                       gb_white2, 0, 3600, "Press space bar to jump"),
                sector([0, -24, -8, -40, -8, -45, ], gb_blue2, gb_white,
                       gb_white2, 0, 3600, "Press space bar to jump"),
                sector([0, -24, -8, -45, -8, -50, ], gb_blue2, gb_white,
                       gb_white2, 0, 3600, "Press space bar to jump"),
                sector([0, -24, -8, -50, -8, -55, ], gb_blue2, gb_white,
                       gb_white2, 0, 3600, "Press space bar to jump"),
                sector([0, -24, -8, -55, -4, -55, ], gb_blue2, gb_white,
                       gb_white2, 0, 3600, "Press space bar to jump"),
                sector([0, -24, -4, -55,  0, -55, ], gb_blue2, gb_white,
                       gb_white2, 0, 3600, "Press space bar to jump"),
                sector([0, -24, 0, -55,  4, -55, ], gb_blue2, gb_white,
                       gb_white2, 0, 3600, "Press space bar to jump"),
                sector([0, -24, 4, -55,  8, -55, ], gb_blue2, gb_white,
                       gb_white2, 0, 3600, "Press space bar to jump"),
                sector([0, -24, 8, -55,  8, -50, ], gb_blue2, gb_white,
                       gb_white2, 0, 3600, "Press space bar to jump"),
                sector([0, -24, 8, -50,  8, -45, ], gb_blue2, gb_white,
                       gb_white2, 0, 3600, "Press space bar to jump"),
                sector([0, -24, 8, -45,  8, -40, ], gb_blue2, gb_white,
                       gb_white2, 0, 3600, "Press space bar to jump"),
                sector([0, -24, 8, -40,  8, -35, ], gb_blue2, gb_white,
                       gb_white2, 0, 3600, "Press space bar to jump"),
                sector([0, -24, 8, -35,  8, -30, ], gb_blue2, gb_white,
                       gb_white2, 0, 3600, "Press space bar to jump"),
                sector([0, -24, 8, -30,  8, -28, ], gb_blue2, gb_white, gb_white2, 0, 3600, "Press space bar to jump")]

hub01_platforms = [sector([10, -30, 10, -24, 8, -28,  8, -30, ], gb_blue2, gb_red, gb_white2, 400, 3600, "Press space bar to jump"),
                   sector([10, -35, 10, -30, 8, -30,  8, -35, ], gb_blue2,
                          gb_white, gb_white2, 0, 3600, "Press space bar to jump"),
                   sector([10, -40, 10, -35, 8, -35,  8, -40, ], gb_blue2,
                          gb_green, gb_white2, 600, 3600, "Press space bar to jump"),
                   sector([10, -45, 10, -40, 8, -40,  8, -45, ], gb_blue2,
                          gb_white, gb_white2, 0, 3600, "Press space bar to jump"),
                   sector([10, -50, 10, -45, 8, -45,  8, -50, ], gb_blue2,
                          gb_blue, gb_white2, 800, 3600, "Press space bar to jump"),
                   sector([10, -55, 10, -50, 8, -50,  8, -55, ], gb_blue2,
                          gb_white, gb_white2, 0, 3600, "Press space bar to jump"),

                   sector([-8, -30, -8, -28, -10, -24, -10, -30, ], gb_blue2,
                          gb_cyan, gb_white2, 1200, 3600, "Press space bar to jump"),
                   sector([-8, -35, -8, -30, -10, -30, -10, -35, ], gb_blue2,
                          gb_white, gb_white2, 1200, 3600, "Press space bar to jump"),
                   sector([-8, -40, -8, -35, -10, -35, -10, -40, ], gb_blue2,
                          gb_magenta, gb_white2, 1200, 3600, "Press space bar to jump"),
                   sector([-8, -45, -8, -40, -10, -40, -10, -45, ], gb_blue2,
                          gb_white, gb_white2, 1200, 3600, "Press space bar to jump"),
                   sector([-8, -50, -8, -45, -10, -45, -10, -50, ], gb_blue2,
                          gb_yellow, gb_white2, 1200, 3600, "Press space bar to jump"),
                   sector([-8, -55, -8, -50, -10, -50, -10, -55, ], gb_blue2,
                          gb_white, gb_white2, 1200, 3600, "Press space bar to jump"),
                   ]

join_sectorlist([final_step] + hub01_pillars + hub01_tsplit +
                hub01_floor + hub01_slices + hub01_platforms)

blue_connector1 = sector([10, -45, 10, -50, 18, -42, 10, -42, ],
                         gb_blue2, gb_blue, gb_blue2, 800, 3600, "...")
blue_connector2 = sector([18, -42, 10, -35, 10, -40, 10, -42, ],
                         gb_blue2, gb_blue, gb_blue2, 800, 3600, "...")

join_sectorlist(hub01_platforms + [blue_connector1])
join_sectorlist([blue_connector1, blue_connector2])

hub02_pillars = [sector([2, -14, -2, -14, -3, -15, 3, -15, ], gb_blue2, gb_white, gb_blue, 400, 3600, "Something is different"),
                 sector([2, -14, 3, -15, 3, -9, 2, -10, ], gb_blue2,
                        gb_white, gb_blue, 400, 3600, "Something is different"),
                 sector([-2, -10, -3, -9, -3, -15, -2, -14, ], gb_blue2,
                        gb_white, gb_blue, 400, 3600, "Something is different"),
                 sector([-3, -9, -2, -10, 2, -10, 3, -9, ], gb_blue2, gb_white, gb_blue, 400, 3600, "Something is different"), ]

hub02_tsplit = [sector([2, -20, -2, -20, 0, -24], gb_blue2, gb_white, gb_blue, 400, 3600, "Something is different"),
                sector([3, -15, -3, -15, -2, -20, 2, -20, ], gb_blue2,
                       gb_white, gb_blue, 400, 3600, "Something is different"),
                sector([0, -24, -2, -20, -10, -24, -8, -28, ], gb_blue2,
                       gb_white, gb_blue, 400, 3600, "Something is different"),
                sector([2, -20, 0, -24, 8, -28, 10, -24, ], gb_blue2, gb_white, gb_blue, 400, 3600, "Something is different")]

hub02_floor = [sector([-2, -20, -3, -15, -15, -15, -10, -24, ], gb_blue2, gb_white, gb_blue, 0, 3600, "Something is different"),
               sector([10, -24, 15, -15, 3, -15, 2, -20, ], gb_blue2,
                      gb_white, gb_blue, 0, 3600, "Something is different"),
               sector([3, -15, 15, -15, 15, -4, 3, -9, ], gb_blue2,
                      gb_white, gb_blue, 0, 3600, "Something is different"),
               sector([-3, -9, -15, -4, -15, -15, -3, -15, ], gb_blue2,
                      gb_white, gb_blue, 0, 3600, "Something is different"),
               sector([15, -4, 10, 1, 5, 3, -5, 3, -10, 1, -15, -4, -3, -9, 3, -9, ], gb_blue2, gb_white, gb_blue, 200, 3600, "Something is different")]

hub02_slices = [sector([0, -24, -8, -28, -8, -30, ], gb_blue2, gb_white, gb_blue, 0, 3600, "Something is different"),
                sector([0, -24, -8, -30, -8, -35, ], gb_blue2, gb_white,
                       gb_blue, 0, 3600, "Something is different"),
                sector([0, -24, -8, -35, -8, -40, ], gb_blue2, gb_white,
                       gb_blue, 0, 3600, "Something is different"),
                sector([0, -24, -8, -40, -8, -45, ], gb_blue2, gb_white,
                       gb_blue, 0, 3600, "Something is different"),
                sector([0, -24, -8, -45, -8, -50, ], gb_blue2, gb_white,
                       gb_blue, 0, 3600, "Something is different"),
                sector([0, -24, -8, -50, -8, -55, ], gb_blue2, gb_white,
                       gb_blue, 0, 3600, "Something is different"),
                sector([0, -24, -8, -55, -4, -55, ], gb_blue2, gb_white,
                       gb_blue, 0, 3600, "Something is different"),
                sector([0, -24, -4, -55,  0, -55, ], gb_blue2, gb_white,
                       gb_blue, 0, 3600, "Something is different"),
                sector([0, -24, 0, -55,  4, -55, ], gb_blue2, gb_white,
                       gb_blue, 0, 3600, "Something is different"),
                sector([0, -24, 4, -55,  8, -55, ], gb_blue2, gb_white,
                       gb_blue, 0, 3600, "Something is different"),
                sector([0, -24, 8, -55,  8, -50, ], gb_blue2, gb_white,
                       gb_blue, 0, 3600, "Something is different"),
                sector([0, -24, 8, -50,  8, -45, ], gb_blue2, gb_white,
                       gb_blue, 0, 3600, "Something is different"),
                sector([0, -24, 8, -45,  8, -40, ], gb_blue2, gb_white,
                       gb_blue, 0, 3600, "Something is different"),
                sector([0, -24, 8, -40,  8, -35, ], gb_blue2, gb_white,
                       gb_blue, 0, 3600, "Something is different"),
                sector([0, -24, 8, -35,  8, -30, ], gb_blue2, gb_white,
                       gb_blue, 0, 3600, "Something is different"),
                sector([0, -24, 8, -30,  8, -28, ], gb_blue2, gb_white, gb_blue, 0, 3600, "Something is different")]

hub02_platforms = [sector([10, -30, 10, -24, 8, -28,  8, -30, ], gb_blue2, gb_red, gb_blue, 400, 3600, "Something is different"),
                   sector([10, -35, 10, -30, 8, -30,  8, -35, ], gb_blue2,
                          gb_white, gb_blue, 0, 3600, "Something is different"),
                   sector([10, -40, 10, -35, 8, -35,  8, -40, ], gb_blue2,
                          gb_blue, gb_blue, 600, 3600, "Something is different"),
                   sector([10, -45, 10, -40, 8, -40,  8, -45, ], gb_blue2,
                          gb_white, gb_blue, 0, 3600, "Something is different"),
                   sector([10, -50, 10, -45, 8, -45,  8, -50, ], gb_blue2,
                          gb_green, gb_blue, 800, 3600, "Something is different"),
                   sector([10, -55, 10, -50, 8, -50,  8, -55, ], gb_blue2,
                          gb_white, gb_blue, 0, 3600, "Something is different"),

                   sector([-8, -30, -8, -28, -10, -24, -10, -30, ], gb_blue2,
                          gb_cyan, gb_blue, 1200, 3600, "Something is different"),
                   sector([-8, -35, -8, -30, -10, -30, -10, -35, ], gb_blue2,
                          gb_white, gb_blue, 0, 3600, "Something is different"),
                   sector([-8, -40, -8, -35, -10, -35, -10, -40, ], gb_blue2,
                          gb_magenta, gb_blue, 1200, 3600, "Something is different"),
                   sector([-8, -45, -8, -40, -10, -40, -10, -45, ], gb_blue2,
                          gb_white, gb_blue, 0, 3600, "Something is different"),
                   sector([-8, -50, -8, -45, -10, -45, -10, -50, ], gb_blue2,
                          gb_yellow, gb_blue, 1200, 3600, "Something is different"),
                   sector([-8, -55, -8, -50, -10, -50, -10, -55, ], gb_blue2,
                          gb_white, gb_blue, 0, 3600, "Something is different"),
                   ]


hub03_pillars = [sector([2, -14, -2, -14, -3, -15, 3, -15, ], gb_blue2, gb_green, gb_black2, 100, 3600, "There is no wall there"),
                 sector([2, -14, 3, -15, 3, -9, 2, -10, ], gb_blue2,
                        gb_green, gb_black2, 100, 3600, "There is no wall there"),
                 sector([-2, -10, -3, -9, -3, -15, -2, -14, ], gb_blue2,
                        gb_green, gb_black2, 100, 3600, "There is no wall there"),
                 sector([-3, -9, -2, -10, 2, -10, 3, -9, ], gb_blue2, gb_green, gb_black2, 100, 3600, "There is no wall there"), ]

hub03_tsplit = [sector([2, -20, -2, -20, 0, -24], gb_blue2, gb_green, gb_black2, 200, 3600, "There is no wall there"),
                sector([3, -15, -3, -15, -2, -20, 2, -20, ], gb_blue2,
                       gb_green, gb_black2, 100, 3600, "There is no wall there"),
                sector([0, -24, -2, -20, -10, -24, -8, -28, ], gb_blue,
                       gb_green, gb_green2, 0, 3600, "There is no wall there"),
                sector([2, -20, 0, -24, 8, -28, 10, -24, ], gb_blue, gb_green, gb_green2, 0, 3600, "There is no wall there")]

hub03_floor = [sector([-2, -20, -3, -15, -15, -15, -10, -24, ], gb_blue, gb_green, gb_green2, 0, 3600, "There is no wall there"),
               sector([10, -24, 15, -15, 3, -15, 2, -20, ], gb_blue,
                      gb_green, gb_green2, 0, 3600, "There is no wall there"),
               sector([3, -15, 15, -15, 15, -4, 3, -9, ], gb_blue,
                      gb_green, gb_green2, 0, 3600, "There is no wall there"),
               sector([-3, -9, -15, -4, -15, -15, -3, -15, ], gb_blue,
                      gb_green, gb_green2, 0, 3600, "There is no wall there"),
               sector([15, -4, 10, 1, 5, 3, -5, 3, -10, 1, -15, -4, -3, -9, 3, -9, ], gb_blue, gb_green, gb_green2, 0, 3600, "There is no wall there")]

hub03_slices = [sector([0, -24, -8, -28, -8, -30, ], gb_blue, gb_green, gb_black2, 200, 3600, "There is no wall there"),
                sector([0, -24, -8, -30, -8, -35, ], gb_blue2, gb_green, gb_green2, 250, 3600, "There is no wall there"),
                sector([0, -24, -8, -35, -8, -40, ], gb_blue, gb_green, gb_black2, 300, 3600, "There is no wall there"),
                sector([0, -24, -8, -40, -8, -45, ], gb_blue2, gb_green, gb_green2, 350, 3600, "There is no wall there"),
                sector([0, -24, -8, -45, -8, -50, ], gb_blue, gb_green, gb_black2, 400, 3600, "There is no wall there"),
                sector([0, -24, -8, -50, -8, -55, ], gb_blue2, gb_green, gb_green2, 450, 3600, "There is no wall there"),
                sector([0, -24, -8, -55, -4, -55, ], gb_blue, gb_green, gb_black2, 500, 3600, "There is no wall there"),
                sector([0, -24, -4, -55,  0, -55, ], gb_blue2, gb_green, gb_green2, 550, 3600, "There is no wall there"),
                sector([0, -24, 0, -55,  4, -55, ], gb_blue, gb_green, gb_black2, 550, 3600, "There is no wall there"),
                sector([0, -24, 4, -55,  8, -55, ], gb_blue2, gb_green, gb_green2, 500, 3600, "There is no wall there"),
                sector([0, -24, 8, -55,  8, -50, ], gb_blue, gb_green, gb_black2, 450, 3600, "There is no wall there"),
                sector([0, -24, 8, -50,  8, -45, ], gb_blue2, gb_green, gb_green2, 400, 3600, "There is no wall there"),
                sector([0, -24, 8, -45,  8, -40, ], gb_blue, gb_green, gb_black2, 350, 3600, "There is no wall there"),
                sector([0, -24, 8, -40,  8, -35, ], gb_blue2, gb_green, gb_green2, 300, 3600, "There is no wall there"),
                sector([0, -24, 8, -35,  8, -30, ], gb_blue, gb_green, gb_black2, 250, 3600, "There is no wall there"),
                sector([0, -24, 8, -30,  8, -28, ], gb_blue2, gb_green, gb_green2, 200, 3600, "There is no wall there")]

hub03_platforms = [sector([10, -30, 10, -24, 8, -28,  8, -30, ], gb_blue, gb_red, gb_black2, 400, 3600, "There is no wall there"),
                   sector([10, -35, 10, -30, 8, -30,  8, -35, ], gb_blue,
                          gb_green, gb_green2, 0, 3600, "There is no wall there"),
                   sector([10, -40, 10, -35, 8, -35,  8, -40, ], gb_blue2,
                          gb_green, gb_black2, 600, 3600, "There is no wall there"),
                   sector([10, -45, 10, -40, 8, -40,  8, -45, ], gb_blue,
                          gb_green, gb_green2, 0, 3600, "There is no wall there"),
                   sector([10, -50, 10, -45, 8, -45,  8, -50, ], gb_blue,
                          gb_blue, gb_black2, 800, 3600, "There is no wall there"),
                   sector([10, -55, 10, -50, 8, -50,  8, -55, ], gb_blue,
                          gb_green, gb_green2, 0, 3600, "There is no wall there"),

                   sector([-8, -30, -8, -28, -10, -24, -10, -30, ], gb_blue,
                          gb_cyan, gb_black2, 1200, 3600, "There is no wall there"),
                   sector([-8, -35, -8, -30, -10, -30, -10, -35, ], gb_blue,
                          gb_green, gb_green2, 0, 3600, "There is no wall there"),
                   sector([-8, -40, -8, -35, -10, -35, -10, -40, ], gb_blue,
                          gb_magenta, gb_black2, 1200, 3600, "There is no wall there"),
                   sector([-8, -45, -8, -40, -10, -40, -10, -45, ], gb_blue,
                          gb_green, gb_green2, 0, 3600, "There is no wall there"),
                   sector([-8, -50, -8, -45, -10, -45, -10, -50, ], gb_blue,
                          gb_yellow, gb_black2, 1200, 3600, "There is no wall there"),
                   sector([-8, -55, -8, -50, -10, -50, -10, -55, ], gb_blue,
                          gb_green, gb_green2, 0, 3600, "There is no wall there"),
                   ]

hub_connector1 = sector([-2, -10, -2, -12, 2, -12, 2, -10, ],
                        gb_blue2, gb_green, gb_black2, 300, 3600, "A new backdrop")
hub_connector2 = sector([-2, -12, -2, -14, 2, -14, 2, -12, ],
                        gb_blue2, gb_green, gb_black2, 200, 3600, "A new backdrop")

bridge_connector1 = sector([15, -40, 10, -35, 10, -40, 10, -42], gb_green,
                           gb_green, gb_green, 800, 3600, "You do not need to reach the end")
bridge_connector2 = sector([10, -42, 10, -44, 15, -50, 15, -40, ], gb_green,
                           gb_green, gb_green, 800, 3600, "You do not need to reach the end")
bridge_connector3 = sector([15, -50, 10, -44, 10, -50, 11, -55, ], gb_green,
                           gb_green, gb_green, 800, 3600, "You do not need to reach the end")
bridge_connector4 = sector([-10, -55, 11, -55, 10, -50, -10, -50, ], gb_blue2,
                           gb_yellow, gb_yellow2, 800, 3600, "You do not need to reach the end")
bridge_connector5 = sector([-10, -50, -20, -50, -20, -55, -10, -55, ], gb_blue2,
                           gb_yellow, gb_yellow2, 800, 3600, "You do not need to reach the end")
bridge_connector6 = sector([-20, -50, -10, -50, -10, -45, -20, -45, ], gb_yellow,
                           gb_yellow, gb_yellow, 1000, 3600, "You do not need to reach the end")


join_sectorlist([blue_connector2, hub_connector1] + hub02_pillars +
                hub02_tsplit + hub02_floor + hub02_slices + hub02_platforms)
join_sectors(hub_connector1, hub_connector2)
join_sectorlist([hub_connector2, bridge_connector1, bridge_connector2] +
                hub03_pillars + hub03_tsplit + hub03_floor + hub03_slices + hub03_platforms)
join_sectorlist([bridge_connector2, bridge_connector3,
                 bridge_connector4, bridge_connector5, bridge_connector6])

hub04_pillars = [sector([2, -14, -2, -14, -3, -15, 3, -15, ], gb_blue2, gb_yellow, gb_yellow2, 400, 3600, "Back and forth"),
                 sector([2, -14, 3, -15, 3, -9, 2, -10, ], gb_blue2,
                        gb_yellow, gb_yellow2, 400, 3600, "Back and forth"),
                 sector([-2, -10, -3, -9, -3, -15, -2, -14, ], gb_blue2,
                        gb_yellow, gb_yellow2, 400, 3600, "Back and forth"),
                 sector([-3, -9, -2, -10, 2, -10, 3, -9, ], gb_blue2, gb_yellow, gb_yellow2, 400, 3600, "Back and forth"), ]

hub04_tsplit = [sector([2, -20, -2, -20, 0, -24], gb_blue2, gb_yellow, gb_yellow2, 400, 3600, "Back and forth"),
                sector([3, -15, -3, -15, -2, -20, 2, -20, ], gb_blue2,
                       gb_yellow, gb_yellow2, 400, 3600, "Back and forth"),
                sector([0, -24, -2, -20, -10, -24, -8, -28, ], gb_blue2,
                       gb_yellow, gb_yellow2, 400, 3600, "Back and forth"),
                sector([2, -20, 0, -24, 8, -28, 10, -24, ], gb_blue2, gb_yellow, gb_yellow2, 400, 3600, "Back and forth")]

hub04_floor = [sector([-2, -20, -3, -15, -15, -15, -10, -24, ], gb_blue2, gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
               sector([10, -24, 15, -15, 3, -15, 2, -20, ], gb_blue2,
                      gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
               sector([3, -15, 15, -15, 15, -4, 3, -9, ], gb_blue2,
                      gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
               sector([-3, -9, -15, -4, -15, -15, -3, -15, ], gb_blue2,
                      gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
               sector([15, -4, 10, 1, 5, 3, -5, 3, -10, 1, -15, -4, -3, -9, 3, -9, ], gb_blue2, gb_yellow, gb_yellow2, 0, 3600, "Back and forth")]

hub04_slices = [sector([0, -24, -8, -28, -8, -30, ], gb_blue2, gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
                sector([0, -24, -8, -30, -8, -35, ], gb_blue2,
                       gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
                sector([0, -24, -8, -35, -8, -40, ], gb_blue2,
                       gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
                sector([0, -24, -8, -40, -8, -45, ], gb_blue2,
                       gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
                sector([0, -24, -8, -45, -8, -50, ], gb_blue2,
                       gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
                sector([0, -24, -8, -50, -8, -55, ], gb_blue2,
                       gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
                sector([0, -24, -8, -55, -4, -55, ], gb_blue2,
                       gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
                sector([0, -24, -4, -55,  0, -55, ], gb_blue2,
                       gb_yellow, gb_yellow2, 400, 3600, "Back and forth"),
                sector([0, -24, 0, -55,  4, -55, ], gb_blue2, gb_yellow,
                       gb_yellow2, 400, 3600, "Back and forth"),
                sector([0, -24, 4, -55,  8, -55, ], gb_blue2,
                       gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
                sector([0, -24, 8, -55,  8, -50, ], gb_blue2,
                       gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
                sector([0, -24, 8, -50,  8, -45, ], gb_blue2,
                       gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
                sector([0, -24, 8, -45,  8, -40, ], gb_blue2,
                       gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
                sector([0, -24, 8, -40,  8, -35, ], gb_blue2,
                       gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
                sector([0, -24, 8, -35,  8, -30, ], gb_blue2,
                       gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
                sector([0, -24, 8, -30,  8, -28, ], gb_blue2, gb_yellow, gb_yellow2, 0, 3600, "Back and forth")]

hub04_platforms = [sector([10, -30, 10, -24, 8, -28,  8, -30, ], gb_blue2, gb_red, gb_black2, 400, 3600, "Back and forth"),
                   sector([10, -35, 10, -30, 8, -30,  8, -35, ], gb_blue2,
                          gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
                   sector([10, -40, 10, -35, 8, -35,  8, -40, ], gb_blue2,
                          gb_green, gb_black2, 600, 3600, "Back and forth"),
                   sector([10, -45, 10, -40, 8, -40,  8, -45, ], gb_blue2,
                          gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
                   sector([10, -50, 10, -45, 8, -45,  8, -50, ], gb_blue2,
                          gb_blue, gb_black2, 800, 3600, "Back and forth"),
                   sector([10, -55, 10, -50, 8, -50,  8, -55, ], gb_blue2,
                          gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),

                   sector([-8, -30, -8, -28, -10, -24, -10, -30, ], gb_blue2,
                          gb_cyan, gb_black2, 1200, 3600, "Back and forth"),
                   sector([-8, -35, -8, -30, -10, -30, -10, -35, ], gb_blue2,
                          gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
                   sector([-8, -40, -8, -35, -10, -35, -10, -40, ], gb_blue2,
                          gb_magenta, gb_black2, 1200, 3600, "Back and forth"),
                   sector([-8, -45, -8, -40, -10, -40, -10, -45, ], gb_blue2,
                          gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
                   sector([-8, -50, -8, -45, -10, -45, -10, -50, ], gb_blue2,
                          gb_yellow, gb_black2, 1200, 3600, "Back and forth"),
                   sector([-8, -55, -8, -50, -10, -50, -10, -55, ], gb_blue2,
                          gb_yellow, gb_yellow2, 0, 3600, "Back and forth"),
                   ]

join_sectorlist([bridge_connector6] + hub04_pillars +
                hub04_tsplit + hub04_floor + hub04_slices + hub04_platforms)

# join_sectors(hub04_pillars[0],bridge_connector6)
# join_sectorlist(hub02_pillars+[bridge_connector6])
join_sectorlist(hub02_pillars + [hub_connector1])
#
join_sectors(hub_connector1, hub04_pillars[3])
join_sectors(hub_connector1, hub02_pillars[3])

join_sectors(hub01_platforms[9], hub04_platforms[8])
join_sectors(hub01_platforms[9], hub01_platforms[8])


window_area = sector([
    5,15,
    -5,15,
    -15,8, -10,5, -5,4, 5,4, 10,5, 15,8,], gb_black2, gb_black, gb_black2, 0, 3600, "Split view")
window1 = sector([15, -4, 15, 8, 10, 5, 10, 1,], gb_black2, gb_black, gb_black2, 400, 1200, "Window 1")
window2 = sector([10, 1, 10, 5, 5, 4, 5, 3,], gb_black2, gb_black, gb_black2, 400, 1200, "Window 1")
window3 = sector([5, 3, 5, 4, -5, 4, -5, 3,], gb_black2, gb_black, gb_black2, 400, 1200, "Window 1")
window4 = sector([-5, 3, -5, 4, -10, 5, -10, 1,], gb_black2, gb_black, gb_black2, 400, 1200, "Window 1")
window5 = sector([-10, 1, -10, 5, -15, 8, -15, -4,], gb_black2, gb_black, gb_black2, 400, 1200, "Window 1")
for w in [window1,window2,window3,window4,window5,]:
    w.no_access = True

join_sectorlist([window1,window2,window3,window4,window5,window_area])
join_sectors(window1,hub02_floor[4])
join_sectors(window2,hub03_floor[4])
join_sectors(window3,hub01_floor[4])
join_sectors(window4,hub04_floor[4])
join_sectors(window5,hub01_floor[4])


init_secret6 = sector([
    -3, 7,
    -5, 15, -10, 18, -6, 4,], gb_black2, gb_black, gb_black2, 250, 1600, "?")
init_secret7 = sector([-5, 15, 5, 15, 5, 18, -10, 18,], gb_black2, gb_black, gb_black2, 250, 1600, "?")
join_sectorlist([init_secret5,init_secret6,init_secret7,window_area])



# current_sector = hub03_floor[1]
current_sector = init_sector

# current_sector = window_area
# player_x = -6
# player_y = -1
# player_z = 0
# player_angle = -0.6
# DEBUG = False
