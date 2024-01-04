#!/usr/bin/python3

Abilene_r = (("Amarillo", 266), ("Austin", 213), ("Beaumont", 412), ("Big Bend", 392), ("Big Spring", 107), ("Brownsville", 516), ("Brownwood", 77), ("Bryan", 253), ("Childress", 154), ("Corpus Christi", 387), ("Dalhart", 343),  ("Dallas", 180), ("Del Rio", 246), ("Denison", 235), ("Eagle Pass", 298),  ("El Paso", 439), ("Fort Stockton", 250), ("Fort Worth", 150), ("Gainsville", 195), ("Galveston", 398), ("Houston", 348), ("Huntsville", 304), ("Junction", 144), ("Kingsville", 397), ("Laredo", 373), ("Longview", 305), ("Lubbock", 162), ("Lufkin", 336), ("McAllen", 480), ("Odessa", 167), ("Orange", 434), ("Ozona", 170), ("Paris", 281), ("Pecos", 240), ("San Angelo", 89), ("San Antonio", 244), ("South Padre Is", 530), ("Temple", 181), ("Texarkana", 359), ("Tyler", 277), ("Van Horn", 328), ("Victoria", 334), ("Waco", 183), ("Wichita Falls", 141), ("Yoakum", 304))
5

Amarillo_r = (("Austin", 478), ("Beaumont", 637), ("Big Bend", 484), ("Big Spring", 222), ("Brownsville", 765), ("Brownwood", 342), ("Bryan", 503), ("Childress", 116), ("Corpus Christi", 636), ("Dalhart", 82),  ("Dallas", 361), ("Del Rio", 450), ("Denison", 348), ("Eagle Pass", 505),  ("El Paso", 418), ("Fort Stockton", 338), ("Fort Worth", 337), ("Gainsville", 309), ("Galveston", 646), ("Houston", 596), ("Huntsville", 528), ("Junction", 380), ("Kingsville", 646), ("Laredo", 609), ("Longview", 482), ("Lubbock", 119), ("Lufkin", 529), ("McAllen", 728), ("Odessa", 255), ("Orange", 649), ("Ozona", 336), ("Paris", 403), ("Pecos", 320), ("San Angelo", 293), ("San Antonio", 493), ("South Padre Is", 779), ("Temple", 444), ("Texarkana", 495), ("Tyler", 457), ("Van Horn", 401), ("Victoria", 600), ("Waco", 423), ("Wichita Falls", 225), ("Yoakum", 566))


Austin_r = (("Beaumont", 238), ("Big Bend", 462), ("Big Spring", 289), ("Brownsville", 325), ("Brownwood", 137), ("Bryan", 100), ("Childress", 367), ("Corpus Christi", 192), ("Dalhart", 556),  ("Dallas", 192), ("Del Rio", 232), ("Denison", 267), ("Eagle Pass", 220),  ("El Paso", 573), ("Fort Stockton", 335), ("Fort Worth", 187), ("Gainsville", 252), ("Galveston", 206), ("Houston", 162), ("Huntsville", 153), ("Junction", 139), ("Kingsville", 206), ("Laredo", 232), ("Longview", 256), ("Lubbock", 368), ("Lufkin", 219), ("McAllen", 300), ("Odessa", 334), ("Orange", 262), ("Ozona", 229), ("Paris", 294), ("Pecos", 388), ("San Angelo", 203), ("San Antonio", 79), ("South Padre Is", 339), ("Temple", 67), ("Texarkana", 340), ("Tyler", 224), ("Van Horn", 454), ("Victoria", 122), ("Waco", 102), ("Wichita Falls", 283), ("Yoakum", 88))


Beaumont_r = (("Big Bend", 699), ("Big Spring", 519), ("Brownsville", 437), ("Brownwood", 350), ("Bryan", 158), ("Childress", 521), ("Corpus Christi", 288), ("Dalhart", 719),  ("Dallas", 276), ("Del Rio", 434), ("Denison", 321), ("Eagle Pass", 421),  ("El Paso", 810), ("Fort Stockton", 572), ("Fort Worth", 301), ("Gainsville", 345), ("Galveston", 78), ("Houston", 86), ("Huntsville", 113), ("Junction", 376), ("Kingsville", 317), ("Laredo", 396), ("Longview", 194), ("Lubbock", 574), ("Lufkin", 108), ("McAllen", 430), ("Odessa", 567), ("Orange", 24), ("Ozona", 466), ("Paris", 292), ("Pecos", 625), ("San Angelo", 436), ("San Antonio", 281), ("South Padre Is", 451), ("Temple", 230), ("Texarkana", 256), ("Tyler", 192), ("Van Horn", 690), ("Victoria", 209), ("Waco", 242), ("Wichita Falls", 412), ("Yoakum", 204))


