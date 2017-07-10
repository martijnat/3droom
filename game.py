all_sectors = []

def octagon(x,y,z,c1=gb_blue2,c2=gb_white,c3=gb_white2,height=1600,desc=""):
    grid_size = 4
    return sector([
        x+2*grid_size,y-1*grid_size,
        x+2*grid_size,y+1*grid_size,
        x+1*grid_size,y+2*grid_size,
        x-1*grid_size,y+2*grid_size,
        x-2*grid_size,y+1*grid_size,
        x-2*grid_size,y-1*grid_size,
        x-1*grid_size,y-2*grid_size,
        x+1*grid_size,y-2*grid_size,],
        c1, c2, c3, z, height, desc)



init_sector = octagon(0,0,0)
init_path1a = octagon(12,12,100,gb_blue2,gb_blue,gb_blue2)
init_path1b = octagon(0,24,200,gb_blue2,gb_green,gb_green2)
init_path1c = octagon(-12,12,100,gb_blue2,gb_yellow,gb_yellow2)

init_path2a = octagon(-12,12,100,gb_blue2,gb_red,gb_red2)
init_path2b = octagon(0,24,200,gb_blue2,gb_yellow,gb_yellow2)
init_path2c = octagon(12,12,100,gb_blue2,gb_green,gb_green2)

new_start = octagon(0,0,0,gb_blue2,gb_black,gb_black2)

join_sectors(init_sector,init_path1a)
join_sectors(init_path1a,init_path1b)
join_sectors(init_path1b,init_path1c)
join_sectors(init_path1c,new_start)
join_sectors(init_sector,init_path2a)
join_sectors(init_path2a,init_path2b)
join_sectors(init_path2b,init_path2c)
join_sectors(init_path2c,new_start)


loop1 = octagon(0,16,100,gb_blue2,gb_black2,gb_white)
loop2 = octagon(16,16,0,gb_blue2,gb_black2,gb_white2)
loop3 = octagon(16,0,100,gb_blue2,gb_black2,gb_white)
loop4 = octagon(0,0,0,gb_blue2,gb_black2,gb_white2)
loop5 = octagon(0,16,100,gb_blue2,gb_black2,gb_white)
loop6 = octagon(16,16,0,gb_blue2,gb_black2,gb_white2)
loop_exit1 = octagon(16,16,0,gb_blue2,gb_black2,gb_white2)
loop_exit2 = octagon(0,16,100,gb_blue2,gb_black2,gb_white)
loop_exit3 = octagon(0,0,0,gb_blue2,gb_black2,gb_white2)
loop_exit4 = octagon(16,0,-200,gb_blue2,gb_black2,gb_white)
loop_exit5 = octagon(16,16,-400,gb_blue2,gb_black2,gb_white2)
loop_finish = octagon(0,16,-400,gb_blue2,gb_magenta,gb_magenta2)
join_sectors(new_start,loop1)
join_sectors(loop1,loop2)
join_sectors(loop2,loop3)
join_sectors(loop3,loop4)
join_sectors(loop4,loop5)
join_sectors(loop5,loop6)
join_oneway(loop6,loop3)
join_oneway(loop_exit1,loop3)
join_oneway(loop3,loop_exit1)
join_sectors(loop_exit1,loop_exit2)
join_sectors(loop_exit2,loop_exit3)
join_sectors(loop_exit3,loop_exit4)
join_sectors(loop_exit4,loop_exit5)
join_sectors(loop_exit5,loop_finish)
join_oneway(loop_finish,new_start)


# jumper1 = sector([
#     -8,20,
#     -4,24,
#     -8,28,
#     -12,24,
# ], gb_blue2, gb_blue, gb_blue2, -300, 1600, "")

jumper1 = sector([
    -8,20,
    -4,24,
    -12,28,
    -12,24,
], gb_blue2, gb_blue, gb_blue2, -300, 1600, "")

jumper2 = sector([
    -12,24,
    -12,28,
    -16,28,
    -16,24,
], gb_blue2, gb_green, gb_green2, -100, 1600, "")

jumper3 = sector([
    -16,24,
    -16,20,
    -12,24,
], gb_blue2, gb_yellow, gb_yellow2, 100, 1600, "")

jumper4 = sector([
    -12,24,
    -16,20,
    -8,20,
], gb_blue2, gb_red, gb_red2, 400, 1600, "")

join_sectors(loop_finish,jumper1)
join_sectorlist([jumper1,jumper2,jumper3,jumper4])


# current_sector = init_sector
current_sector = loop_finish
# Debugging
print(player_x,player_y,player_z)
