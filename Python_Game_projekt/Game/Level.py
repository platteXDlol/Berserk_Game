import pygame


def Draw_Platforms(DISPLAYSURF, screen_height, screen_width, platform_position_X):

    platform_X = [
        platform_position_X + (screen_width / 100 * 52.08),  # 1000
        platform_position_X + (screen_width / 100 * 104.17),  # 2000
        platform_position_X + (screen_width / 100 * 156.25),  # 3000
        platform_position_X + (screen_width / 100 * 208.33),  # 4000
        platform_position_X + (screen_width / 100 * 260.42),  # 5000
        platform_position_X + (screen_width / 100 * 312.5),  # 6000
        platform_position_X + (screen_width / 100 * 364.58),  # 7000
        platform_position_X + (screen_width / 100 * 416.67),  # 8000
        platform_position_X + (screen_width / 100 * 468.75),  # 9000
        platform_position_X + (screen_width / 100 * 520.83),  # 10000
        platform_position_X + (screen_width / 100 * 572.92),  # 11000
        platform_position_X + (screen_width / 100 * 625),  # 12000
        platform_position_X + (screen_width / 100 * 677.08),  # 13000
        platform_position_X + (screen_width / 100 * 729.17),  # 14000
        platform_position_X + (screen_width / 100 * 781.25),  # 15000
        platform_position_X + (screen_width / 100 * 833.33),  # 16000
        platform_position_X + (screen_width / 100 * 885.42),  # 17000
        platform_position_X + (screen_width / 100 * 937.5),  # 18000
        platform_position_X + (screen_width / 100 * 989.58),  # 19000
        platform_position_X + (screen_width / 100 * 1041.67),  # 20000
        platform_position_X + (screen_width / 100 * 1093.75),  # 21000
        platform_position_X + (screen_width / 100 * 1145.83),  # 22000
        platform_position_X + (screen_width / 100 * 1197.92),  # 23000
        platform_position_X + (screen_width / 100 * 1250),  # 24000
        platform_position_X + (screen_width / 100 * 1302.08),  # 25000
        platform_position_X + (screen_width / 100 * 1354.17),  # 26000

    ]

    # Platform Y positions: mixed heights for varying difficulty
    platform_Y = [
        screen_height / 100 * 75,  # Lower platform for easy walking
        screen_height / 100 * 60,  # Medium height
        screen_height / 100 * 80,  # High platform
        screen_height / 100 * 65,  # Mid height for jump
        screen_height / 100 * 55,  # Lower platform
        screen_height / 100 * 60,  # Mid-high platform for jump
        screen_height / 100 * 45,  # Low enough for easy jump
        screen_height / 100 * 50,  # Mid platform, easy jump
        screen_height / 100 * 40,  # High platform, but reachable
        screen_height / 100 * 50,  # Low platform
        screen_height / 100 * 55,  # Mid height
        screen_height / 100 * 60,  # Platform at medium height
        screen_height / 100 * 45,  # Lower platform for walking
        screen_height / 100 * 50,  # Mid height platform
        screen_height / 100 * 55,  # Slightly higher platform
        screen_height / 100 * 65,  # Higher platform for jump
        screen_height / 100 * 50,  # Lower platform
        screen_height / 100 * 45,  # Another low platform for walking
        screen_height / 100 * 50,  # Mid platform
        screen_height / 100 * 40,  # Slightly higher platform, requiring a jump
        screen_height / 100 * 45,  # Mid platform
        screen_height / 100 * 50,  # Last platform, mid height
        screen_height / 100 * 55,  # Mid height
        screen_height / 100 * 60,  # Slightly higher platform
        screen_height / 100 * 65,  # Higher platform
        screen_height / 100 * 50,  # Last reachable platform

    ]

    # Platform length: balanced length for each platform
    platform_length = [
        screen_width / 100 * 15,  # Small platform
        screen_width / 100 * 18,  # Longer platform
        screen_width / 100 * 15,  # Short platform for fast timing
        screen_width / 100 * 14,  # Medium platform
        screen_width / 100 * 20,  # Longer platform for stability
        screen_width / 100 * 16,  # Medium platform
        screen_width / 100 * 18,  # Medium platform
        screen_width / 100 * 12,  # Shorter platform for precision
        screen_width / 100 * 14,  # Medium-sized platform
        screen_width / 100 * 15,  # Medium platform
        screen_width / 100 * 16,  # Medium platform
        screen_width / 100 * 18,  # Larger platform
        screen_width / 100 * 14,  # Medium-sized platform
        screen_width / 100 * 20,  # Larger platform
        screen_width / 100 * 14,  # Medium platform
        screen_width / 100 * 12,  # Short platform
        screen_width / 100 * 18,  # Larger platform
        screen_width / 100 * 15,  # Medium platform
        screen_width / 100 * 10,  # Shorter platform for timing
        screen_width / 100 * 14,  # Medium platform
        screen_width / 100 * 16,  # Medium platform
        screen_width / 100 * 20,  # Final larger platform
        screen_width / 100 * 18,  # Larger platform
        screen_width / 100 * 15,  # Medium platform
        screen_width / 100 * 12,  # Shorter platform
        screen_width / 100 * 18,  # Final platform

    ]

    # Platform width remains constant
    platform_width = screen_height / 100 * 2

    # Create the platforms as rectangles
    platforms = [
        pygame.Rect(platform_X[i], platform_Y[i], platform_length[i], platform_width)
        for i in range(len(platform_X))
    ]

    # Draw all the platforms
    for platform in platforms:
        pygame.draw.rect(DISPLAYSURF, (0, 255, 100), platform)

    return platforms