Big_Bend_r = (("Big Spring", 281), ("Brownsville", 636), ("Brownwood", 398), ("Bryan", 559), ("Childress", 483), ("Corpus Christi", 524), ("Dalhart", 525),  ("Dallas", 559), ("Del Rio", 253), ("Denison", 606), ("Eagle Pass", 309),  ("El Paso", 329), ("Fort Stockton", 139), ("Fort Worth", 529), ("Gainsville", 584), ("Galveston", 651), ("Houston", 603), ("Huntsville", 602), ("Junction", 332), ("Kingsville", 602), ("Laredo", 434), ("Longview", 649), ("Lubbock", 360), ("Lufkin", 675), ("McAllen", 578), ("Odessa", 222), ("Orange", 715), ("Ozona", 236), ("Paris", 665), ("Pecos", 190), ("San Angelo", 300), ("San Antonio", 406), ("South Padre Is", 644), ("Temple", 499), ("Texarkana", 744), ("Tyler", 647), ("Van Horn", 199), ("Victoria", 522), ("Waco", 518), ("Wichita Falls", 213), ("Yoakum", 460))


Big_Spring_r = (("Brownsville", 567), ("Brownwood", 174), ("Bryan", 360), ("Childress", 204), ("Corpus Christi", 438), ("Dalhart", 294),  ("Dallas", 287), ("Del Rio", 231), ("Denison", 341), ("Eagle Pass", 286),  ("El Paso", 332), ("Fort Stockton", 143), ("Fort Worth", 257), ("Gainsville", 301), ("Galveston", 493), ("Houston", 449), ("Huntsville", 411), ("Junction", 182), ("Kingsville", 448), ("Laredo", 406), ("Longview", 412), ("Lubbock", 104), ("Lufkin", 443), ("McAllen", 531), ("Odessa", 60), ("Orange", 541), ("Ozona", 117), ("Paris", 388), ("Pecos", 133), ("San Angelo", 87), ("San Antonio", 295), ("South Padre Is", 251), ("Temple", 288), ("Texarkana", 466), ("Tyler", 384), ("Van Horn", 221), ("Victoria", 402), ("Waco", 290), ("Wichita Falls", 234), ("Yoakum", 368))


Brownsville_r = (("Brownwood", 471), ("Bryan", 382), ("Childress", 671), ("Corpus Christi", 159), ("Dalhart", 842),  ("Dallas", 517), ("Del Rio", 378), ("Denison", 592), ("Eagle Pass", 324),  ("El Paso", 801), ("Fort Stockton", 563), ("Fort Worth", 512), ("Gainsville", 577), ("Galveston", 374), ("Houston", 352), ("Huntsville", 414), ("Junction", 386), ("Kingsville", 119), ("Laredo", 199), ("Longview", 557), ("Lubbock", 655), ("Lufkin", 470), ("McAllen", 56), ("Odessa", 609), ("Orange", 459), ("Ozona", 476), ("Paris", 615), ("Pecos", 616), ("San Angelo", 481), ("San Antonio", 272), ("South Padre Is", 27), ("Temple", 392), ("Texarkana", 634), ("Tyler", 526), ("Van Horn", 682), ("Victoria", 230), ("Waco", 427), ("Wichita Falls", 608), ("Yoakum", 259))


