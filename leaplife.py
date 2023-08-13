import lifelib
sess = lifelib.load_rules("b2n3s23-q")
lt = sess.lifetree(n_layers=1)

fixeds = """1 xs4_33 4 block 
1 xs4_252 4 tub 
2 xp2_7 3 blinker 
3 xp3_334oo 8 
4 xp4_31cio 9 
4 xp4_g02196z11 9 
5 xp5_25aszy16ac 13 
6 xp6_77w77 10 interchange
7 xp7_35ekox8ozxog1 17 
8 xp8_356oozy112cc 16 
9 xp9_3520gogy0gog0253 18 
9 xp9_3520gogy0gggzy81w4ac 18 
9 xp9_3520gogy08o8zyb256 18 
10 xp10_lry1rl 12 
11 xp11_32xsx23zo8x7x8o 18 
12 xp12_33y133zxhrhzooy1oo 24 
12 xp12_35uy0u53zokfy0fko 24 
13 xp13_w8o0o5b88gz628ngh7s0vg23zy165 42 
14 xp14_tvuz573 12 
15 xp15_4r4z4r4 12 pentadecathlon
17 xp17_ggw33z11x46j04ggzy531y066zy733 26 
18 xp18_33y833zy072y027z66y866 24 
19 xp19_0p1rszw1465x9f0ccz33 26 
19 xp19_0p1rszw1465x9f033z33 26 
20 xp20_8kkkxkkk8yb270707072zyaee4y04eezx8s0s0s0s8yb2555x5552 66 
22 xp22_y1gka953zo4ic3z11 22 
24 xp24_0g04013hcz38c802 16 
25 xp25_xg8sxey02596z0ghh1z0gz3452 28 
26 xp26_33zx2796zy4256 16 
27 xp27_y2c4oybidrzg88wp444o0408ox6a46ahxhac4acz110201i229w11w8c8y1rm9zy2123zy566wsksxsksw66zy7ooy5oo 112 
28 xp28_33y133z0o42224ozohy1ho 25 
30 xp30_077w77zzvtvz757 23 LCM(6,15)
33 xp33_061i0l1l0i16zy1222z32xsx23zo8x7x8o 38 LCM(3,11)
34 xp34_02eg88m9b8oyco8b9m88ge2zg88c0va239cycc8728r1c88gz011321wiu066xeaey2660uiw12311 109 
36 xp36_xgggw3534739czs4om2lcgszx655 33 LCM(4,9) 
38 xp38_xrb8oyno8brzy1g848yj848gzccx1021dey3277y5ed1201xcc 61 
40 xp40_y5kcwbd0mk4o0o8bi2s0c88gybg88c0s2ib8o0o4km0dbwckzok4ra970v0h9dd1dg507c28o96650pr21y1oy312rp05669o82c705gd1dd9h0v079ar4kozxrais0v0himmgm1k0s6823icck0jr8gx116y3g8rj0kcci3286s0k1mgmmih0v0siarzy556wqm0d543032q98706221yb12260789q230345d0mqw65 392 
42 xp42_77w77zzw391hh193 24 LCM(6,14)
42 xp42_lawalzzw74a66a47 24 LCM(6,14)
42 xp42_391hh193zy5ehhhe 24 LCM(6,14)
42 xp42_suqy2ehhhez7fb 24 LCM(6,14)
42 xp42_ehhhezzx36777763 24 LCM(6,14)
42 xp42_uvty2ehhhez375 24 LCM(6,14)
42 xp42_0ehhhezzv102oz7402 24 LCM(6,14)
42 xp42_qusy2ehhhezbf7 24 LCM(6,14)
44 xp44_y2gci97zg84ka21y5c9450c93z111 35 LCM(4,22)
45 xp45_y42ljzw6a406elrlec04aczy4pl8zvtvz757 48 LCM(9,15)
50 xp50_cc0v168y2goxsy04aiczx11y22321zy6111zy569a4 43 LCM(10,25)
51 xp51_4a447w744a4y0cczy9gsksx66zy1ooxeaf31zy5cc 42 LCM(3,17)
52 xp52_c9374353y18kczy5siczy1oo 29 LCM(4,26)
55 xp55_0swoo3oowszxs11811szoow22822woozx6ehghe6zx7w8w7zy28cmey5emc8zy6rrhxhrrzy226dey5ed62 106 LCM(5,11)
60 xp60_4r4z4r4y1kaezy3c937 25 LCM(4,15)
63 xp63_66y3c53y4ok6y3cc 20 
66 xp66_25522552zggz3496ozy115aiko 32 LCM(6,22)
68 xp68_ecp3y4ccz752y2gsksx66z0ooxeaf31zy1cc 39 LCM(4,17)
72 xp72_s82240gy13520gogy0gog0253zw208gg4e 34 LCM(9,24)
75 xp75_y54r4zy54r4zzy0goxsy04aiczw2321z0111z69a4 40 LCM(15,25)
82 xp82_33xgoy633zy13267wcf932zx4c9f3we6kszccy61y0cc 40 
102 xp102_wehhhey0ggzy711woozy2sgh17z33wggzy011 38 LCM(6,17)"""
cfuncs = ()