def Draw_Spikes(DISPLAYSURF, l, screen_width, screen_height, platform_position_X, Spikes_img):
    # More spikes spread across the level, with consistent height
    spike_X = [
        platform_position_X + (screen_width / 100 * 62.5),  # 1200
        platform_position_X + (screen_width / 100 * 65.1),  # 1250
        platform_position_X + (screen_width / 100 * 67.7),  # 1300
        platform_position_X + (screen_width / 100 * 70.3),  # 1350
        platform_position_X + (screen_width / 100 * 72.9),  # 1400
        platform_position_X + (screen_width / 100 * 75.5),  # 1450
        platform_position_X + (screen_width / 100 * 78.1),  # 1500
        platform_position_X + (screen_width / 100 * 80.7),  # 1550
        platform_position_X + (screen_width / 100 * 83.3),  # 1600
        platform_position_X + (screen_width / 100 * 85.9),  # 1650
        platform_position_X + (screen_width / 100 * 88.5),  # 1700
        platform_position_X + (screen_width / 100 * 91.1),  # 1750
        platform_position_X + (screen_width / 100 * 93.7),  # 1800
        platform_position_X + (screen_width / 100 * 96.4),  # 1850
        platform_position_X + (screen_width / 100 * 99.0),  # 1900
        platform_position_X + (screen_width / 100 * 101.6),  # 1950
        platform_position_X + (screen_width / 100 * 104.2),  # 2000
        platform_position_X + (screen_width / 100 * 106.8),  # 2050
        platform_position_X + (screen_width / 100 * 109.4),  # 2100
        platform_position_X + (screen_width / 100 * 112.0),  # 2150
        platform_position_X + (screen_width / 100 * 114.6),  # 2200
        platform_position_X + (screen_width / 100 * 117.2),  # 2250
        platform_position_X + (screen_width / 100 * 119.8),  # 2300
        platform_position_X + (screen_width / 100 * 122.4),  # 2350
        platform_position_X + (screen_width / 100 * 125.0),  # 2400
        platform_position_X + (screen_width / 100 * 127.6),  # 2450
        platform_position_X + (screen_width / 100 * 130.2),  # 2500
        platform_position_X + (screen_width / 100 * 132.8),  # 2550
        platform_position_X + (screen_width / 100 * 135.4),  # 2600
        platform_position_X + (screen_width / 100 * 138.0),  # 2650
        platform_position_X + (screen_width / 100 * 140.6),  # 2700
        platform_position_X + (screen_width / 100 * 143.2),  # 2750
        platform_position_X + (screen_width / 100 * 145.8),  # 2800
        platform_position_X + (screen_width / 100 * 148.4),  # 2850
        platform_position_X + (screen_width / 100 * 151.0),  # 2900
        platform_position_X + (screen_width / 100 * 153.6),  # 2950
        platform_position_X + (screen_width / 100 * 156.2),  # 3000
        platform_position_X + (screen_width / 100 * 158.8),  # 3050
        platform_position_X + (screen_width / 100 * 161.4),  # 3100
        platform_position_X + (screen_width / 100 * 208.3),  # 4000
        platform_position_X + (screen_width / 100 * 210.9),  # 4050
        platform_position_X + (screen_width / 100 * 213.5),  # 4100
        platform_position_X + (screen_width / 100 * 216.1),  # 4150
        platform_position_X + (screen_width / 100 * 218.7),  # 4200
        platform_position_X + (screen_width / 100 * 221.3),  # 4250
        platform_position_X + (screen_width / 100 * 223.9),  # 4300
        platform_position_X + (screen_width / 100 * 226.5),  # 4350
        platform_position_X + (screen_width / 100 * 229.2),  # 4400
        platform_position_X + (screen_width / 100 * 231.8),  # 4450
        platform_position_X + (screen_width / 100 * 234.4),  # 4500
        platform_position_X + (screen_width / 100 * 237.0),  # 4550
        platform_position_X + (screen_width / 100 * 239.6),  # 4600
        platform_position_X + (screen_width / 100 * 242.2),  # 4650
        platform_position_X + (screen_width / 100 * 244.8),  # 4700
        platform_position_X + (screen_width / 100 * 247.4),  # 4750
        platform_position_X + (screen_width / 100 * 250.0),  # 4800
        platform_position_X + (screen_width / 100 * 252.6),  # 4850
        platform_position_X + (screen_width / 100 * 255.2),  # 4900
        platform_position_X + (screen_width / 100 * 257.8),  # 4950
        platform_position_X + (screen_width / 100 * 260.4),  # 5000
        platform_position_X + (screen_width / 100 * 263.0),  # 5050
        platform_position_X + (screen_width / 100 * 265.6),  # 5100
        platform_position_X + (screen_width / 100 * 268.2),  # 5150
        platform_position_X + (screen_width / 100 * 270.8),  # 5200
        platform_position_X + (screen_width / 100 * 273.4),  # 5250
        platform_position_X + (screen_width / 100 * 276.0),  # 5300
        platform_position_X + (screen_width / 100 * 278.6),  # 5350
        platform_position_X + (screen_width / 100 * 281.2),  # 5400
        platform_position_X + (screen_width / 100 * 283.8),  # 5450
        platform_position_X + (screen_width / 100 * 286.4),  # 5500
        platform_position_X + (screen_width / 100 * 289.0),  # 5550
        platform_position_X + (screen_width / 100 * 291.6),  # 5600
        platform_position_X + (screen_width / 100 * 294.2),  # 5650
        platform_position_X + (screen_width / 100 * 296.8),  # 5700
        platform_position_X + (screen_width / 100 * 299.4),  # 5750
        platform_position_X + (screen_width / 100 * 302.0),  # 5800
        platform_position_X + (screen_width / 100 * 304.6),  # 5850
        platform_position_X + (screen_width / 100 * 307.2),  # 5900
        platform_position_X + (screen_width / 100 * 309.8),  # 5950
        platform_position_X + (screen_width / 100 * 312.4),  # 6000
        platform_position_X + (screen_width / 100 * 315.0),  # 6050
        platform_position_X + (screen_width / 100 * 317.6),  # 6100
        platform_position_X + (screen_width / 100 * 320.2),  # 6150
        platform_position_X + (screen_width / 100 * 322.8),  # 6200
        platform_position_X + (screen_width / 100 * 325.4),  # 6250
        platform_position_X + (screen_width / 100 * 328.0),  # 6300
        platform_position_X + (screen_width / 100 * 330.6),  # 6350
        platform_position_X + (screen_width / 100 * 333.2),  # 6400
        platform_position_X + (screen_width / 100 * 335.8),  # 6450
        platform_position_X + (screen_width / 100 * 338.4),  # 6500
        platform_position_X + (screen_width / 100 * 341.0),  # 6550
        platform_position_X + (screen_width / 100 * 343.6),  # 6600
        platform_position_X + (screen_width / 100 * 346.2),  # 6650
        platform_position_X + (screen_width / 100 * 348.8),  # 6700
        platform_position_X + (screen_width / 100 * 351.4),  # 6750
        platform_position_X + (screen_width / 100 * 354.0),  # 6800
        platform_position_X + (screen_width / 100 * 356.6),  # 6850
        platform_position_X + (screen_width / 100 * 359.2),  # 6900
        platform_position_X + (screen_width / 100 * 361.8),  # 6950
        platform_position_X + (screen_width / 100 * 364.4),  # 7000
        platform_position_X + (screen_width / 100 * 367.0),  # 7050
        platform_position_X + (screen_width / 100 * 369.6),  # 7100
        platform_position_X + (screen_width / 100 * 372.2),  # 7150
        platform_position_X + (screen_width / 100 * 374.8),  # 7200
        platform_position_X + (screen_width / 100 * 377.4),  # 7250
        platform_position_X + (screen_width / 100 * 380.0),  # 7300
        platform_position_X + (screen_width / 100 * 382.6),  # 7350
        platform_position_X + (screen_width / 100 * 385.2),  # 7400
        platform_position_X + (screen_width / 100 * 387.8),  # 7450
        platform_position_X + (screen_width / 100 * 390.4),  # 7500
        platform_position_X + (screen_width / 100 * 393.0),  # 7550
        platform_position_X + (screen_width / 100 * 395.6),  # 7600
        platform_position_X + (screen_width / 100 * 398.2),  # 7650
        platform_position_X + (screen_width / 100 * 400.8),  # 7700
        platform_position_X + (screen_width / 100 * 403.4),  # 7750
        platform_position_X + (screen_width / 100 * 406.0),  # 7800
        platform_position_X + (screen_width / 100 * 408.6),  # 7850
        platform_position_X + (screen_width / 100 * 411.2),  # 7900
        platform_position_X + (screen_width / 100 * 413.8),  # 7950
        platform_position_X + (screen_width / 100 * 416.4),  # 8000
        platform_position_X + (screen_width / 100 * 419.0),  # 8050
        platform_position_X + (screen_width / 100 * 421.6),  # 8100
        platform_position_X + (screen_width / 100 * 424.2),  # 8150
        platform_position_X + (screen_width / 100 * 426.8),  # 8200
        platform_position_X + (screen_width / 100 * 429.4),  # 8250
        platform_position_X + (screen_width / 100 * 432.0),  # 8300
        platform_position_X + (screen_width / 100 * 434.6),  # 8350
        platform_position_X + (screen_width / 100 * 437.2),  # 8400
        platform_position_X + (screen_width / 100 * 439.8),  # 8450
        platform_position_X + (screen_width / 100 * 729.2),  # 14000
        platform_position_X + (screen_width / 100 * 731.8),  # 14050
        platform_position_X + (screen_width / 100 * 734.4),  # 14100
        platform_position_X + (screen_width / 100 * 737.0),  # 14150
        platform_position_X + (screen_width / 100 * 739.6),  # 14200
        platform_position_X + (screen_width / 100 * 742.2),  # 14250
        platform_position_X + (screen_width / 100 * 744.8),  # 14300
        platform_position_X + (screen_width / 100 * 747.4),  # 14350
        platform_position_X + (screen_width / 100 * 750.0),  # 14400
        platform_position_X + (screen_width / 100 * 752.6),  # 14450
        platform_position_X + (screen_width / 100 * 755.2),  # 14500
        platform_position_X + (screen_width / 100 * 757.8),  # 14550
        platform_position_X + (screen_width / 100 * 760.4),  # 14600
        platform_position_X + (screen_width / 100 * 763.0),  # 14650
        platform_position_X + (screen_width / 100 * 765.6),  # 14700
        platform_position_X + (screen_width / 100 * 768.2),  # 14750
        platform_position_X + (screen_width / 100 * 770.8),  # 14800
        platform_position_X + (screen_width / 100 * 773.4),  # 14850
        platform_position_X + (screen_width / 100 * 776.0),  # 14900
        platform_position_X + (screen_width / 100 * 778.6),  # 14950
        platform_position_X + (screen_width / 100 * 781.2),  # 15000
        platform_position_X + (screen_width / 100 * 783.8),  # 15050
        platform_position_X + (screen_width / 100 * 786.4),  # 15100
        platform_position_X + (screen_width / 100 * 789.0),  # 15150
        platform_position_X + (screen_width / 100 * 885.4),  # 17000
        platform_position_X + (screen_width / 100 * 888.0),  # 17050
        platform_position_X + (screen_width / 100 * 890.6),  # 17100
        platform_position_X + (screen_width / 100 * 893.2),  # 17150
        platform_position_X + (screen_width / 100 * 895.8),  # 17200
        platform_position_X + (screen_width / 100 * 898.4),  # 17250
        platform_position_X + (screen_width / 100 * 901.0),  # 17300
        platform_position_X + (screen_width / 100 * 903.6),  # 17350
        platform_position_X + (screen_width / 100 * 906.2),  # 17400
        platform_position_X + (screen_width / 100 * 908.8),  # 17450
        platform_position_X + (screen_width / 100 * 911.4),  # 17500
        platform_position_X + (screen_width / 100 * 914.0),  # 17550
        platform_position_X + (screen_width / 100 * 916.6),  # 17600
        platform_position_X + (screen_width / 100 * 919.2),  # 17650
        platform_position_X + (screen_width / 100 * 921.8),  # 17700
        platform_position_X + (screen_width / 100 * 924.4),  # 17750
        platform_position_X + (screen_width / 100 * 927.0),  # 17800
        platform_position_X + (screen_width / 100 * 929.6),  # 17850
        platform_position_X + (screen_width / 100 * 932.2),  # 17900
        platform_position_X + (screen_width / 100 * 934.8),  # 17950
        platform_position_X + (screen_width / 100 * 937.4),  # 18000
        platform_position_X + (screen_width / 100 * 940.0),  # 18050
        platform_position_X + (screen_width / 100 * 942.6),  # 18100
        platform_position_X + (screen_width / 100 * 945.2),  # 18150
        platform_position_X + (screen_width / 100 * 947.8),  # 18200
        platform_position_X + (screen_width / 100 * 950.4),  # 18250
        platform_position_X + (screen_width / 100 * 953.0),  # 18300
        platform_position_X + (screen_width / 100 * 955.6),  # 18350
        platform_position_X + (screen_width / 100 * 958.2),  # 18400
        platform_position_X + (screen_width / 100 * 960.8),  # 18450
        platform_position_X + (screen_width / 100 * 963.4),  # 18500
        platform_position_X + (screen_width / 100 * 966.0),  # 18550
        platform_position_X + (screen_width / 100 * 968.6),  # 18600
        platform_position_X + (screen_width / 100 * 971.2),  # 18650
        platform_position_X + (screen_width / 100 * 973.8),  # 18700
        platform_position_X + (screen_width / 100 * 976.4),  # 18750
        platform_position_X + (screen_width / 100 * 979.0),  # 18800
        platform_position_X + (screen_width / 100 * 981.6),  # 18850
        platform_position_X + (screen_width / 100 * 984.2),  # 18900
        platform_position_X + (screen_width / 100 * 986.8),  # 18950
        platform_position_X + (screen_width / 100 * 989.4),  # 19000
        platform_position_X + (screen_width / 100 * 992.0),  # 19050
        platform_position_X + (screen_width / 100 * 994.6),  # 19100
        platform_position_X + (screen_width / 100 * 997.2),  # 19150
        platform_position_X + (screen_width / 100 * 999.8),  # 19200
        platform_position_X + (screen_width / 100 * 1002.4),  # 19250
        platform_position_X + (screen_width / 100 * 1005.0),  # 19300
        platform_position_X + (screen_width / 100 * 1007.6),  # 19350
        platform_position_X + (screen_width / 100 * 1010.2),  # 19400
        platform_position_X + (screen_width / 100 * 1012.8),  # 19450
        platform_position_X + (screen_width / 100 * 1015.4),  # 19500
        platform_position_X + (screen_width / 100 * 1018.0),  # 19550
        platform_position_X + (screen_width / 100 * 1020.6),  # 19600
        platform_position_X + (screen_width / 100 * 1023.2),  # 19650
        platform_position_X + (screen_width / 100 * 1025.8),  # 19700
        platform_position_X + (screen_width / 100 * 1028.4),  # 19750
        platform_position_X + (screen_width / 100 * 1031.0),  # 19800
        platform_position_X + (screen_width / 100 * 1033.6),  # 19850
        platform_position_X + (screen_width / 100 * 1036.2),  # 19900
        platform_position_X + (screen_width / 100 * 1038.8),  # 19950
        platform_position_X + (screen_width / 100 * 1041.4),  # 20000
        platform_position_X + (screen_width / 100 * 1044.0),  # 20050
        platform_position_X + (screen_width / 100 * 1046.6),  # 20100
        platform_position_X + (screen_width / 100 * 1049.2),  # 20150
        platform_position_X + (screen_width / 100 * 1051.8),  # 20200
        platform_position_X + (screen_width / 100 * 1054.4),  # 20250
        platform_position_X + (screen_width / 100 * 1057.0),  # 20300
        platform_position_X + (screen_width / 100 * 1059.6),  # 20350
        platform_position_X + (screen_width / 100 * 1062.2),  # 20400
        platform_position_X + (screen_width / 100 * 1064.8),  # 20450
        platform_position_X + (screen_width / 100 * 1067.4),  # 20500
        platform_position_X + (screen_width / 100 * 1070.0),  # 20550
        platform_position_X + (screen_width / 100 * 1072.6),  # 20600
        platform_position_X + (screen_width / 100 * 1075.2),  # 20650
        platform_position_X + (screen_width / 100 * 1077.8),  # 20700
        platform_position_X + (screen_width / 100 * 1080.4),  # 20750
        platform_position_X + (screen_width / 100 * 1083.0),  # 20800
        platform_position_X + (screen_width / 100 * 1085.6),  # 20850
        platform_position_X + (screen_width / 100 * 1088.2),  # 20900
        platform_position_X + (screen_width / 100 * 1090.8),  # 20950
        platform_position_X + (screen_width / 100 * 1093.4),  # 21000
        platform_position_X + (screen_width / 100 * 1096.0),  # 21050
        platform_position_X + (screen_width / 100 * 1098.6),  # 21100
        platform_position_X + (screen_width / 100 * 1101.2),  # 21150
        platform_position_X + (screen_width / 100 * 1103.8),  # 21200
        platform_position_X + (screen_width / 100 * 1106.4),  # 21250
        platform_position_X + (screen_width / 100 * 1109.0),  # 21300
        platform_position_X + (screen_width / 100 * 1111.6),  # 21350
        platform_position_X + (screen_width / 100 * 1114.2),  # 21400
        platform_position_X + (screen_width / 100 * 1333.4),  # 25500
        platform_position_X + (screen_width / 100 * 1336.0),  # 25550
        platform_position_X + (screen_width / 100 * 1338.6),  # 25600
        platform_position_X + (screen_width / 100 * 1341.2),  # 25650
        platform_position_X + (screen_width / 100 * 1343.8),  # 25700
        platform_position_X + (screen_width / 100 * 1346.4),  # 25750
        platform_position_X + (screen_width / 100 * 1349.0),  # 25800
        platform_position_X + (screen_width / 100 * 1351.6),  # 25850
        platform_position_X + (screen_width / 100 * 1354.2),  # 25900
        platform_position_X + (screen_width / 100 * 1356.8),  # 25950
        platform_position_X + (screen_width / 100 * 1359.4),  # 26000
        platform_position_X + (screen_width / 100 * 1362.0),  # 26050
    ]




    # Consistent height for all spikes
    spike_Y = screen_height / 100 * 92

    # Create rectangles for each spike
    spikes = [
        pygame.Rect(spike_X[i], spike_Y, Spikes_img.get_width(), Spikes_img.get_height())
        for i in range(len(spike_X))
    ]

    # Draw all the spikes
    for spike in spikes:
        DISPLAYSURF.blit(Spikes_img, (spike.x, spike.y))

    # Create the spike masks for collision detection
    spike_masks = [
        pygame.mask.from_surface(Spikes_img)
        for _ in range(len(spike_X))
    ]

    # Store mask positions for collision detection
    spike_mask_positions = [
        {'mask': spike_masks[i], 'pos': (spike_X[i], spike_Y)}
        for i in range(len(spikes))
    ]

    return spike_mask_positions
