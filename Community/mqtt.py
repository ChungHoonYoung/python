#-*- coding:utf-8 -*-
import paho.mqtt.client as mqtt

mqtt = mqtt.Client("python_pub") 

mqtt.connect("172.30.1.20", 1883) 

mqtt.publish("HomeSweetHome", "쾌남박도연") 

mqtt.loop(2)