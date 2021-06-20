import turtle
import pandas as pd

# The image path
image = "saudi_image.gif"

screen = turtle.Screen()
screen.title("Saudi Province Game")
# make the image background of the screen
# screen.bgpic(image)
# another way is added to shape then assign the shape
screen.addshape(image)
turtle.shape(image)

# to get the location of the province
# def get_mouse_click_coord(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coord)
# keep the screen open
# turtle.mainloop()

# read the data file
df = pd.read_csv("provinces.csv")
# get the provinces with list format
provinces_list = df["province"].tolist()
# provinces
provinces = []

while len(provinces) < len(df):
    # to save the answer
    answer = screen.textinput(title=f"{len(provinces)}/13 the provinces correct", prompt="Write a province name")
    answer = answer.title()

    if answer == "Exit":
        missing_province = []
        # append not answered province
        for province in provinces_list:
            if province not in provinces:
                missing_province.append(province)

        new_df = pd.DateFrame(missing_province)
        new_df.to_csv("missing_provinces.csv")
        break
    # if the answer in the provinces
    if answer in provinces_list:
        # if the answer is correct
        provinces.append(answer)

        province_name = turtle.Turtle()
        province_name.hideturtle()
        province_name.penup()
        df_row = df[df["province"] == answer]
        province_name.goto(int(df_row["x"]), int(df_row["y"]))
        province_name.write(df_row["province"].item())
