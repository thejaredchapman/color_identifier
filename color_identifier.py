import colorgram

img = "Alabama-Sweet-Tea-Party.jpg"

colors = colorgram.extract(img, 10)
# arguments are the image then how many colors received back in a tuple
# change both to receive what is needed. 

img
print(colors)