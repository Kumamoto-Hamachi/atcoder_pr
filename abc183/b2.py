def accept_one_num_row():
    num_list = list(map(int, input().strip().split()))
    return num_list

def accept_one_num_map_row():
    num_map = map(int, input().strip().split())
    return num_map

if __name__ == "__main__":
    """
    num_list = accept_one_num_row()
    sx, sy, gx, gy = num_list
    # ans = (gx*sy - sx*sy) / (gy + sy) + sx
    ans = (gx * sy + gy * sx) / (gy + sy)
    print(ans)
    """
    sx, sy, gx, gy = accept_one_num_map_row()
    rate = (-gy - sy) / (gx - sx)
    point = -sy / rate
    ans = point + sx
    print(ans)
