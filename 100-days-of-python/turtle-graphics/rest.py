from turtle import Turtle, Screen

# screen = Screen()
# tim = Turtle()

# tim.shape("turtle")
# tim.fillcolor("red")
#
#
# def draw_square(radius):
#     tim.ht()
#     tim.penup()
#     tim.speed(0)
#     tim.setpos(radius / 2, radius / 2)
#     tim.pendown()
#     tim.st()
#     tim.speed(3)
#     for _ in range(4):
#         tim.right(90)
#         tim.fd(radius)
#
#
# def draw_dashed_line(meter):
#     for _ in range(15):
#         tim.forward(meter)
#         tim.penup()
#         tim.forward(meter)
#         tim.pendown()
#
#
# def draw_polygon():
#     side_of_polygon = 3
#     while side_of_polygon <= 10:
#         for _ in range(side_of_polygon):
#             tim.forward(100)
#             tim.right(360 / side_of_polygon)
#         side_of_polygon += 1


result = [
    "AliceBlue\nAntiqueWhite\nAntiqueWhite1\nAntiqueWhite2\nAntiqueWhite3\nAntiqueWhite4\naquamarine\naquamarine1\naquamarine2\naquamarine3\naquamarine4\nazure\n\nazure 1\n\nazure2\n\nazure3\n\nazure4\n\nbeige\n\nbisque\n\nbisque1\nbisque2\n\nbisque3\nbisque4\nblack\nBlanchedAlmond\nblue\n\nblue\n\nblue2\nblue3\nblue4\nBlueViolet\nbrown\nbrown1\nbrown2\nbrown3\nbrown4\nburlywood\nburlywood1\nburlywood2\nburlywood3\nburlywood4\n\nCadetBlue\nCadetBlue1\nCadetBlue2\nCadetBlue3\nCadetBlue4\nchartreuse\nchartreuse\nchartreuse2\nchartreuse3\nchartreuse4\nchocolate\nchocolate1\nchocolate2\nchocolate3\nchocolate4\ncoral\n\ncoral1\ncoral2\ncoral3\n\ncoral4\n\nPython Turtle Graphics\n\nCornflowerBlue\ncornsilk\ncornsilk1\ncornsilk2\ncornsilk3\ncornsilk4\n\ncyan\n\ncyan1\n\ncyan2\n\ncyan3\n\ncyan4\nDarkBlue\nDarkCyan\nDarkGoldenrod\n\nDarkGoldenrod1\nDarkGoldenrod2\nDarkGoldenrod3\nDarkGoldenrod4\n\nDarkGray\n\nDarkGreen\n\nDarkGrey\nDarkKhaki\nDarkMagenta\nDarkOliveGreen\nDarkOliveGreen1\nDarkOliveGreen2\nDarkOliveGreen3\nDarkOliveGreen4|\nDarkOrange\nDarkOrange'1\nDarkOrange2\nDarkOrange3\nDarkOrange4\nDarkOrchid\nDarkOrchid1\nDarkOrchid2\nDarkOrchid3\nDarkOrchid4\nDarkRed\n\nDarkSalmon\n\nDarkSeaGreen\nDarkSeaGreen1\nDarkSeaGreen2\nDarkSeaGreen3\nDarkSeaGreen4\nDarkSlateBlue\nDarkSlateGray\nDarkSlateGray1\nDarkSlateGray2\nDarkSlateGray3\nDarkSlateGray4\nDarkSlateGrey\nDarkTurquoise\nDarkViolet\nDeepPink\nDeepPink1\nDeepPink2\nDeepPink3\nDeepPink4\nDeepSkyBlue\n\n>\n\n",
    'Python Turtle Graphics\n\nDeepSkyBlue2 gold1 gray100 IndianRed1 LavenderBlush4 LightGoldenrod »\nDeepSkyBlue3 gold2 green IndianRed2 lawngreen LightGoldenrod1\nDeepSkyBlue4 gold3 green1 IndianRed3 LawnGreen LightGoldenrod2\nDimGray gold4 green2 IndianRed4 lemonchiffon LightGoldenrod3\nDimGrey goldenrod green3 ivory LemonChiffon LightGoldenrod4\nDodgerBlue goldenrod1 green4 ivory1 LemonChiffon1 LightGoldenrodYellow\nDodgerBlue1 goldenrod2 GreenYellow ivory2 LemonChiffon2 LightGray\nDodgerBlue2 goldenrod3 honeydew ivory3 LemonChiffon3 LightGreen\nDodgerBlue3 goldenrod4 honeydew1 ivory4 LemonChiffon4 LightGrey\nDodgerBlue4 gray honeydew2 khaki LightBlue LightPink\n\nfirebrick grayO honeydew3 khaki1 LightBlue1 LightPink1\n\nfirebrick1 gray10 honeydew4 khaki2 LightBlue2 LightPink2\n\nfirebrick2 gray20 hotpink khaki3 LightBlue3 LightPink3\nfirebrick3 gray30 HotPink khaki4 LightBlue4 LightPink4\nfirebrick4 gray40 HotPink1 lavender LightCoral LightSalmon\nFloralWhite gray50 HotPink2 lavenderblush LightCyan LightSalmon1\nForestGreen gray60 HotPink3 LavenderBlush LightCyan1 LightSalmon2\ngainsboro gray70 HotPink4 LavenderBlush1 LightCyan2 LightSalmon3\nGhostWhite gray80 indianred LavenderBlush2 LightCyan3 LightSalmon4\n\ngold gray90 IndianRed LavenderBlush3 LightCyan4 LightSeaGreen\n\n',
    'LightSkyBlue\nLightSkyBlue1\nLightSkyBlue2\nLightSkyBlue3\nLightSkyBlue4\nLightSlateBlue\nLightSlateGray\nLightSlateGrey\nLightSteelBlue\nLightStee!lBlue1\nLightSteeIBlue2\nLightSteeIBlue3\nLightSteelBlue4\nLightYellow\nLightYellow1\nLightY ellow2\nLightY ellow3\nLightY ellow4\nLimeGreen\n\nlinen\n\nmagenta\nmagenta‘\nmagenta2\nmagenta3\nmagenta4\nmaroon\nmaroon1\nmaroon2\nmaroon3\n\nmaroon4\n\nMediumAquamar\n\nMediumBlue\nMediumOrchid\nMediumOrchid 1\nMediumOrchid2\nMediumOrchid3\nMedium Orchid4\nMediumPurple\nMediumPurple1\nMediumPurple2\n\nMediumPurple3\nMediumPurple4\n\nMediumSeaGree\n\nMediumSlateBlu\n\nMediumSpringGr\n\nMediumTurquois\nMediumVioletRe\nmidnightblue\nMidnightBlue\nMintCream\nMistyRose\nMistyRose1\nMistyRose2\nMistyRose3\nMistyRose4\nmoccasin\nNavajoWhite\nNavajoWhite1\nNavajoWhite2\nNavajoWhite3\n\nPython Turtle Graphics\n\nNavajoWhite4\n\nnavy\nNavyBlue\nOldLace\nOliveDrab\nOliveDrab1\nOliveDrab2\nOliveDrab3\nOliveDrab4\norange\norange1\norange2\norange3\norange4\nOrangeRed\nOrangeRed1\nOrangeRed2\nOrangeRed3\nOrangeRed4\n\norchid\n\norchid1\n\norchid2\n\norchid3\n\norchid4\nPaleGoldenrod\nPaleGreen\nPaleGreen1\nPaleGreen2\nPaleGreen3\nPaleGreen4\nPaleTurquoise\nPaleTurquoise1\nPaleTurquoise2\nPaleTurquoise3\nPaleTurquoise4\nPaleVioletRed\nPaleVioletRed1\nPaleVioletRed2\nPaleVioletRed3\nPaleVioletRed4\n\nPapayaWhip >\nPeachPuff\nPeachPuff1\nPeachPuff2\nPeachPuff3\nPeachPuff4\nperu\n\npink\n\npink1\n\npink2\n\npink3\n\npink4\n\nplum\n\nplum1\nplum2\nplum3\nplum4\nPowderBlue\npurple\npurple1\n\n',
    'purple2\npurple3\npurple4\n\nred\n\nred1\n\nred2\n\nred3\n\nred4\nRosyBrown\nRosyBrown1\nRosyBrown2\nRosyBrown3\nRosyBrown4\nRoyalBlue\nRoyalBlue1\nRoyalBlue2\nRoyalBlue3\nRoyalBlue4\nSaddleBrown\n\nsalmon\n\nsalmon‘\nsalmon2\nsalmon3\nsalmon4\nSandyBrown\nSeaGreen\nSeaGreen1\nSeaGreen2\nSeaGreen3\nSeaGreen4\nseashell\nseashell\nseashell2\nseashell3\nseashell4\nsienna\nsienna‘\nsienna2\nsienna3\n\nsienna4\n\nSkyBlue\nSkyBlue1\nSkyBlue2\nSkyBlue3\nSkyBlue4\nSlateBlue\nSlateBlue 1\nSlateBlue2\nSlateBlue3\nSlateBlue4\nSlateGray\nSlateGray1\nSlateGray2\nSlateGray3\nSlateGray4\nSlateGrey\nsnow\nsnow1\nsnow2\n\nsnow3\n\nPython Turtle Graphics\n\nsnow4\nSpringGreen\nSpringGreen1\nSpringGreen2\nSpringGreen3\nSpringGreen4\nSteelBlue\nSteelBlue1\nSteelBlue2\nSteelBlue3\nSteelBlue4\ntan\n\ntan1\n\ntan2\n\ntan3\n\ntan4\n\nthistle\n\nthistle1\nthistle2\nthistle3\n\nthistle4\ntomato\ntomato1\ntomato2\ntomato3\ntomato4\nturquoise\nturquoise1\nturquoise2\nturquoise3\nturquoise4\nviolet\nVioletRed\nVioletRed1\nVioletRed2\nVioletRed3\nVioletRed4\nwheat\nwheat\n\nwheat2\n\nwheat3\nwheat4\nwhite\nWhiteSmoke\nyellow\nyellow1\nyellow2\nyellow3\nyellow4\n\nYellowGreen\n\n']
