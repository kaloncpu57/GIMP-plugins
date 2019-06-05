from gimpfu import *

def plugin_main(image, drawable):
    rainbowlayer = gimp.Layer(image, "Rainbow", image.width*2, image.height*2, 1, 100, 0)
    image.add_layer(rainbowlayer)
    rainbowlayer.translate(-(rainbowlayer.width / 2), 0)
    gimp.context_set_gradient('Full saturation spectrum CW')
    pdb.gimp_edit_blend(rainbowlayer, 3, 0, 0, 33.3, 0, 1, FALSE, FALSE, 1, 0, TRUE, rainbowlayer.width, 0, rainbowlayer.width / 2, image.height)
    slashindex = pdb.gimp_image_get_filename(image).rfind('\\')
    savepath = pdb.gimp_image_get_filename(image)[:slashindex+1]
    newgif = gimp.Image(image.width, image.height, RGB)
    gifframes = []
    xmovement = image.width / 24
    ymovement = -(image.height / 24)
    average = (image.width + image.height) / 2
    totalframes = average / (average / 24)
    for i in range(totalframes):
        framename = "%sframe%s.png" % (savepath, i+1)
        new_image = pdb.gimp_image_duplicate(image)
        savelayer = pdb.gimp_image_merge_visible_layers(new_image, CLIP_TO_IMAGE)
        pdb.gimp_file_save(new_image, savelayer, framename, '?')
        rainbowlayer.translate(xmovement, ymovement)
        gifframes.append(pdb.gimp_file_load_layer(newgif, framename))
    for i in reversed(gifframes):
        newgif.add_layer(i)
    gimp.Display(newgif)

register(
    "python_fu_rainbowgif",
    "Creates all frames for a gif with a sliding rainbow filter",
    "Export as a gif from the new window",
    "kaloncpu57",
    "kaloncpu57",
    "2019",
    "<Image>/Rainbow/Rainbow",
    "RGB*, GRAY*",
    [],
    [],
    plugin_main)

main()
