from math import pi
def main():
    temp_list = []
    radii = []
    heights = []
    names = []
    costs = []
    with open("canlist.txt") as objects:
        for data in objects:
            cleaned_data = data.strip()
            temp_list = cleaned_data.split(",")
            names.append(temp_list[0])
            radii.append(float(temp_list[1]))
            heights.append(float(temp_list[2]))
            costs.append(temp_list[3])
            temp_list.clear
        for i in range(len(names)):
            volume  = calculate_volume(radii[i], heights[i])
            surface_area = calculate_surface_area(radii[i], heights[i])
            storage_efficiency = calculate_storage_efficiency(volume, surface_area)
            print(f"{names[i]}'s storage efficiency is: {storage_efficiency:.2f}")
def calculate_volume(radius, height): 
    volume = pi * (radius ** 2) *height
    return volume

def calculate_surface_area(radius, height):
    surface_area = 2 * pi * radius * (radius + height)
    return surface_area

def calculate_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return  storage_efficiency

main()