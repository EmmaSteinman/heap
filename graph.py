import matplotlib.pyplot as pyplot


def plot():
	heapTime = [1e-06,0.000355,0.000866,0.001276,0.00182,0.002042,0.002556,0.003021,0.003464,0.003602,0.004125,0.004257,0.004582,0.004538,0.004993,0.004953,0.005328,0.005429,0.005648,0.005576,0.005884,0.005858,0.006058,0.006113,0.006405,0.006358,0.006485,0.006545,0.006535,0.006658,0.006672,0.006686,0.006838,0.006751,0.006848,0.006925,0.00686,0.00695,0.007024,0.007004,0.007042,0.007086,0.00705,0.007121,0.00714,0.007115,0.007175,0.007267,0.008196,0.007235,0.007266,0.007258,0.007243,0.007355,0.007485,0.007667,0.007887,0.008035,0.008116,0.008299,0.008419,0.008613,0.008736,0.008901,0.009059,0.00921,0.009375,0.009581,0.00977,0.009873,0.010016,0.010151,0.010331,0.010461,0.010759,0.010781,0.010962,0.011136,0.011362,0.012006,0.011603,0.011774,0.011904,0.012069,0.012266,0.012382,0.012569,0.012748,0.0129,0.013066,0.013312,0.013408,0.013632,0.013742,0.01397,0.014222,0.014283,0.014414,0.014631,0.01478,0.014967,0.015049,0.015325,0.01537,0.015623,0.015732,0.015859,0.016054,0.016208,0.016348,0.016561,0.016716,0.016955,0.017076,0.017222,0.017543,0.017676,0.017827,0.017957,0.018268,0.01825,0.01841,0.018574,0.018705,0.018851,0.019152,0.01927,0.01945,0.019604,0.019726,0.019877,0.020055,0.020238,0.020562,0.020598,0.020952,0.020934,0.021265,0.021336,0.021634,0.02437,0.021946,0.022021,0.022376,0.022357,0.022706,0.02272,0.02301,0.023042,0.023161,0.023389,0.023514,0.023726,0.023872,0.024101,0.024216,0.024509,0.024661,0.024751,0.024915,0.02513,0.02546,0.025518,0.025701,0.025833,0.02616,0.026173,0.026445,0.026579,0.026754,0.026929,0.027113,0.027287,0.027411,0.027565,0.027868,0.028061,0.028132,0.028419,0.028513,0.028802,0.029,0.029141,0.029321,0.029483,0.029683,0.029852,0.029979,0.030215,0.030386,0.030656,0.030657,0.031079,0.031075,0.031175,0.031338,0.031536,0.03186,0.031932,0.032583,0.032331,0.032499,0.032675,0.0329,0.032974,0.033261,0.033345,0.03382,0.033816,0.034061,0.034086,0.034347,0.034497,0.034615,0.034768,0.034997,0.035141,0.035434,0.035694,0.035984,0.035968,0.036295,0.036351,0.036679,0.036853,0.037027,0.037145,0.037418,0.037515,0.037931,0.037744,0.038303,0.038352,0.038823,0.038589,0.038686,0.038873,0.039202,0.039217,0.039431,0.03963,0.039842,0.040077,0.040126,0.04034,0.040578,0.040701,0.040952,0.041263,0.041241,0.041554,0.041785,0.041834,0.04205,0.04225,0.042411,0.042559,0.042705,0.042987,0.043275,0.043567,0.043639,0.044025,0.043869,0.044501,0.044421,0.044719,0.047077,0.045146,0.045185,0.045614,0.047368,0.045944,0.04603,0.047183,0.046265,0.046735,0.046548,0.046786,0.046992,0.047147,0.047296,0.047517,0.047894,0.047919,0.048135,0.048285,0.048394,0.048663,0.048953,0.049148,0.049157,0.049437,0.049796,0.049787,0.050076,0.050248,0.050391,0.050553,0.050753,0.050972,0.051191,0.051334,0.05198,0.051717,0.052091,0.052159,0.052513,0.052839,0.052753,0.052941,0.053294,0.053365,0.053667,0.056049,0.054042,0.054172,0.054502,0.05459,0.054582,0.054742,0.055032,0.055172,0.055309,0.055584,0.055788,0.056118,0.056083,0.056479,0.056714,0.056834,0.057048,0.057642,0.057324,0.057419,0.057553,0.057911,0.058029,0.058173,0.058355,0.05871,0.058799,0.058974,0.059073,0.059335,0.059764,0.060492,0.060189,0.060629,0.060323,0.060995,0.061046,0.061327,0.061425,0.061711,0.061712,0.062284,0.064342,0.062676,0.062522,0.063087,0.062716,0.063138,0.063141,0.063285,0.063558,0.063751,0.063819,0.064139,0.064308,0.064512,0.064889,0.064944,0.065785,0.065427,0.065364,0.065585,0.065835,0.066095,0.066247,0.06671,0.066666,0.066953,0.067148,0.067226,0.067311,0.067595,0.067694,0.068033,0.068839,0.068316,0.068984,0.068831,0.069509,0.069465,0.069868,0.06987,0.070258,0.070206,0.070923,0.07049,0.071319,0.070947,0.071433,0.071469,0.071923,0.0717,0.07179,0.071971,0.072095,0.072413,0.07275,0.072977,0.072911,0.073057,0.073302,0.073572,0.075032,0.073979,0.074047,0.074575,0.074489,0.074752,0.074756,0.075284,0.075332,0.075647,0.075702,0.078193,0.07598,0.076436,0.076497,0.07716,0.076915,0.077448,0.077504,0.077811,0.078078,0.078144,0.078266,0.078847,0.078769,0.07895,0.078999,0.079294,0.079378,0.079899,0.079764,0.079876,0.080336,0.080315,0.080476,0.080728,0.080921,0.081084,0.081243,0.081386,0.081735,0.081845,0.082085,0.082852,0.083386,0.08282,0.083008,0.083296,0.083188,0.083396,0.083703,0.0838,0.084001,0.084131,0.084508,0.084603,0.085566,0.08519,0.085861,0.085399,0.086093,0.086143,0.086525,0.086611,0.087238,0.086983,0.087554,0.087169,0.087776,0.087564,0.088646,0.087868,0.088732,0.088376,0.088929,0.088943,0.088986,0.090264,0.089341,0.089796,0.08981,0.089841,0.089936,0.090243,0.091872,0.090959,0.090862,0.091072,0.091368,0.09164,0.091864,0.091838,0.092097,0.092408,0.092832,0.092681,0.092869,0.093149,0.093202,0.093863,0.093807,0.094679,0.094134,0.094829,0.102437,0.095258,0.095297,0.095751,0.095726,0.096098,0.09589,0.09669,0.096394,0.097002,0.096603,0.097477,0.096966,0.09723,0.097352,0.097486,0.097808,0.09816,0.098294,0.098551,0.099667,0.098982,0.099081,0.099044,0.099333,0.09959,0.100015,0.100161,0.100237,0.100521,0.100516,0.100894,0.101096,0.101392,0.101395,0.101647,0.10188,0.102183,0.102944,0.102398,0.103078,0.102836,0.103407,0.103417,0.103777,0.104076,0.104686,0.104545,0.104617,0.109012,0.105176,0.105003,0.105603,0.105389,0.105937,0.106379,0.105975,0.106461,0.106411,0.106849,0.107209,0.106933,0.107062,0.107341,0.107564,0.108088,0.107961,0.108318,0.108611,0.109473,0.109032,0.109102,0.109664,0.109417,0.109453,0.110067,0.110012,0.110283,0.110611,0.110742,0.111023,0.111733,0.111405,0.111957,0.111781,0.112375,0.112308,0.113279,0.112695,0.113304,0.113311,0.113939,0.113651,0.114377,0.113786,0.115842,0.114155,0.115079,0.114567,0.114807,0.115121,0.115001,0.115467,0.115549,0.115868,0.116169,0.116292,0.116284,0.116723,0.116827,0.11708,0.117176,0.117488,0.117707,0.117852,0.118305,0.118269,0.118332,0.119504,0.118906,0.119183,0.11928,0.119481,0.119603,0.120818,0.120075,0.121153,0.120555,0.121446,0.121333,0.122266,0.121716,0.122637,0.122006,0.122688,0.122339,0.139759,0.122818,0.123559,0.123282,0.123895,0.123791,0.123501,0.123933,0.123809,0.124385,0.124571,0.12464,0.124848,0.125166,0.125314,0.125782,0.125782,0.125911,0.126276,0.126566,0.127149,0.127034,0.127073,0.127394,0.127871,0.127657,0.128371,0.12813,0.128322,0.128709,0.128715,0.129454,0.129192,0.129914,0.131037,0.130925,0.130156,0.130621,0.147049,0.131041,0.131289,0.131304,0.131521,0.131886,0.131685,0.132382,0.132169,0.132564,0.132433,0.132417,0.133179,0.133469,0.133376,0.133363,0.133827,0.133791,0.134186,0.134253,0.134725,0.134731,0.13502,0.135347,0.135511,0.135406,0.135925,0.13597,0.136106,0.136635,0.136997,0.136911,0.137114,0.137391,0.138109,0.137624,0.138625,0.138217,0.138929,0.145303,0.139375,0.139369,0.140005,0.13967,0.140373,0.140029,0.140927,0.140647,0.141808,0.140685,0.142519,0.141511,0.142218,0.14404,0.142,0.141945,0.142208,0.142427,0.142253,0.144296,0.142964,0.143177,0.143104,0.14353,0.144543,0.14414,0.144317,0.144286,0.144888,0.144998,0.167002,0.145274,0.145294,0.145584,0.145724,0.146037,0.146369,0.147071,0.146611,0.147778,0.147154,0.148111,0.147676,0.149614,0.154994,0.149238,0.148757,0.149437,0.148931,0.15,0.149391,0.150504,0.149835,0.150946,0.150229,0.150855,0.150546,0.150534,0.150969,0.151004,0.151538,0.151438,0.151803,0.151934,0.152615,0.152302,0.152835,0.15295,0.152971,0.152956,0.153328,0.154399,0.153803,0.154458,0.15472,0.154288,0.154777,0.155127,0.159246,0.155142,0.156382,0.155822,0.156418,0.155972,0.156833,0.157263,0.15743,0.157506,0.15794,0.157762,0.158316,0.158178,0.158568,0.158427,0.159519,0.158954,0.159587,0.159246,0.159268,0.159884,0.159645,0.160064,0.160483,0.160514,0.164055,0.161183,0.161271,0.161559,0.161616,0.162445,0.162254,0.162248,0.162995,0.162634,0.162726,0.163241,0.163269,0.164382,0.163589,0.164131,0.163934,0.164115,0.164806,0.166649,0.164708,0.165721,0.165326,0.16624,0.171892,0.166828,0.166461,0.167132,0.167198,0.167857,0.167078,0.168451,0.167674,0.169156,0.170173,0.169401,0.168487,0.168599,0.168912,0.168941,0.169166,0.169631,0.169498,0.169606,0.170217,0.170214,0.171823,0.170833,0.170716,0.171054,0.171262,0.171269,0.171633,0.171877,0.172027,0.1724,0.175011,0.17404,0.173347,0.173414,0.17362,0.173901,0.175342,0.174016,0.175357,0.174215,0.175736,0.175346,0.176153,0.175806,0.176657,0.176073,0.177429,0.176439,0.177594,0.176762,0.178176,0.177316,0.178454,0.177504,0.177804,0.177859,0.178544,0.178497,0.178663,0.179255,0.178848,0.179349,0.179625,0.17982,0.179881,0.180439,0.180387,0.18045,0.180892,0.180928,0.180783,0.181662,0.181506,0.181599,0.182704,0.185945,0.182378,0.182944,0.182765,0.183792,0.183496,0.184044,0.183831,0.187667,0.184891,0.185056,0.185682,0.185796,0.185599,0.186021,0.190967,0.186301,0.186101,0.186791,0.186384,0.18756,0.187044,0.187038,0.18755,0.187328,0.187647,0.187876,0.187961,0.188597,0.188911,0.188453,0.189059,0.190211,0.189241,0.189239,0.189667,0.190078,0.19022,0.190658,0.190554,0.190785,0.191332,0.191098,0.191376,0.191501,0.192478,0.191942,0.193149,0.192351,0.193521,0.193416,0.193779,0.193963,0.194482,0.194125,0.195168,0.194317,0.197764,0.195003,0.196858]
	heapSize = []	
	for i in range(1, 500000, 500):
		heapSize.append(i)
		
	insertTime = [0,1.2e-05,4.4e-05,9.9e-05,0.000154,0.000245,0.000357,0.000524,0.000623,0.000835,0.000948,0.001188,0.001369,0.001658,0.002409,0.002452,0.002385,0.002887,0.003082,0.003486,0.00389,0.004344,0.004996,0.005146,0.005507,0.006112,0.006729,0.006905,0.007422,0.008015,0.008638,0.008989,0.009807,0.010572,0.011192,0.011648,0.012431,0.012937,0.013663,0.014489,0.015211,0.015868,0.016934,0.017595,0.018325,0.019164,0.020096,0.02078,0.02233,0.022862,0.024055,0.024817,0.025752,0.026908,0.027863,0.029127,0.030049,0.031551,0.031916,0.033568,0.034228,0.035547,0.037075,0.037781,0.039109,0.040114,0.04086,0.042252,0.044503,0.045437,0.046606,0.047366,0.049973,0.050364,0.051152,0.053688,0.054743,0.055995,0.057961,0.059863,0.060389,0.061918,0.063623,0.066109,0.067735,0.068516,0.070871,0.071504,0.074144,0.076251,0.076897,0.079078,0.079869,0.082647,0.083513,0.08481,0.086682,0.089274,0.092504,0.093346,0.095133,0.097234,0.099081,0.099365,0.102541,0.105054,0.106364,0.106673,0.109949,0.113009,0.114883,0.119139,0.120216,0.122496,0.123487,0.126001,0.130215,0.130457,0.132903,0.135998,0.139511,0.139007,0.141903,0.14414,0.148573,0.148237,0.152468,0.155191,0.156956,0.15953,0.161036,0.163355,0.166573,0.167472,0.171232,0.174648,0.176504,0.178498,0.181149,0.184682,0.186424,0.189347,0.191743,0.193726,0.197665,0.197704,0.203361,0.20627,0.210446,0.209612,0.215069,0.219109,0.221785,0.224249,0.22559,0.228743,0.23474,0.234807,0.238707,0.239658,0.243939,0.245026,0.24873,0.251247,0.256534,0.256568,0.262762,0.262224,0.266891,0.269778,0.272226,0.274808,0.279825,0.282496,0.290699,0.293433,0.293216,0.29584,0.300243,0.302409,0.308453,0.311869,0.315005,0.316067,0.321072,0.325172,0.326719,0.331032,0.33444,0.339266,0.343287,0.348938,0.351682,0.352045,0.358271,0.360681,0.363576,0.371203,0.372599,0.374344,0.380066,0.38379,0.384773,0.390322,0.395187,0.394624,0.404313,0.409821,0.410141,0.412497,0.41878,0.425565,0.42638,0.432883,0.438112,0.442584,0.445526,0.448245,0.45368,0.454291,0.460603,0.466076,0.467773,0.470924,0.475533,0.480564,0.485476,0.490533,0.493031,0.499888,0.506132,0.509295,0.514287,0.512405,0.518738,0.523101,0.530329,0.531982,0.535425,0.542357,0.55101,0.552408,0.55553,0.562291,0.564621,0.570921,0.576901,0.577895,0.584155,0.589955,0.596042,0.597578,0.603788,0.6087,0.611587,0.619387,0.620304,0.626264,0.637011,0.637276,0.642445,0.650372,0.651983,0.658308,0.661486,0.663787,0.668425,0.680296,0.686536,0.686488,0.685866,0.696741,0.704418,0.711968,0.714352,0.718768,0.724773,0.732559,0.739624,0.740843,0.745559,0.752633,0.764071,0.75472,0.764315,0.767031,0.774315,0.780193,0.789726,0.790888,0.803291,0.806535,0.809025,0.813813,0.815545,0.826957,0.832798,0.839704,0.843031,0.848473,0.85645,0.857432,0.865008,0.870766,0.88178,0.881063,0.893984,0.89423,0.90016,0.907197,0.911876,0.914223,0.920147,0.932317,0.939312,0.941936,0.947462,0.953421,0.963624,0.966885,0.975257,0.983017,0.990724,0.990718,1.00139,1.00225,1.0111,1.02088,1.0284,1.02799,1.04338,1.04724,1.06116,1.05931,1.05806,1.06425,1.07063,1.08184,1.08547,1.08952,1.10602,1.10829,1.11015,1.11346,1.11919,1.13265,1.13651,1.14284,1.14902,1.16141,1.1724,1.17038,1.18417,1.1856,1.1885,1.19247,1.19971,1.21037,1.22161,1.22314,1.23089,1.24385,1.24272,1.25033,1.25587,1.25946,1.2696,1.27663,1.28327,1.29078,1.29685,1.31193,1.31456,1.31343,1.32218,1.34212,1.34523,1.35021,1.35702,1.36645,1.37105,1.38716,1.38369,1.39338,1.4061,1.40082,1.42331,1.4268,1.42365,1.4412,1.44437,1.45373,1.46634,1.47021,1.48333,1.48403,1.50164,1.49334,1.51134,1.5105,1.5259,1.53388,1.53436,1.53508,1.54589,1.55856,1.56226,1.56303,1.58066,1.58465,1.59057,1.59442,1.61337,1.61432,1.62233,1.63329,1.63855,1.65508,1.65696,1.67256,1.68251,1.68771,1.69951,1.70052,1.70854,1.70823,1.72389,1.73455,1.74459,1.753,1.75274,1.76745,1.77821,1.77399,1.7966,1.80377,1.80134,1.81201,1.82139,1.83767,1.83157,1.84963,1.86095,1.86327,1.86363,1.88493,1.9017,1.91168,1.9054,1.92502,1.92027,1.94209,1.96072,1.957,1.96129,1.97866,1.9786,1.99284,2.00021,2.00564,2.01966,2.01997,2.01553,2.04721,2.04853,2.04925,2.07579,2.07537,2.08888,2.09147,2.10083,2.11677,2.12633,2.12933,2.12146,2.15348,2.17733,2.16598,2.16583,2.19027,2.2023,2.20572,2.21533,2.21414,2.2385,2.22967,2.24504,2.24724,2.27168,2.27338,2.29829,2.28013,2.2988,2.3121,2.31656,2.3365,2.32848,2.34299,2.35133,2.36045]
	insertSize = []
	for i in range(1, 50000, 100):
		insertSize.append(i)
	
	mergeTime = [3e-06,0.000268,0.000561,0.000891,0.001182,0.001549,0.001748,0.001988,0.002252,0.002585,0.002891,0.00315,0.003151,0.003443,0.00373,0.003674,0.003883,0.004167,0.004085,0.004323,0.004482,0.00445,0.004699,0.004604,0.00474,0.004839,0.004871,0.004104,0.003296,0.003405,0.00353,0.003576,0.003618,0.003742,0.003818,0.003859,0.003989,0.004014,0.004056,0.004175,0.004191,0.004226,0.004388,0.004349,0.004449,0.004471,0.004491,0.004597,0.004548,0.00462,0.00469,0.004711,0.004838,0.00477,0.004865,0.004895,0.004915,0.00494,0.004914,0.005017,0.004971,0.005057,0.005148,0.005236,0.005314,0.005384,0.005473,0.005584,0.005687,0.005797,0.005906,0.00599,0.006086,0.006153,0.006234,0.006333,0.006418,0.006533,0.006623,0.006728,0.006843,0.006864,0.006932,0.007051,0.007162,0.007265,0.007356,0.007462,0.007554,0.007643,0.007716,0.00781,0.007904,0.007985,0.008071,0.008159,0.008248,0.008333,0.008382,0.008498,0.008624,0.008742,0.00883,0.008935,0.00903,0.009108,0.009197,0.009284,0.009604,0.009512,0.009589,0.00968,0.009758,0.009827,0.00988,0.009968,0.010111,0.010449,0.010319,0.010436,0.010494,0.010596,0.010847,0.010734,0.010839,0.010945,0.011015,0.011108,0.011206,0.011265,0.011341,0.011404,0.01155,0.011663,0.011775,0.01187,0.012002,0.012101,0.012197,0.01228,0.012416,0.01267,0.01274,0.012748,0.012907,0.012956,0.013006,0.013055,0.013185,0.013307,0.013363,0.01356,0.013585,0.01372,0.013768,0.013851,0.013951,0.014055,0.014133,0.014231,0.014307,0.014424,0.014459,0.014523,0.014615,0.014728,0.014863,0.015008,0.015111,0.015193,0.015297,0.015391,0.0155,0.0156,0.015695,0.015816,0.015888,0.016001,0.01611,0.016175,0.01625,0.016335,0.016431,0.016521,0.016605,0.016777,0.016819,0.016899,0.016965,0.01705,0.017147,0.017249,0.017348,0.017449,0.017523,0.01763,0.017748,0.017858,0.018025,0.018128,0.018204,0.018398,0.018451,0.018568,0.018699,0.018752,0.018979,0.018999,0.019126,0.019189,0.019278,0.01933,0.019468,0.019495,0.01957,0.019712,0.019845,0.020006,0.02013,0.020199,0.020315,0.02032,0.02038,0.020567,0.020571,0.020746,0.02079,0.020804,0.020931,0.021022,0.021088,0.021223,0.021527,0.021401,0.021494,0.021614,0.021636,0.021735,0.02185,0.02193,0.022019,0.02214,0.022274,0.022286,0.022406,0.022565,0.022729,0.022717,0.02294,0.023009,0.023172,0.023238,0.023321,0.023415,0.023614,0.023579,0.023659,0.023677,0.023718,0.023763,0.023831,0.023964,0.024009,0.024126,0.024408,0.024592,0.024652,0.024789,0.024883,0.024901,0.025043,0.025215,0.025443,0.025558,0.025608,0.025668,0.025796,0.025799,0.025833,0.02594,0.02609,0.026219,0.026374,0.026448,0.026535,0.026685,0.026794,0.026855,0.026944,0.026983,0.027141,0.027154,0.027225,0.027276,0.027349,0.027448,0.027556,0.027637,0.027801,0.027924,0.027974,0.028104,0.028244,0.028379,0.028423,0.028638,0.028627,0.028932,0.028936,0.028983,0.029067,0.029272,0.02942,0.029419,0.0295,0.029638,0.02986,0.02982,0.029911,0.029992,0.030051,0.030119,0.030196,0.030267,0.030371,0.030529,0.03048,0.030585,0.030703,0.030828,0.030972,0.031089,0.03119,0.031316,0.031428,0.031574,0.031651,0.031773,0.031886,0.032047,0.032152,0.032262,0.03236,0.03248,0.032532,0.032659,0.032736,0.032875,0.033222,0.033157,0.0332,0.033274,0.033368,0.033491,0.033585,0.033711,0.033764,0.033842,0.033951,0.034014,0.034077,0.034172,0.034298,0.03439,0.034525,0.034616,0.034688,0.034767,0.03485,0.034963,0.035104,0.035219,0.035282,0.035346,0.035436,0.035536,0.035595,0.035659,0.03581,0.035913,0.036159,0.036284,0.036365,0.036522,0.036608,0.036606,0.036618,0.03683,0.036889,0.037003,0.037046,0.036962,0.037061,0.037138,0.037326,0.03744,0.037577,0.037693,0.037829,0.037946,0.038122,0.038211,0.038294,0.03855,0.038698,0.038827,0.038848,0.038886,0.038951,0.039096,0.039243,0.039316,0.039394,0.039518,0.039626,0.039699,0.039884,0.03986,0.039999,0.040305,0.040236,0.04034,0.040487,0.040533,0.040615,0.04067,0.040723,0.040889,0.041021,0.041158,0.041289,0.041309,0.041439,0.041577,0.041739,0.041781,0.041922,0.042009,0.042167,0.042208,0.042349,0.04239,0.042515,0.042559,0.042663,0.042743,0.042827,0.042912,0.043042,0.043121,0.043171,0.043263,0.043349,0.043441,0.043595,0.043628,0.043669,0.043769,0.043761,0.04384,0.044011,0.044126,0.044261,0.044631,0.044611,0.044589,0.044694,0.044827,0.045069,0.045046,0.04529,0.04555,0.045674,0.04581,0.045858,0.045942,0.046123,0.046144,0.046247,0.046292,0.046221,0.046247,0.046353,0.046622,0.046671,0.04674,0.04688,0.047057,0.047032,0.047094,0.047194,0.047268,0.04737,0.047458,0.047584,0.047663,0.047815,0.04809,0.048071,0.048127,0.048249,0.048332,0.048427,0.048511,0.048578,0.048718,0.04885,0.048915,0.049031,0.049084,0.049191,0.049223,0.049341,0.049437,0.049757,0.049858,0.049985,0.049931,0.049898,0.049917,0.05014,0.050098,0.050196,0.050228,0.050342,0.050509,0.050607,0.050778,0.050917,0.051044,0.051125,0.051263,0.051343,0.051521,0.051727,0.051774,0.052479,0.053599,0.053262,0.052755,0.052362,0.052479,0.05262,0.052721,0.053186,0.052983,0.053116,0.053163,0.053334,0.053451,0.053543,0.053904,0.053826,0.053904,0.053902,0.053974,0.054171,0.054618,0.054374,0.054637,0.054662,0.054782,0.054877,0.054987,0.055194,0.055517,0.055463,0.055578,0.055553,0.055906,0.055805,0.056114,0.056309,0.056079,0.056205,0.056278,0.056383,0.056421,0.056939,0.056896,0.056717,0.056843,0.056881,0.056978,0.057547,0.058085,0.058143,0.057911,0.058689,0.058893,0.057759,0.057621,0.057799,0.058182,0.05798,0.05813,0.058234,0.05885,0.058732,0.058888,0.058637,0.058801,0.05892,0.059501,0.059974,0.060153,0.059618,0.05952,0.059684,0.059926,0.059786,0.06006,0.060361,0.060633,0.060538,0.06044,0.060569,0.061344,0.062369,0.061049,0.060965,0.061035,0.061118,0.061276,0.061798,0.061922,0.062065,0.062251,0.062253,0.062481,0.062409,0.062651,0.062818,0.062726,0.062754,0.063003,0.063023,0.063249,0.063278,0.063674,0.063377,0.063342,0.063333,0.063712,0.063575,0.063744,0.063656,0.06373,0.063626,0.063814,0.063784,0.063859,0.06399,0.064103,0.06414,0.065,0.064661,0.064756,0.064857,0.064899,0.065466,0.065496,0.065707,0.065693,0.065722,0.06563,0.066115,0.066249,0.066028,0.066163,0.066285,0.066372,0.066717,0.066487,0.066616,0.06676,0.066997,0.067208,0.067169,0.067234,0.067425,0.067374,0.067547,0.06756,0.067732,0.067788,0.068156,0.068486,0.068493,0.068383,0.068391,0.068619,0.069958,0.069006,0.069089,0.068973,0.069364,0.069621,0.069647,0.069611,0.069813,0.069877,0.069926,0.070051,0.070214,0.070371,0.070319,0.070453,0.072036,0.071734,0.071328,0.070898,0.070714,0.070842,0.070998,0.071027,0.071167,0.071144,0.07124,0.071222,0.071308,0.071428,0.071527,0.071662,0.072753,0.073058,0.073441,0.072997,0.073571,0.074077,0.073755,0.073922,0.074513,0.07428,0.074317,0.074839,0.074051,0.073898,0.07327,0.073463,0.073557,0.073598,0.073654,0.073707,0.073804,0.074011,0.074746,0.074688,0.07454,0.074339,0.074425,0.074544,0.074656,0.074695,0.07476,0.07502,0.074979,0.07504,0.075138,0.075256,0.075403,0.075507,0.075569,0.075834,0.075888,0.075878,0.076002,0.076103,0.076169,0.076343,0.076451,0.076551,0.076536,0.076659,0.076799,0.076953,0.077046,0.077093,0.07735,0.077167,0.077246,0.077365,0.077451,0.077478,0.077564,0.07768,0.077814,0.077933,0.078107,0.078251,0.078384,0.078559,0.078652,0.078862,0.078903,0.079075,0.07926,0.079368,0.079446,0.07967,0.079919,0.079824,0.079919,0.080079,0.080231,0.080308,0.080468,0.080575,0.080705,0.081291,0.081194,0.081116,0.081233,0.081297,0.081354,0.081527,0.081675,0.081779,0.081883,0.081986,0.082102,0.08219,0.082516,0.082477,0.082507,0.08266,0.082844,0.082996,0.083585,0.084168,0.084255,0.083887,0.084497,0.08399,0.084088,0.084019,0.084558,0.085035,0.084678,0.084868,0.084436,0.084257,0.084289,0.08466,0.084535,0.084663,0.084693,0.085104,0.084996,0.08512,0.085272,0.085216,0.085215,0.085484,0.085534,0.086107,0.085894,0.085897,0.086076,0.086205,0.086326,0.086407,0.08658,0.086661,0.086848,0.086934,0.086991,0.08718,0.087325,0.087414,0.087551,0.087627,0.087706,0.087867,0.0879,0.088014,0.088113,0.08823,0.088335,0.088429,0.088602,0.088707,0.088739,0.088935,0.088951,0.089061,0.08907,0.089225,0.089241,0.089353,0.089463,0.089502,0.089631,0.089736,0.089993,0.090038,0.089988,0.09012,0.090219,0.090311,0.090342,0.090449,0.09052,0.090627,0.09069,0.090762,0.090872,0.090976,0.091009,0.091173,0.091214,0.091351,0.091362,0.091406,0.091487,0.091588,0.091626,0.091756,0.091817,0.091966,0.092117,0.092213,0.092337,0.092548,0.093152,0.092932,0.092905,0.09308,0.093181,0.093222,0.093482,0.09345,0.093569,0.093683,0.093777,0.093938,0.094289,0.09425,0.094359,0.094365,0.094489,0.094715,0.094795,0.0949,0.094924,0.095054,0.095164,0.095282,0.095647,0.095512,0.095538,0.09573,0.095744,0.095972,0.096129,0.096145,0.096422,0.096381,0.096441,0.096786,0.096931,0.096908,0.096859,0.096997,0.097101,0.097178,0.097437,0.097384,0.09748,0.097585,0.097641,0.09784,0.098159,0.098004,0.098102,0.098193,0.098329,0.09838,0.098583,0.098686,0.09864,0.098778,0.098837,0.098979,0.09934,0.099191,0.099314,0.099445,0.099571,0.099638,0.099841,0.099978,0.099978,0.100094,0.100229,0.100372,0.100799,0.10056,0.100736,0.100876]
	mergeSize = []	
	for i in range(1, 500000, 500):
		mergeSize.append(i)

	quickTime = [1e-06,3.9e-05,9.2e-05,0.000132,0.000173,0.000231,0.000277,0.000327,0.000376,0.000495,0.001,0.001124,0.001258,0.001406,0.001043,0.000809,0.00084,0.000898,0.000965,0.001001,0.001048,0.001143,0.001189,0.001196,0.001291,0.001316,0.001418,0.001461,0.001545,0.001631,0.001678,0.00175,0.001792,0.001806,0.001869,0.001891,0.001959,0.002026,0.002101,0.002164,0.002262,0.002284,0.002425,0.0024,0.00247,0.002499,0.002639,0.002656,0.002714,0.002787,0.002781,0.002852,0.003008,0.003021,0.003086,0.003142,0.003231,0.003252,0.003367,0.003409,0.003425,0.003523,0.003592,0.003698,0.00378,0.003773,0.003829,0.003896,0.003932,0.004026,0.004082,0.004157,0.004178,0.004287,0.004335,0.004436,0.004492,0.00448,0.004616,0.004707,0.004751,0.004805,0.004905,0.004988,0.004944,0.005099,0.005166,0.005225,0.005321,0.005344,0.005342,0.005379,0.005524,0.005715,0.005632,0.005655,0.005749,0.005828,0.005868,0.006066,0.005998,0.006093,0.006194,0.006291,0.006361,0.00638,0.006375,0.006497,0.006466,0.006607,0.00673,0.00681,0.00677,0.006853,0.006907,0.006969,0.007133,0.00718,0.00722,0.007288,0.007438,0.007418,0.00755,0.007558,0.007558,0.007794,0.007737,0.007739,0.007876,0.007947,0.008104,0.008066,0.008178,0.008142,0.00844,0.008353,0.008392,0.008701,0.008712,0.008571,0.008715,0.008758,0.008887,0.008904,0.008976,0.009095,0.008954,0.009029,0.009174,0.009424,0.009307,0.009419,0.009517,0.009487,0.009696,0.009735,0.009773,0.009675,0.009912,0.009946,0.010072,0.010247,0.01012,0.010284,0.010504,0.010515,0.01039,0.010604,0.010494,0.010644,0.010733,0.010625,0.010988,0.011066,0.011136,0.01105,0.011032,0.011839,0.011232,0.011407,0.011259,0.011674,0.011605,0.011863,0.01163,0.011904,0.011762,0.011866,0.012279,0.01198,0.012308,0.012188,0.012522,0.012319,0.012317,0.012609,0.012561,0.012582,0.012645,0.012861,0.012783,0.012725,0.012983,0.013053,0.013257,0.013354,0.013866,0.013312,0.013376,0.013456,0.013696,0.013496,0.013597,0.013971,0.014241,0.013982,0.013901,0.014123,0.013963,0.014165,0.014456,0.014566,0.014482,0.01449,0.014383,0.014742,0.01458,0.014738,0.014882,0.014787,0.014943,0.015161,0.015051,0.015377,0.015808,0.015356,0.015488,0.015477,0.015337,0.015402,0.015303,0.015579,0.01574,0.016127,0.016169,0.016261,0.016511,0.016128,0.016515,0.016433,0.016333,0.016336,0.016231,0.01643,0.016431,0.016534,0.016421,0.016668,0.017053,0.017084,0.017139,0.017067,0.016955,0.017208,0.017334,0.017311,0.017384,0.017445,0.017564,0.017801,0.01783,0.017667,0.01829,0.017841,0.017866,0.017935,0.017918,0.018419,0.018351,0.018799,0.018443,0.018676,0.01878,0.018738,0.018954,0.018647,0.018797,0.019232,0.019215,0.018875,0.01899,0.019224,0.019518,0.019269,0.019507,0.019512,0.019475,0.019649,0.019801,0.019747,0.019839,0.020084,0.01988,0.019895,0.020064,0.020584,0.020441,0.020494,0.020842,0.020701,0.020546,0.020506,0.021016,0.021225,0.021345,0.02142,0.020874,0.021475,0.020926,0.021361,0.022737,0.021666,0.021673,0.021321,0.021886,0.021659,0.021386,0.02169,0.021645,0.021914,0.021901,0.021933,0.022179,0.022183,0.022623,0.021738,0.022074,0.022581,0.022839,0.022573,0.022523,0.022661,0.022684,0.022878,0.02285,0.023269,0.023029,0.023466,0.023317,0.023196,0.023221,0.023452,0.023657,0.023515,0.023551,0.0243,0.023906,0.023962,0.023826,0.023997,0.02411,0.024358,0.024145,0.02437,0.024851,0.024814,0.024395,0.024516,0.024632,0.024663,0.024957,0.024858,0.025115,0.025073,0.02518,0.025279,0.025156,0.025286,0.025652,0.025364,0.025649,0.026292,0.025637,0.025622,0.02583,0.026102,0.025988,0.025937,0.026116,0.026328,0.026639,0.026357,0.026662,0.026367,0.026603,0.026712,0.027212,0.026826,0.026837,0.027257,0.027184,0.027424,0.02699,0.027307,0.027431,0.027261,0.027056,0.027988,0.027544,0.028676,0.027544,0.027787,0.028224,0.027651,0.027931,0.028016,0.028341,0.028315,0.028408,0.028607,0.028696,0.028735,0.028716,0.028722,0.028461,0.02837,0.02879,0.029342,0.028952,0.030416,0.029853,0.029102,0.029296,0.03015,0.029471,0.029529,0.029506,0.030046,0.03039,0.029902,0.02984,0.029802,0.030324,0.030179,0.030481,0.030219,0.031071,0.031017,0.031105,0.030927,0.03075,0.030637,0.030633,0.031083,0.031131,0.030915,0.031088,0.031578,0.031215,0.031112,0.031193,0.031206,0.031736,0.031808,0.032222,0.03173,0.031533,0.031986,0.031695,0.032212,0.031953,0.03295,0.032263,0.032586,0.033077,0.032895,0.032219,0.032687,0.0325,0.033041,0.033061,0.032949,0.032897,0.033314,0.033231,0.033213,0.034553,0.033489,0.033639,0.033667,0.03446,0.033508,0.033803,0.034225,0.034857,0.03447,0.034074,0.033985,0.033919,0.035517,0.034812,0.034397,0.034272,0.034358,0.035486,0.035315,0.034762,0.035162,0.035181,0.035208,0.035564,0.035699,0.035147,0.036051,0.035316,0.036189,0.035396,0.035899,0.035845,0.03583,0.036152,0.035923,0.036132,0.036298,0.03706,0.036424,0.036107,0.036098,0.036327,0.036254,0.036726,0.038133,0.0364,0.038246,0.037093,0.036667,0.036949,0.037749,0.037363,0.037319,0.037054,0.0379,0.037604,0.037403,0.03751,0.03773,0.037823,0.039251,0.037738,0.03772,0.037603,0.038618,0.038382,0.038047,0.039134,0.038627,0.038151,0.038535,0.039039,0.038338,0.038504,0.038822,0.039325,0.039011,0.038907,0.039175,0.039163,0.040408,0.039148,0.039817,0.039968,0.040015,0.039509,0.039486,0.040662,0.040772,0.03996,0.040415,0.040288,0.040255,0.040552,0.040619,0.040286,0.040244,0.040478,0.041183,0.040767,0.040849,0.041241,0.041391,0.04085,0.040974,0.040753,0.041325,0.041468,0.041587,0.041469,0.041694,0.041914,0.042306,0.041722,0.042022,0.042096,0.041657,0.041649,0.042494,0.042305,0.042331,0.042776,0.042171,0.04294,0.043099,0.043438,0.0433,0.042864,0.043197,0.042965,0.044369,0.0432,0.042944,0.043723,0.042986,0.043295,0.043343,0.043335,0.043498,0.04346,0.044033,0.043995,0.043185,0.043834,0.043793,0.044549,0.044634,0.044045,0.044311,0.04433,0.044324,0.044612,0.044466,0.044649,0.044453,0.04517,0.045232,0.045837,0.045442,0.045431,0.044959,0.045904,0.046063,0.046205,0.046095,0.045538,0.046313,0.045409,0.046254,0.046705,0.046228,0.046332,0.046743,0.04623,0.046852,0.046765,0.046498,0.046319,0.046498,0.047147,0.046488,0.046695,0.047098,0.046477,0.048074,0.047769,0.047205,0.047395,0.04782,0.047476,0.04786,0.047997,0.04807,0.047178,0.048811,0.0489,0.05008,0.048811,0.048323,0.047804,0.048721,0.049569,0.048172,0.047903,0.048769,0.048816,0.049145,0.048244,0.049075,0.049372,0.050012,0.049124,0.049849,0.048977,0.050086,0.049542,0.049565,0.050269,0.050792,0.049995,0.049908,0.050012,0.049529,0.051111,0.050179,0.051067,0.050071,0.052188,0.050956,0.050593,0.050852,0.05034,0.050391,0.050894,0.050395,0.050556,0.05106,0.051512,0.052049,0.051959,0.051437,0.052003,0.051291,0.051351,0.051211,0.05164,0.052338,0.05232,0.052063,0.0517,0.052381,0.05238,0.05368,0.052051,0.052605,0.05302,0.052912,0.053104,0.052655,0.052283,0.053006,0.053295,0.053336,0.053446,0.053701,0.052711,0.05388,0.053144,0.053205,0.053485,0.053971,0.053903,0.053956,0.054198,0.054667,0.053399,0.055205,0.053916,0.054752,0.054821,0.054258,0.054782,0.054957,0.054549,0.0545,0.054265,0.055328,0.056121,0.054777,0.055073,0.055885,0.054763,0.055006,0.055602,0.055779,0.055156,0.055359,0.055578,0.055678,0.055965,0.056345,0.056297,0.056111,0.056738,0.057313,0.056821,0.056314,0.057457,0.056802,0.05732,0.05621,0.057972,0.056996,0.056825,0.056825,0.056944,0.056939,0.057445,0.057444,0.057386,0.057779,0.057766,0.057883,0.057728,0.0579,0.058026,0.058045,0.058921,0.058887,0.057679,0.057689,0.058437,0.058532,0.058253,0.058428,0.058162,0.059128,0.059316,0.058361,0.059755,0.058732,0.058939,0.059058,0.05914,0.059493,0.059349,0.061135,0.059192,0.059556,0.060563,0.060796,0.060504,0.060893,0.060111,0.060049,0.061702,0.060472,0.060182,0.060173,0.060378,0.061521,0.060172,0.065247,0.060619,0.060358,0.061641,0.061934,0.061082,0.063286,0.061485,0.060789,0.061674,0.061346,0.061929,0.061957,0.061809,0.062092,0.061893,0.061871,0.063826,0.062578,0.06393,0.06304,0.062636,0.062904,0.062387,0.063211,0.062823,0.062448,0.062714,0.062656,0.062327,0.062557,0.062484,0.06374,0.062787,0.06347,0.063055,0.064242,0.066998,0.063146,0.063571,0.064817,0.063385,0.063343,0.063605,0.063886,0.064488,0.063921,0.06514,0.065557,0.064527,0.066806,0.065616,0.064758,0.064457,0.065116,0.06473,0.06538,0.065115,0.06505,0.064476,0.065775,0.06508,0.064616,0.065864,0.066621,0.065321,0.065132,0.065572,0.066856,0.065823,0.066487,0.066471,0.06685,0.066077,0.066344,0.067254,0.066524,0.066778,0.067541,0.066937,0.066744,0.067025,0.067223,0.067188,0.067113,0.067572,0.067669,0.06808,0.068841,0.067652,0.068891,0.068034,0.067762,0.067639,0.068168,0.06821,0.068462,0.068505,0.068636,0.068814,0.069358,0.068272,0.068423,0.068814,0.068641,0.068895,0.068879,0.068887,0.068193,0.069054,0.068906,0.070278,0.068838,0.069672,0.069582,0.069427,0.07023,0.06925,0.068981,0.071188,0.069927,0.069895,0.069823,0.070421,0.070383,0.070305,0.069917,0.069933,0.069705,0.07036,0.070902,0.070612,0.070249,0.071082,0.071161,0.071316,0.071917,0.071339,0.07125,0.07135,0.072274,0.072319,0.072012,0.072026,0.071581,0.072338,0.072901,0.072381,0.071495,0.072263,0.070497]
	quickSize = []
	for i in range(1, 500000, 500):
		quickSize.append(i)

	pyplot.plot(heapSize, heapTime, 'green')
	pyplot.plot(insertSize, insertTime, 'blue')
	pyplot.plot(mergeSize, mergeTime, 'red')
	pyplot.plot(quickSize, quickTime, 'purple')
	
	pyplot.axis([0,500000,0,1])
	pyplot.xlabel('Number of items')
	pyplot.ylabel('Time to sort (s)')
	pyplot.show()

def main():
	plot()

main()