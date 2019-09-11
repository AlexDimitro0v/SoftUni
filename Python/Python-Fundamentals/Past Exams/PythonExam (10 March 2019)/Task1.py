from math import pi


def main():
    truck_width = float(input())
    truck_depth = float(input())
    truck_height = float(input())
    barrels = int(input())

    total_truck_volume = truck_width*truck_height*truck_depth
    total_barrels_volume = 0
    for n in range(barrels):
        barrel_radius = float(input())
        barrel_height = float(input())
        barrel_volume = pi*barrel_radius**2*barrel_height
        total_barrels_volume += barrel_volume
        if total_barrels_volume > total_truck_volume:
            print(f"Truck is full. {n} on board!")
            return
    print(f"All barrels on board. Capacity left - {total_truck_volume-total_barrels_volume:.2f}.")


if __name__ == '__main__':
    main()
