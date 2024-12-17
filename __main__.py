import os
import shutil
import sys

data_file = sys.argv[1]

print(data_file)

shutil.copy("./data/"+data_file, "./src/main/data.py")

shutil.copy("./params.py", "./src/main/params.py")

res = int(input("1 - to plot data , 2 - get estimate\ninput: "))

if res == 2:
    import src.main.__main__
elif res == 1:
    import src.main.plotter
    plot_name = os.path.splitext(data_file)[0]+".png"
    shutil.move("./results/images/result.png", "./results/images/"+plot_name)
else :
    print("wrong input: retry")
