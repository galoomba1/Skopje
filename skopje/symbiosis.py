import lifelib
sess = lifelib.load_rules("xsymbiosis")
lt = sess.lifetree()

fixeds = """1 xs2_1_2 2
2 xp2_7 3
3 xp3_f_g 5
4 xp4_ic_1z1 6
5 xp5_ci_1z1 6
6 xp6_s1_w1z1 6
7 xp7_usz1_1z2 7
8 xp8_acs_1zw1 7
9 xp9_02b7_28 7
10 xp10_61e_1 7
11 xp11_02s_21z01 7
12 xp12_22go_1zx1 7
13 xp13_oez1_018z02 9
14 xp14_02208c_410g 8
15 xp15_02b4_4g 7
16 xp16_2og_01z1 6
17 xp17_043h_8hzw1 9
18 xp18_ka4_w12z1 8
19 xp19_9312_g04 8
20 xp20_iem_1z01 8
21 xp21_028s_1zw1 7
22 xp22_028e_4g1 7
23 xp23_2g0cc_1y0gz1 8
24 xp24_030186_2y14 8
25 xp25_2cq8_1w2o 10
26 xp26_2k6_g1 7
27 xp27_05126z01_5g 8
28 xp28_0224c_14xg 8
29 xp29_012413_2w8w1 9
30 xp30_01ee_og 9
31 xp31_01j84zg_x18z0g 10
32 xp32_03104_2xgo 8
33 xp33_0g66z2_w1z401 9
34 xp34_2gozwg_1wgz08 8
35 xp35_gx6208_y01x8z1 8
36 xp36_0d1i_izw1 9
37 xp37_2oo_1wk 8
38 xp38_024e_18g 8
39 xp39_g09c_x18z1 8
40 xp40_21w6571_14w8x1 12
41 xp41_0gqw8_w1x4z1 8
42 xp42_03ho_1xg 8
43 xp43_0i974_1y04z1 9
44 xp44_cquz02_01z1 11
45 xp45_0222484_201w2 9
46 xp46_2y22io_4y2102g 10
47 xp47_ja7_c 9
48 xp48_6kz02_018z2 8
49 xp49_waoz4_x1z2x1 8
50 xp50_09glfw2_9y16 12
51 xp51_0gk2zy32_w1z1y21 8
52 xp52_620fx8_10gy166 13
53 xp53_2wgqb_1y04g 11
54 xp54_630go48_1y0g 11
55 xp55_079czw1_1g 10
56 xp56_031b6x4_4xgy026 11
57 xp57_02r9_1x9 10
58 xp58_371w8a_4y21 11
59 xp59_3v15_8x2 9
60 xp60_0139y28_140ggy04 11
61 xp61_27az2_x4z1 9
62 xp62_02jr_1zw1 9
63 xp63_4a97_h 10
64 xp64_1318_40g 7
65 xp65_01b4zy81_1gy5g 9
66 xp66_01a4x8_1gy04 8
67 xp67_0lvz31_x9z4021 15
68 xp68_02sozg_w10oz8 11
69 xp69_08xge6w1zx4_8y3802zw2x1 13
70 xp70_xg88m8z041_y04w16za1 16
71 xp71_01z08y2801zx2314_w1z4y2801zw4x84 15
72 xp72_qf1_w82z1 10
73 xp73_4x6phm08_8y38 14
74 xp74_02bja4_1y0g4 10
75 xp75_04w6g8n_4w1zy21 10
76 xp76_010g8gz4ehrgfy18zx1zy8okc_2g84zy23xg 30
77 xp77_044172c_4w8wg4 13
78 xp78_y18048sicz1_y1402w1z2 13
79 xp79_gs6kz01z41_w10az2z3 14
80 xp80_3a17y14_4y34 10
81 xp81_02y0648gzy2gg843z01y01_2y21248zy5g81z1y221 25
82 xp82_08026z040gox1_401z8y21zw1 14
83 xp83_02344s4_1408g 13
84 xp84_ohgzb0iz01_160gz0k 16
85 xp85_18ogs2ux1_2hy1gx1 15
86 xp86_08zy06d132_8y633zy1gx2 14
87 xp87_1c22ey64_g1ggy64 12
88 xp88_3b180e_40g0g 13
89 xp89_3a7zy644_4zy58w2 12
90 xp90_0imz411_81z2 10
91 xp91_g1z178ge4_02z2gxg8 16
92 xp92_0212gozwg_1x10gzw8 11
93 xp93_0106aicy5g_108gy78zy11 15
94 xp94_0cdw5zx1_2w1w2zw2 12
95 xp95_0315963_208x41 15
96 xp96_0o46z63_k21z8 13
97 xp97_0351e4_408wg2 13
98 xp98_0gy2108z0348_gy220gz08g 12
99 xp99_020ksg8y28_1y04y48 12
100 xp100_0g865zz2y62_08x2zz4y64 12
101 xp101_060oo273y02_21gxokx1zx1 21
102 xp102_01e16c4_24wgw4 13
103 xp103_wdiszg28j_05gz8g1zx1 20
104 xp104_02so_1x4c 9
105 xp105_0g0ks81_gx22zzx8k8 14
106 xp106_029qwgz02zx8_2x2wgz2zxg 14
107 xp107_0igz8m5_014zg085z1 16
108 xp108_4y3q8gz26y29_8y31w8zogy1802 17
109 xp109_02phby24_2y08y18zx1 14
110 xp110_4g0s9zz01_802w2zz1 12
111 xp111_010os21364_20gx4w12 17
112 xp112_1zw8xiv16_01z08y2g02 14
113 xp113_a0ehvh_hw4 17
114 xp114_08sir204z0c_421x58 18
115 xp115_0gx401z025wgy48_g8x8w2z08y78zy21 15
116 xp116_0g8mey82z801zy98_04x1y74z082zy84 17
117 xp117_w8w1zgy25d4_x842xgz0gy44cz01 17
118 xp118_4253123w48_2x4x880g 17
119 xp119_0g8mez801yl33_g4x1z082 17
120 xp120_0dczw1yagzy32_821z02yb8zy31 14
121 xp121_080i64z021_0gdx2z2 14
122 xp122_1g8yf4zw137_g14ye4z02x8 14
123 xp123_03192w31_1wgx4 12
124 xp124_06208zx1a6y1g_4w104zx40gy08 16
125 xp125_4agxka4zy02_hy3g4z01w4w1 17
126 xp126_y0ihz9d9t1zw103_wgg421zigzx24 27
128 xp128_04ug2gszw1x1y14_4g10102gz01y58 21
129 xp129_2okex4_4x1x8 10
130 xp130_y42z08k17y81z4_y1gw1z02yb2z041 15
131 xp131_0gy966zx24ey2cc_gya104zw480gy2g08 22
132 xp132_om26cko_21x248z1 19
133 xp133_22z0hqek201zy266_41zxgw5zy12 20
134 xp134_1f0349430f1_g048gw840g 23
136 xp136_0134468zzyb1_14w80gzyag 13
137 xp137_0dcz1_1w4z02 9
138 xp138_0g0og2z4qr7_gx41z840g 19
140 xp140_0gp0eo08x4zw232_8042wcx8 21
141 xp141_02uaz0a_09z50g 14
142 xp142_01ozx131_14y0oo 13
143 xp143_y91z08n1o1f_y81zg3y0g2zx1 19
144 xp144_0gacg04x4zw7rpp_04x8y08x33z18zw1 24
145 xp145_4ogx2zy61_2w8w1xgzzyaoo 14
146 xp146_y666zwagz030rpzx4_y521zx5z10czx2 24
147 xp147_y284qa64zz13ybcc_y142w1w2zz04 22
148 xp148_c60246zyb1_2w1w9zya1 14
149 xp149_0g846z1348oya1_8421z48gyb1zx1 22
150 xp150_y262cz0ly31z01_gy11w4zay51zw2 17
151 xp151_y85z0gu2wuzw101_y92zg6y14zw20201 22
152 xp152_0884676488zz2y52zy0cic_8021x1208zz02y32zzy11 27
153 xp153_4y3q8gz26y29_8y31w8z8y2802 15
156 xp156_g0cguzw8y233zzyq2zyof1601_82w1z0gzzyr1zyogw82 27
158 xp158_0249he4y31_48gxg8y11 15
159 xp159_8021bezx2y1204_3h0gzx4y2a 17
162 xp162_y0iis1zym1z804czw1_xdx2zyl1z48gzx1 23
164 xp164_y1g842248gzy01y41z4yc4_xg84201w248gzz8yc8 23
165 xp165_324aic4_48gxg8 16
166 xp166_058gzxv96z0a1_10248gzy1g2z80421 25
167 xp167_20gy4g02zx126aa621_1y81z012480gw8421 25
169 xp169_1w206aacw4_2x2y028 14
170 xp170_03pmzx13yc31_4gzy04yd4 16
171 xp171_x8gaggsy166z0136_gx401wiz248 24
173 xp173_6bj_1zw1 10
176 xp176_0o42s8z074zy766_42w124z9zy7802 25
177 xp177_08n1s1f_82y0g2zw101 20
180 xp180_x8658gz201xg065zx1_w4x248gz05y1ow4zw2 26
182 xp182_4y61zx12646_04y42zw24x8 13
183 xp183_0gyc24ckozy88xg0j_gyd1w20gzy7408zyb10101 21
184 xp184_ok2w4z010jy04wgz04y124_01y02z1y4sa4ozw3y04 29
185 xp185_02zxsy84zzxgw4a533_104zyb2zy7gzx8040g08 22
186 xp186_4w1y258ai48w4_8w2y1106x408 19
187 xp187_0g846y74z1348o_8421y78z48gzx1 22
190 xp190_0o8e1w6iszw4y31cc_841w101w4z0204y310k 28
191 xp191_1w2skc22y1gzggg_021y09y1g 19
193 xp193_0o42s8z074_42w124z9 18
194 xp194_g088ca2kzxc041_8402w10izxg8w2 22
198 xp198_0cirqcz9876_gzi1 19
200 xp200_0g865zz2y2g_08x2zz4y28 12
202 xp202_0g042d2y22zx24f_g021x1y04zw480g 20
203 xp203_648085_8g0gw5 12
204 xp204_1y6ggwgy61zy64f0817_01yj1zy5410gw81 22
209 xp209_1ydk8gggzyep9gpmfz8yd21_02yd248zyk6z04yd421 32
210 xp210_0208g853_10gxg84 13
212 xp212_0oaq6yk1z4_041yn1z04 13
215 xp215_o8429248oz4_421x124z2 20
217 xp217_y180s272s08z09yb9zzy51_y08021x1208z9yd9zy5g 26
218 xp218_y22zz0401y1gmczw4x8_y21zwgz4y61z08x4w1 18
219 xp219_0auy4sz011zz0lvy4e_81z02z0gz4z01 28
220 xp220_040419b033w2_6020gg04cw2 22
222 xp222_y06532y7gz1gy28zy21_x8y01y7gz02y3gz1y12 18
224 xp224_6lh6sy04zx1_g8x2x88 19
228 xp228_046073cy4c37064_4w8wg4y24gw8w4 26
231 xp231_031313y631313_2w4w2y42w4w2 22
232 xp232_08xsu48gz08xvvj873zy21_8y21248z8y4g81zy321 29
234 xp234_4auzx28_gw1z014w8 14
237 xp237_0oc463gzy11zw1_8421zwgx21 18
238 xp238_0g86z134oy71zy18w8_8401z48y81zx10gwg 22
241 xp241_4c1zil42z01_0hkzx82z021 20
242 xp242_01zy033z20gz01238y88_w2zz028z14xgy74y166 24
243 xp243_01y7ogzyb1iczy9621z01_1y948gzyd14zya8421z1 25
245 xp245_w8ed8gz01xi045zw1_04x248gz1y1ow4z02 26
246 xp246_01c8gzy0g96z0831_1w248gzy2g2z8w421 25
248 xp248_4y2253xc4gzyb21gzykgzy3g_8y72x8zyb4g1zzy48ya1 23
249 xp249_0abg62xgy04_c0g0804w8x4 18
251 xp251_0p1684zw3y7ggzy08y61_px102zx4zx40gy52 23
253 xp253_0g8kc801z1348_84y12z48g 19
255 xp255_0ok48acylcczy28g0gzzyb31_g02w1zy18zy41zyc4 26
256 xp256_8y528zgz08kozx12y82_0gy31048z0gz802z01x4y71 21
258 xp258_g80ccw2z1azyc4_cx2x1zkzyb2 18
263 xp263_wg144z05w13x4_081w2kz2y32 17
265 xp265_042033z01x4y02_21y01z2y02x1 15
268 xp268_2yc2zy0124ckkc421_1yc1zx248gy0g842zy41 25
269 xp269_gs21e4z1z01_81x12z0g 16
275 xp275_gy11zy33d4cwgz1x8zy42_8y120gzy62x8z01w4zy51 22
277 xp277_0at1ezzy369a4_1y08 17
279 xp279_wg04kpx28gz1011_08x2x1w8z2 18
284 xp284_gi6tz1x8_8w2zxo 15
285 xp285_01z08y2ma242_1z8y4g01 14
288 xp288_0p1684zw3yi1zy08y65zya4_px102yegzx4zx40gy52zyb4 26
290 xp290_14iqg44_2x1084 11
291 xp291_01y0610f7_12x280gwa 16
295 xp295_0g8meyng02z801yned21_g4x1ym82z082ymgx41 28
303 xp303_0mcz02y18s2zy211_801z5y4g2zy22 20
304 xp304_21252k2zx49ny110c_04x11xgzw8hy5izy01 27
305 xp305_04y3648gz0gy3gg843zy51_4y51248zgy7g81zy621 25
311 xp311_0g86201z124pgy38zwg_842x2z48gy48zxg 24
319 xp319_wgosqqsogz01y41z2y62_g84201w248gzz4y64 25
341 xp341_0g862y22z124pgzy21_842y45z48gxg 23
349 xp349_8g2252wkxg_g01x1w8zy71 15
350 xp350_y0gy31y7gz8k6xe48zzx1_y08y41z21y1128y91z1zx2 24
356 xp356_gx8c21ac8zyd2zy92_0gw21x124zyc2zy91 20
385 xp385_0ggw1x2z343y1802zzxg_x8w2x1z8y4g02zzzx1 19
387 xp387_zxgz0258vy5252_33z0g8y8gz08gy88zx1 25
388 xp388_8k6xmt2zw1221_21y282z1204w21 24
389 xp389_0g0ca4w1zyc8zz04_w2010402z1ybgzzw4 16
398 xp398_2x125boob521x2_1w248gy0g842w1zy41 25
408 xp408_02yg1zyj8z0g8gzx352w8_w2ye2zyi4z8zw4080204 20
420 xp420_0g04612zx26ay24_g021x1zw480gy1208 21
424 xp424_0oaq6yl2z4_041ym2z04 13
437 xp437_0g86601yc4z134ogy38zy08g_842x2yb8z48gy48zy0g 28
446 xp446_06608zy0axhzyc2_4w104zx4gzy51y11 17
456 xp456_2x253zzzybange_4zzzyagy02 19
473 xp473_go26y32zx570101_8y521zw28w21 20
494 xp494_2y54ehne8a4zya1_1yb1g4zy92 21
614 xp614_whw1y2oozw4woc2dz4yc1_082x2y34z04y1g02y3gz04y01 25
681 xp681_0g04212y0gzx24e_g021x1y0gzw480g 18
781 xp781_y62zyhgz0ooz2zy08zy01x4ige1_y61zzw4yd1z12zxkzx2y481zy51 27
829 xp829_1o6hl6acw1zx111_21y1gx2z01x2 21
921 xp921_4xkwg8ccw42w2zy32x8_22w8y24a0401zy21x4 23
1302 xp1302_0ky4g2zw26454553_62y513z148w88w841 28"""

