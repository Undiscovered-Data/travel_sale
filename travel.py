#!/usr/bin/python3

Abilene_r = (("Amarillo", 266), ("Austin", 213), ("Beaumont", 412), ("Big Bend", 392), ("Big Spring", 107), ("Brownsville", 516), ("Brownwood", 77), ("Bryan", 253), ("Childress", 154), ("Corpus Christi", 387), ("Dalhart", 343),  ("Dallas", 180), ("Del Rio", 246), ("Denison", 235), ("Eagle Pass", 298),  ("El Paso", 439), ("Fort Stockton", 250), ("Fort Worth", 150), ("Gainsville", 195), ("Galveston", 398), ("Houston", 348), ("Huntsville", 304), ("Junction", 144), ("Kingsville", 397), ("Laredo", 373), ("Longview", 305), ("Lubbock", 162), ("Lufkin", 336), ("McAllen", 480), ("Odessa", 167), ("Orange", 434), ("Ozona", 170), ("Paris", 281), ("Pecos", 240), ("San Angelo", 89), ("San Antonio", 244), ("South Padre Is", 530), ("Temple", 181), ("Texarkana", 359), ("Tyler", 277), ("Van Horn", 328), ("Victoria", 334), ("Waco", 183), ("Wichita Falls", 141), ("Yoakum", 304))
5
Amarillo_r = (("Austin", 478), ("Beaumont", 637), ("Big Bend", 484), ("Big Spring", 222), ("Brownsville", 765), ("Brownwood", 342), ("Bryan", 503), ("Childress", 116), ("Corpus Christi", 636), ("Dalhart", 82),  ("Dallas", 361), ("Del Rio", 450), ("Denison", 348), ("Eagle Pass", 505),  ("El Paso", 418), ("Fort Stockton", 338), ("Fort Worth", 337), ("Gainsville", 309), ("Galveston", 646), ("Houston", 596), ("Huntsville", 528), ("Junction", 380), ("Kingsville", 646), ("Laredo", 609), ("Longview", 482), ("Lubbock", 119), ("Lufkin", 529), ("McAllen", 728), ("Odessa", 255), ("Orange", 649), ("Ozona", 336), ("Paris", 403), ("Pecos", 320), ("San Angelo", 293), ("San Antonio", 493), ("South Padre Is", 779), ("Temple", 444), ("Texarkana", 495), ("Tyler", 457), ("Van Horn", 401), ("Victoria", 600), ("Waco", 423), ("Wichita Falls", 225), ("Yoakum", 566))

Austin_r = (("Beaumont", 238), ("Big Bend", 462), ("Big Spring", 289), ("Brownsville", 325), ("Brownwood", 137), ("Bryan", 100), ("Childress", 367), ("Corpus Christi", 192), ("Dalhart", 556),  ("Dallas", 192), ("Del Rio", 232), ("Denison", 267), ("Eagle Pass", 220),  ("El Paso", 573), ("Fort Stockton", 335), ("Fort Worth", 187), ("Gainsville", 252), ("Galveston", 206), ("Houston", 162), ("Huntsville", 153), ("Junction", 139), ("Kingsville", 206), ("Laredo", 232), ("Longview", 256), ("Lubbock", 368), ("Lufkin", 219), ("McAllen", 300), ("Odessa", 334), ("Orange", 262), ("Ozona", 229), ("Paris", 294), ("Pecos", 388), ("San Angelo", 203), ("San Antonio", 79), ("South Padre Is", 339), ("Temple", 67), ("Texarkana", 340), ("Tyler", 224), ("Van Horn", 454), ("Victoria", 122), ("Waco", 102), ("Wichita Falls", 283), ("Yoakum", 88))

Beaumont_r = (("Big Bend", 699), ("Big Spring", 519), ("Brownsville", 437), ("Brownwood", 350), ("Bryan", 158), ("Childress", 521), ("Corpus Christi", 288), ("Dalhart", 719),  ("Dallas", 276), ("Del Rio", 434), ("Denison", 321), ("Eagle Pass", 421),  ("El Paso", 810), ("Fort Stockton", 572), ("Fort Worth", 301), ("Gainsville", 345), ("Galveston", 78), ("Houston", 86), ("Huntsville", 113), ("Junction", 376), ("Kingsville", 317), ("Laredo", 396), ("Longview", 194), ("Lubbock", 574), ("Lufkin", 108), ("McAllen", 430), ("Odessa", 567), ("Orange", 24), ("Ozona", 466), ("Paris", 292), ("Pecos", 625), ("San Angelo", 436), ("San Antonio", 281), ("South Padre Is", 451), ("Temple", 230), ("Texarkana", 256), ("Tyler", 192), ("Van Horn", 690), ("Victoria", 209), ("Waco", 242), ("Wichita Falls", 412), ("Yoakum", 204))


Big_bend_r = (("Big Spring", ), ("Brownsville", ), ("Brownwood", ), ("Bryan", ), ("Childress", ), ("Corpus Christi", ), ("Dalhart", ),  ("Dallas", ), ("Del Rio", ), ("Denison", ), ("Eagle Pass", ),  ("El Paso", ), ("Fort Stockton", ), ("Fort Worth", ), ("Gainsville", ), ("Galveston", ), ("Houston", ), ("Huntsville", ), ("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

"""
Big_Spring_r = (("Brownsville", ), ("Brownwood", ), ("Bryan", ), ("Childress", ), ("Corpus Christi", ), ("Dalhart", ),  ("Dallas", ), ("Del Rio", ), ("Denison", ), ("Eagle Pass", ),  ("El Paso", ), ("Fort Stockton", ), ("Fort Worth", ), ("Gainsville", ), ("Galveston", ), ("Houston", ), ("Huntsville", ), ("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Brownsville_r = (("Brownwood", ), ("Bryan", ), ("Childress", ), ("Corpus Christi", ), ("Dalhart", ),  ("Dallas", ), ("Del Rio", ), ("Denison", ), ("Eagle Pass", ),  ("El Paso", ), ("Fort Stockton", ), ("Fort Worth", ), ("Gainsville", ), ("Galveston", ), ("Houston", ), ("Huntsville", ), ("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

Brownwood_r = ("Bryan", ), ("Childress", ), ("Corpus Christi", ), ("Dalhart", ),  ("Dallas", ), ("Del Rio", ), ("Denison", ), ("Eagle Pass", ),  ("El Paso", ), ("Fort Stockton", ), ("Fort Worth", ), ("Gainsville", ), ("Galveston", ), ("Houston", ), ("Huntsville", ), ("Junction", ), ("Kingsville", ), ("Laredo", ), ("Longview", ), ("Lubbock", ), ("Lufkin", ), ("McAllen", ), ("Odessa", ), ("Orange", ), ("Ozona", ), ("Paris", ), ("Pecos", ), ("San Angelo", ), ("San Antonio", ), ("South Padre Is", ), ("Temple", ), ("Texarkana", ), ("Tyler", ), ("Van Horn", ), ("Victoria", ), ("Waco", ), ("Wichita Falls", ), ("Yoakum", ))

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
