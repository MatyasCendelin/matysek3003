def on_forever():
    if sonarbit.sonarbit_distance(Distance_Unit.DISTANCE_UNIT_CM, DigitalPin.P0) <= 8:
        basic.show_number(sonarbit.sonarbit_distance(Distance_Unit.DISTANCE_UNIT_CM, DigitalPin.P0))
        wuKong.set_servo_angle(wuKong.ServoTypeList._360, wuKong.ServoList.S0, 276)
        basic.pause(5000)
        wuKong.set_servo_angle(wuKong.ServoTypeList._360, wuKong.ServoList.S0, 0)
    elif sonarbit.sonarbit_distance(Distance_Unit.DISTANCE_UNIT_CM, DigitalPin.P0) > 8:
        basic.show_icon(IconNames.NO)
        wuKong.set_servo_angle(wuKong.ServoTypeList._360, wuKong.ServoList.S0, 0)
        basic.pause(500)
basic.forever(on_forever)