m0small_1 = lt.pattern("11.A$11.B$7.A$6.B2A$AB2$6.A$2.2A2.A.A$2.2A2.2A$3.B")
m0small_2 = lt.pattern("8.B$8.2A$8.2A3$10.BA$3.2AB$3.2A$B$A")(4,6)

m0_1 = lt.pattern("13.2B$2B9.2A.B$B10.2A$.2A$.2A")
m0_2 = lt.pattern("12.A$12.A$12.2A2$13.A$2.2A10.B$B.2A9.2B$2B")(1,8)

m1_1 = lt.pattern("12.A$12.B$8.A$7.B2A2$AB$7.A$7.A.A$2.2A3.2A$2.2A$3.B")
m1_2 = lt.pattern("9.2A$9.2AB3$8.A$8.B$3.2AB$3.2A$B$A")(5,8)

m2_1 = lt.pattern("2.2B$2.B$3.2A$B3.A$.3A2$.B$2.AB")
m2_2 = lt.pattern("BA$2.B2$2.A$2A.B$A$.B$2B")(16,1)

m3_1 = lt.pattern("13.A$13.B$9.2A$8.B2A3$3.B$3.A3$B2A$.2A")
m3_2 = lt.pattern("9.A$9.A$9.2A2$10.A$11.B$10.2B$3.2AB$3.2A$B$A")(4,9)