Brownwood_r = (("Bryan", 191), ("Childress", 231), ("Corpus Christi", 329), ("Dalhart", 420),  ("Dallas", 157), ("Del Rio", 231), ("Denison", 221), ("Eagle Pass", 260),  ("El Paso", 493), ("Fort Stockton", 260), ("Fort Worth", 127), ("Gainsville", 185), ("Galveston", 336), ("Houston", 286), ("Huntsville", 241), ("Junction", 107), ("Kingsville", 340), ("Laredo", 330), ("Longview", 278), ("Lubbock", 232), ("Lufkin", 274), ("McAllen", 423), ("Odessa", 219), ("Orange", 372), ("Ozona", 178), ("Paris", 257), ("Pecos", 293), ("San Angelo", 96), ("San Antonio", 187), ("South Padre Is", 473), ("Temple", 119), ("Texarkana", 335), ("Tyler", 242), ("Van Horn", 378), ("Victoria", 259), ("Waco", 123), ("Wichita Falls", 169), ("Yoakum", 226))



"""
Bryan_r = (("Childress", ), ("Corpus Christi", ), ("Dalhart", ),  ("Dallas", ), ("Del Rio", ), ("Denison", ), ("Eagle Pass", ),  ("El Paso", ), ("Fort Stockton", ), ("Fort Worth", ), ("Gainsville", ), ("Galveston", ), ("Houston", ), ("Huntsville", ), ("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Childress_r = (("Corpus Christi", ), ("Dalhart", ),  ("Dallas", ), ("Del Rio", ), ("Denison", ), ("Eagle Pass", ),  ("El Paso", ), ("Fort Stockton", ), ("Fort Worth", ), ("Gainsville", ), ("Galveston", ), ("Houston", ), ("Huntsville", ), ("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Corpus_Christi_r = (("Dalhart", ),  ("Dallas", ), ("Del Rio", ), ("Denison", ), ("Eagle Pass", ),  ("El Paso", ), ("Fort Stockton", ), ("Fort Worth", ), ("Gainsville", ), ("Galveston", ), ("Houston", ), ("Huntsville", ), ("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Dalhart_r = (("Dallas", ), ("Del Rio", ), ("Denison", ), ("Eagle Pass", ),  ("El Paso", ), ("Fort Stockton", ), ("Fort Worth", ), ("Gainsville", ), ("Galveston", ), ("Houston", ), ("Huntsville", ), ("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Dallas_r = (("Del Rio", ), ("Denison", ), ("Eagle Pass", ),  ("El Paso", ), ("Fort Stockton", ), ("Fort Worth", ), ("Gainsville", ), ("Galveston", ), ("Houston", ), ("Huntsville", ), ("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Del_Rio_r = (("Denison", ), ("Eagle Pass", ),  ("El Paso", ), ("Fort Stockton", ), ("Fort Worth", ), ("Gainsville", ), ("Galveston", ), ("Houston", ), ("Huntsville", ), ("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Denison_r = (("Eagle Pass", ),  ("El Paso", ), ("Fort Stockton", ), ("Fort Worth", ), ("Gainsville", ), ("Galveston", ), ("Houston", ), ("Huntsville", ), ("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Eagle_pass_r = (("El Paso", ), ("Fort Stockton", ), ("Fort Worth", ), ("Gainsville", ), ("Galveston", ), ("Houston", ), ("Huntsville", ), ("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

El_paso_r = (("Fort Stockton", ), ("Fort Worth", ), ("Gainsville", ), ("Galveston", ), ("Houston", ), ("Huntsville", ), ("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Fort_Stockton_r = (("Fort Worth", ), ("Gainsville", ), ("Galveston", ), ("Houston", ), ("Huntsville", ), ("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Fort_Worth_r = (("Gainsville", ), ("Galveston", ), ("Houston", ), ("Huntsville", ), ("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Gainsville_r = (("Galveston", ), ("Houston", ), ("Huntsville", ), ("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Galveston_r = (("Houston", ), ("Huntsville", ), ("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Houston_r = (("Huntsville", ), ("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Huntsville_r = (("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Junction_r = (("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Kingsville_r = (("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Laredo_r = (("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Longview_r = (("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Lubbock_r = (("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Lufkin_r = (("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

McAllen_r = (("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Odessa_r = (("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Orange_r = (("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Ozona_r = (("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Paris_r = (("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Pecos_r = (("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

San_Angelo_r = (("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

San_Antonio_r = (("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

South_Padre_is = (("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Temple_r = (("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Texarkana_r = (("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Tyler_r = (("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Van_Horn_r = (("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Victoria_r = (("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Waco_r = (("Wichita Falls", ), ("Yoakum", ))

Whichita_Falls_r = (("Yoakum", ))

"""