m4_1 = lt.pattern("13.A$13.B$9.2A$8.B2A3$3.B$3.A3$B2A$.2A")
m4_2 = lt.pattern("10.A$10.A$10.2A2$11.A$12.B$BA9.2B$4.2A$4.2A$4.B")(3,9)

m4large_1 = lt.pattern("3.B$4.A$4.2A5.A$10.A$10.3A11$.2A$.2A$B")
m4large_2 = lt.pattern("5.B$3.2A$3.2A13$2A$2A$2.B")(15,3)

m5_1 = lt.pattern("10.B$9.2A$9.2A$13.AB2$3.B$3.A3$B2A$.2A")
m5_2 = lt.pattern("10.A$10.A$10.2A2$11.A$12.B$BA9.2B$4.2A$4.2A$4.B")(4,9)

m6_1 = lt.pattern("8.B$7.2A$7.2A$2B9.AB$B$.2A$.2A")
m6_2 = lt.pattern("10.A$10.A$10.2A2$11.A$12.B$BA9.2B$4.2A$4.2A$4.B")(2,9)

m7_1 = lt.pattern("13.2B$2B9.2A.B$B10.2A$.2A$.2A")
m7_2 = lt.pattern("10.A$10.A$10.2A2$11.A$12.B$BA9.2B$4.2A$4.2A$4.B")(3,8)

def universal_reflector_loop(p):
    n, r = divmod(p, 8)
    if r == 0:
        if p < 56:
            return None
        elif p < 144:
            return (m0small_1 + m0small_2(n-7,n-7), 32)
        return (m0_1 + m0_2(n-18,n-18), 29)
    elif r == 1:
        if p < 65:
            return None
        return (m1_1 + m1_2(n-8,n-8), 32)
    elif r == 2:
        # there's a p18+8n shuttle akin to Elkies's Life reflector,
        # but it's always beaten by fixed oscillators before p106
        if p < 106:
            return None
        return (m2_1 + m2_2(n-13,n-13), 24)
    elif r == 3:
        if p < 91:
            return None
        return (m3_1 + m3_2(n-11,n-11), 29)
    elif r == 4:
        if p < 84:
            return None
        elif p < 308:
            return (m4_1 + m4_2(n-10,n-10), 29)
        return (m4large_1 + m4large_2(n-38,n-38), 24)
    elif r == 5:
        if p < 85:
            return None
        return (m5_1 + m5_2(n-10,n-10), 29)
    elif r == 6:
        if p < 102:
            return None
        return (m6_1 + m6_2(n-12,n-12), 29)
    else:
        if p < 127:
            return None
        return (m7_1 + m7_2(n-15,n-15), 29)

cfuncs = (universal_reflector_loop,)
